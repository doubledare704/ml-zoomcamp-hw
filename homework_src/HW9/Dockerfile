FROM agrigorev/zoomcamp-bees-wasps:v2

RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
RUN pip install pillow
COPY homework.py .
ENV MODEL_NAME=bees-wasps-v2.tflite

CMD [ "homework.lambda_handler" ]

#agrigorev/zoomcamp-bees-wasps   v2                   b9f6c13de368   7 days ago       662MB
