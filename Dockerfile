FROM python:3.6

WORKDIR /serv

COPY requirements.txt .

RUN pip install -r requirements.txt 

RUN python -m nltk.downloader stopwords

COPY . .

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
