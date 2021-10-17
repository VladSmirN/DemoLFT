Для запуска нужно установить это:

```
pip install opencv-python
pip install imageai
pip install tensorflow-gpu
```

Обработка просходит на процессоре можно попробывать установить CUDA для работы на видео:
```
https://www.machinelearningmastery.ru/installing-tensorflow-with-cuda-cudnn-and-gpu-support-on-windows-10-60693e46e781/
```

``` FirstCustomDetection ``` - Анализ фото.   
Рядом с файлом размещаяем ```frame1.jpg``` для анализа.


``` FirstVideoObjectDetection ``` - Анализ видео.   
Файл для анализа сохраняем в папку ```AVI``` название ```1.avi```.   
После обработки будет создан файл ```cabile_detected.avi```

Описание процесов, там же есть описание для потокового видео:
```
https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/Custom/CUSTOMVIDEODETECTION.md
```

Файлы датасетов:
