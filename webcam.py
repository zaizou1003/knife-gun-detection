import cv2
import torch
from PIL import Image
def main():
    # Load your custom YOLOv5 model
    model = torch.hub.load('C:/Users/Mega-PC/Desktop/deep/yolov5', 'custom', path= r'yolov5\runs\train\exp6\weights\best.pt', source='local')
    #model = DetectMultiBackend('runs/train/exp6/weights/best.pt')

    # Open webcam (use 0 for the default webcam)
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame. Exiting...")
            break

        # Convert the frame to RGB format and run inference
        img_to_read = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        results = model(img_to_read)

        # Loop through detections and draw bounding boxes
        for det in results.pred[0]:
            x1, y1, x2, y2, conf, cls = det.cpu().numpy()

            if conf > 0.5:  # Confidence threshold
                label = f"{model.names[int(cls)]} {conf:.2f}"
                # Draw bounding box and label
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Show the frame with detections
        cv2.imshow("Object Detection", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
