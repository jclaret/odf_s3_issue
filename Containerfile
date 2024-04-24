FROM ubuntu:18.04

RUN apt-get update && apt-get install -y s3fs python3

COPY file.py /file.py
CMD ["python3", "./file.py"]
