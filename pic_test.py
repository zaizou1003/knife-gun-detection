import torch
import cv2
import numpy as np

def main():
    # Load your custom YOLOv5 model
    model = torch.hub.load(r'C:\Users\Mega-PC\Desktop\knife-gun-detection\yolov5', 'custom', 
                           path='C:/Users/Mega-PC/Desktop/knife-gun-detection/yolov5/runs/train/exp6/weights/best.pt', 
                           source='local')

    # Load your test image
    img_path = 'C:/Users/Mega-PC/Desktop/deep/depositphotos_197300400-stock-photo-hand-man-holding-knife-isolated.jpg'
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Could not read the image.")
        return

    # Convert image to RGB (YOLOv5 expects RGB format)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Run inference
    results = model(img_rgb)

    # Display results
    results.show()  # This will display the image with bounding boxes

    # Optionally, save the results
    results.save(save_dir='C:/Users/Mega-PC/Desktop/deep/output')  # Save results to the output directory

if __name__ == "__main__":
    main()
