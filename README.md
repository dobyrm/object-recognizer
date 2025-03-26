# Object Recognizer

The project uses OpenCV for object recognition. The library applies computer vision and machine learning algorithms to automate object detection in various fields.

---

## How to Run the Project

### Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 1. Build the container

```bash
docker-compose build
```
Or without Docker Compose:
```bash
docker build -t object-recognizer .
```

### 2. Run the container

```bash
docker-compose up -d
```

### 3. Access bash inside the container

```bash
docker exec -it object-recognizer bash
```
(If already running via `docker-compose up`)

---

### 4. Run the jupyter

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
├── photo-detection.py
└── README.md
```

---

## Check OpenCV

Inside bash in the container:

```bash
python
```
Then in Python interpreter:

```python
import cv2
print(cv2.__version__)
```

---

## License

MIT License.
