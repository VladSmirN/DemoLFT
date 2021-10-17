from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("cabile/models/detection_model-ex-018--loss-0014.381.h5")
detector.setJsonPath("cabile/json/detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="frame1.jpg", output_image_path="frame1-detected.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

