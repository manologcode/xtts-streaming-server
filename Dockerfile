FROM python:3.9

WORKDIR /app

COPY ./test/requirements.txt /app/test/requirements.txt
RUN python -m pip install -r /app/test/requirements.txt
#COPY ./xtts-streaming-server/* /app/
# CMD ["python", "demo.py"]
