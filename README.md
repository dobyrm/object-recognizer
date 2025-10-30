# Object Recognizer

The project supports object detection on images, videos, and webcam streams, with the ability to save the processed results.

---

## How to Run the Project

### Requirements

- Docker
- Docker Compose
- Python 3.9+ (if running locally)

---

### 1 Build the container

```bash
docker-compose build
```

Or without Docker Compose:

```bash
docker build -t object-recognizer .
```

---

### 2 Run the container

```bash
docker-compose up -d
```

---

### 3 Access bash inside the container

```bash
docker exec -it object-recognizer bash
```

*(If already running via `docker-compose up`)*

---

### 4 Run Jupyter Notebook

```bash
jupyter notebook --ip=0.0.0.0 --allow-root
```

---

## Project Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── main.py
└── README.md
```

---

## Verify OpenCV Installation

Inside the container:

```bash
python
```

Then:

```python
import cv2
print(cv2.__version__)
```

---

## CLI Usage (main.py)

### Detect objects on image
```bash
python main.py --img storage/example.jpg --show
```

### Save result image
```bash
python main.py --img storage/example.jpg --save output/example.jpg
```

### Detect on video
```bash
python main.py --video storage/example.mp4 --show
```

### Process & save video
```bash
python main.py --video storage/example.mp4 --save output/example.mp4
```

### Webcam detection (if enabled)
```bash
python main.py --webcam
```

---

## Controls

| Key | Action |
|---|---|
| **Q** | Quit video/webcam window |

---

## License

MIT License.
