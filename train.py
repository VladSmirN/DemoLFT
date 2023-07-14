from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()

trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="cabile/")

trainer.setTrainConfig(object_names_array=["cabile"],  train_from_pretrained_model="yolov3.pt")

trainer.trainModel()