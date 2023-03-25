FROM python:3.10

WORKDIR /casino
COPY  requirements.txt /casino/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /casino/requirements.txt

COPY . /casino

CMD bash -c "while true; do sleep 1; done"