#Dockerfile, Image, Container
#python -m venv venv
#venv/Scripts/activate

FROM python:3.9.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
CMD ["python", "./main.py"]

#to build
#docker build -t python-imdb .
#to run
#docker run -p 8080:8080 python-imdb ('-t' is sudo terminal, '-i' is interactive mode, '-p' is to map port)