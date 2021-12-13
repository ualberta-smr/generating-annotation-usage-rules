#!/bin/bash

/wait && python -m pipenv run uvicorn src.main:app --host 0.0.0.0 --port 5000