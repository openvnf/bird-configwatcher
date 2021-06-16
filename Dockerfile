FROM quay.io/bitnami/python:3.9-prod
RUN addgroup --system app && adduser --system --group app
COPY --chown=app:app . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python -u ./bird-configwatcher.py
