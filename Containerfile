FROM fedora:38

RUN dnf install s3fs-fuse -y

COPY file.py /file.py
CMD ["python3", "./file.py"]
