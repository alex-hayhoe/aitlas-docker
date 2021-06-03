#!/usr/bin/env bash

echo "Running TrainAndEvaluateTask"
exec python3 -m aitlas.run configs/chactun/train_and_evaluate.json
echo "Running PredictImages"
exec python3 -m aitlas.run configs/chactun/predict_images.json
