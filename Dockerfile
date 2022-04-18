FROM python:3.8

ENV SRC_DIR /usr/bin/src/webapp/src

COPY src/* ${SRC_DIR}/

WORKDIR ${SRC_DIR}

ENV PYTHONUNBUFFERED=1

ENV ADDRESS='0.0.0.0'

CMD ["python", "python_server.py"]

