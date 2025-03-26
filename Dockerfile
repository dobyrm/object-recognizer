FROM python:3.12-slim

WORKDIR /app

COPY . ./

RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    && pip install --no-cache-dir opencv-python matplotlib jupyter

CMD ["bash"]
