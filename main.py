import argparse
from pathlib import Path
import cv2
from ultralytics import YOLO

MODEL_PATH = "models/yolo11n.pt"

def load_model(path: str) -> YOLO:
    if not Path(path).exists():
        raise FileNotFoundError(f"Model not found: {path}")
    return YOLO(path)

def detect_image(model: YOLO, image_path: str):
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    result = model(image_path)[0]
    return result.plot()

def detect_video(model: YOLO, video_path: str, save_path=None):
    if not Path(video_path).exists():
        raise FileNotFoundError(f"Video not found: {video_path}")

    cap = cv2.VideoCapture(video_path)
    writer = None

    if save_path:
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        writer = cv2.VideoWriter(save_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = model(frame)[0]
        frame = result.plot()

        cv2.imshow("Video Detection", frame)

        if writer:
            writer.write(frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    if writer:
        writer.release()
    cv2.destroyAllWindows()

def detect_webcam(model: YOLO):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = model(frame)[0]
        frame = result.plot()
        cv2.imshow("Webcam Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

def parse_args():
    parser = argparse.ArgumentParser(description="YOLO detection CLI")

    parser.add_argument("--img", type=str, help="Path to image")
    parser.add_argument("--video", type=str, help="Path to video")
    parser.add_argument("--webcam", action="store_true", help="Use webcam for detection")
    parser.add_argument("--show", action="store_true", help="Show window")
    parser.add_argument("--save", type=str, help="Path to save output (image/video)")

    return parser.parse_args()

def main():
    args = parse_args()
    model = load_model(MODEL_PATH)

    if args.img:
        img = detect_image(model, args.img)

        if args.show:
            cv2.imshow("Detected Objects", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if args.save:
            cv2.imwrite(args.save, img)
            print(f"Saved to {args.save}")

    elif args.video:
        detect_video(model, args.video, save_path=args.save)
        print(f"Video processing completed. Saved to {args.save}" if args.save else "Video display only.")

    elif args.webcam:
        detect_webcam(model)

    else:
        print("Specify --img, --video, or --webcam")
        exit(1)

if __name__ == "__main__":
    main()
