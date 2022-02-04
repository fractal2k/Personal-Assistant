FROM rasa/rasa

COPY ./src /app

CMD ["run", "--enable-api"]