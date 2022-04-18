FROM python:3.8

ENV SRC_DIR /usr/bin/src/webapp/src

COPY src/* ${SRC_DIR}/

WORKDIR ${SRC_DIR}

ENV PYTHONUNBUFFERED=1

ENV ADDRESS=https://qr-python-server.herokuapp.com
ENV PORT=8000
EXPOSE 8000

CMD ["python", "python_server.py"]

