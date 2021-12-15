from transformers import pipeline


def sum_v1(artikel):
    summarizer = pipeline(model="sshleifer/distilbart-cnn-12-6")
    summary = summarizer(
        artikel, max_length=200, min_length=20, num_workers=1000, batch_size=1
    )
    return summary[0]["summary_text"]
