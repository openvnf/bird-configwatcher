FROM python:3.8-alpine
RUN addgroup -S app && adduser -S app -G app
COPY --chown=app:app . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python ./bird-configwatcher.py
