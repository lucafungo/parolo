FROM python:3

ADD parolo.py .
ADD stored_words.json .
ADD intro.txt .

RUN pip install colorama

CMD ["python3", "./parolo.py"]