FROM python:3.8
RUN mkdir /app 
COPY . /app
COPY pyproject.toml /app
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
ENTRYPOINT ["python"]
CMD ["intents_producer/etl.py"]
cmd ["chat_bot/train.py"]
CMD ["server/server.py"]