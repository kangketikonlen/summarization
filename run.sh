#/bin/bash
HF_DATASETS_OFFLINE=1
TRANSFORMERS_OFFLINE=1

# uvicorn main:app --reload --host 0.0.0.0 --port 2022
gunicorn main:app --bind=0.0.0.0:2022 -k uvicorn.workers.UvicornWorker --timeout 1000
