#/bin/bash
HF_DATASETS_OFFLINE=1
TRANSFORMERS_OFFLINE=1
CUDA_LAUNCH_BLOCKING=1

uvicorn main:app --reload --host 0.0.0.0 --port 2022 --workers 100
