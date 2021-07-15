# сборка образа - docker build --tag=fastapi-server .
# запуск контейнера - docker run -d --name my-fastapi -p 8000:8000 fastapi-server

FROM python:3.9-buster

COPY . .

RUN pip install -r requirements.txt

WORKDIR .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0"]