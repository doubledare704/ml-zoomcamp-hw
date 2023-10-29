FROM python:3.10.12-slim

WORKDIR /app
COPY ["*.bin", "./"]

RUN pip install -U pip

COPY ["requirements.txt", "./"]

RUN pip install -r requirements.txt

COPY ["predict.py", "./"]

EXPOSE 8000

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:8000", "predict:app"]