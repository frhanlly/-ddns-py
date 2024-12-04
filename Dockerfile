FROM python:3.14.0a2-alpine3.19

WORKDIR /batchapp

COPY . .

RUN pip install -r /batchapp/requirements.txt

ENTRYPOINT ["python3"]
CMD ["/batchapp/main.py"]