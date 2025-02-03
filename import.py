import os
from roboflow import Roboflow
rf = Roboflow(api_key=os.getenv("ROBOFLOW_API_KEY"))
project = rf.workspace("crime-detection-zbmr9").project("gun-knife-thesis")
version = project.version(11)
dataset = version.download("yolov5")