FROM python:3

ADD parolo.py .

RUN pip install colorama

CMD ["python3", "./main.py"]