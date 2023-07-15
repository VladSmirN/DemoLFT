FROM ultralytics/ultralytics:latest
WORKDIR /app
COPY ./models /app/models
COPY ./data /app/data
COPY ./predicts /app/predicts