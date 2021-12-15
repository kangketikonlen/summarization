import requests
from bs4 import BeautifulSoup
from transformers import pipeline, PegasusForConditionalGeneration, PegasusTokenizer


def sum_v1(artikel):
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summary = summarizer(artikel, max_length=100, min_length=20, do_sample=False)
    return summary[0]["summary_text"]


def sum_v2(url):
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all(["h1", "p"])
    text = [result.text for result in results]
    artikel = " ".join(text)
    chunks = chunks_text(artikel)
    res = summarizer(chunks, max_length=100, min_length=20, do_sample=False)
    return " ".join([summ["summary_text"] for summ in res])


def sum_v3(text):
    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
    summary = model.generate(**tokens)
    return tokenizer.decode(summary[0])


def chunks_text(artikel):
    max_chunk = 250
    current_chunk = 0
    artikel = artikel.replace(".", ".<eos>")
    artikel = artikel.replace("?", "?<eos>")
    artikel = artikel.replace("!", "!<eos>")
    sentences = artikel.split("<eos>")
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(" ")) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(" "))
            else:
                current_chunk += 1
                chunks.append(sentence.split(" "))
        else:
            chunks.append(sentence.split(" "))
    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = " ".join(chunks[chunk_id])
    return chunks
