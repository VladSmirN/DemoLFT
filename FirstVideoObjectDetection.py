from imageai.Detection.Custom import CustomVideoObjectDetection
import os

execution_path = os.getcwd()

video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath("cabile/models/detection_model-ex-018--loss-0014.381.h5")
video_detector.setJsonPath("cabile/json/detection_config.json")
video_detector.loadModel()

video_detector.detectObjectsFromVideo(input_file_path="AVI/1.avi",
                                          output_file_path=os.path.join(execution_path, "cabile_detected"),
                                          frames_per_second=20,
                                          minimum_percentage_probability=40,
                                          log_progress=True)

