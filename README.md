# Knife and Gun Detection Project

This project leverages YOLOv5 to detect knives and guns in images and videos. It includes scripts for testing camera functionality, importing datasets, real-time detection via webcam, and image testing. The `exp6` folder contains the best weights and metrics from the training process.

---

## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
  - [Testing Camera Functionality](#testing-camera-functionality)
  - [Importing Datasets](#importing-datasets)
  - [Real-Time Detection](#real-time-detection)
  - [Image Detection](#image-detection)
- [Best Weights and Metrics](#best-weights-and-metrics)
- [Requirements](#requirements)
- [Contributing](#contributing)

---

## Features

1. **Camera Testing**: Verify camera functionality with the `test_camera.py` script.
2. **Dataset Import**: Import datasets from Roboflow using `import.py`.
3. **Real-Time Detection**: Detect knives and guns live using your webcam with `webcam.py`.
4. **Image Detection**: Use `pic_test.py` to label objects in an input image and output the processed image.
5. **Model Weights and Metrics**: The `exp6` folder contains the best model weights and training metrics.

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/zaizou1003/knife-gun-detection.git
cd knife-gun-detection
```

### Install Dependencies
To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

### Clone the YOLOv5 Repository
Clone the official YOLOv5 repository from GitHub:

```bash
git clone https://github.com/ultralytics/yolov5.git
```

### Save the Weights Path
The best model weights (`best.pt`) are located in the `exp6/weights/` directory.

---

## How to Use

### Testing Camera Functionality
To test the camera functionality, run:

```bash
python test_camera.py
```

### Importing Datasets
Ensure your Roboflow API key is set as an environment variable before running:

```bash
python import.py
```

### Real-Time Detection
Run real-time detection using your webcam:

```bash
python webcam.py
```

### Image Detection
For object detection on an image, execute:

```bash
python pic_test.py
```
Provide an input image, and the script will return a labeled image with detected objects.

---

## Best Weights and Metrics

### Weights:
- **best.pt**: Best model weights
- **last.pt**: Latest model weights

### Metrics:
- Confusion Matrix
- Precision-Recall Curve
- Training and Validation Results

---

## Requirements
- Python 3.x
- YOLOv5 repository
- Required libraries listed in `requirements.txt`

---

## Contributing
Contributions are welcome! Feel free to fork this repository, create issues, or submit pull requests to improve the project.
