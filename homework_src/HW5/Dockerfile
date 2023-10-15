FROM python:3.10.12-slim
WORKDIR /app
COPY ["model1.bin", "dv.bin", "./"]

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["question6.py", "./"]

EXPOSE 8000

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:8000", "question6:app"]

#docker images
#REPOSITORY              TAG                  IMAGE ID       CREATED          SIZE
#<none>                  <none>               d0ba891403b3   19 minutes ago   147MB