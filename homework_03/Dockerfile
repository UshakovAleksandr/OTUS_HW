# сборка образа - docker build --tag=fastapi-server .
# запуск контейнера - docker run -d --name my-fastapi -p 8000:8000 fastapi-server

# образ питона
FROM python:3.9-buster

#тущая директория внутри образа
WORKDIR /app

#копируем в образ зависимости
COPY requirements.txt /app/requirements.txt

# и устанавливаем их
RUN pip install -r requirements.txt

# откуда (текущий директория) и куда копируется(директория в образе)
COPY . /app

# напоминался для себя, какой порт будет торчать из докера
EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0"]