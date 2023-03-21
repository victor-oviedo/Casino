FROM python:3.10

WORKDIR /blackjack
COPY  requirements.txt /blackjack/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /blackjack/requirements.txt

COPY . /blackjack

CMD bash -c "while true; do sleep 1; done"