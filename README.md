Для запуска через докер нужно запустить команды:

```
sudo docker image pull vladsmirn/cabile:v1
sudo docker run --rm -it  --name cabile -v ./your_data_folder:/app/data/ -v ./your_predict_folder:/app/predicts vladsmirn/cabile:v1
```
Где your_data_folder - папка с данными для предсказаний. По умолчанию в /app/data/ лежат файлы из https://github.com/VladSmirN/DemoLFT/tree/master/data . 
Если не требуется добавлять новые файлы для предсказания, то volume можно проигнорировать (команды ниже).
``` 
sudo docker image pull vladsmirn/cabile:v1
sudo docker run --rm -it  --name cabile  -v ./your_predict_folder:/app/predicts vladsmirn/cabile:v1
```
your_predict_folder - папка, куда будут сохраняться результаты. По умолчанию в /app/predicts лежат файлы из https://github.com/VladSmirN/DemoLFT/tree/master/predicts . 

После запуска контейнера в нем нужно ввести 
``` 
yolo predict model=models/best.pt save=True source=./data/your_file_for_predict project=./predicts
```
Где your_file_for_predict файл из папки your_data_folder, на котором будет работать алгоритм распознавания. Результат будет сохраняться в your_predict_folder. 


