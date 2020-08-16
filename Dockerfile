FROM python:3.8
RUN mkdir /app 
COPY . /app
COPY pyproject.toml /app
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN python intents_producer/etl.py
RUN python chat_bot/train.py
ENTRYPOINT ["python"]
CMD ["server/server.py"]