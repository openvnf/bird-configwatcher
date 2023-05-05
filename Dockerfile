FROM python:alpine3.17
RUN addgroup --system app && adduser -S app -G app
COPY --chown=app:app . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python -u ./bird-configwatcher.py
