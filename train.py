from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()

trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="cabile/")

trainer.setTrainConfig(object_names_array=["cabile"], num_experiments=300, batch_size=16,  train_from_pretrained_model="yolov3.pt")

trainer.trainModel()