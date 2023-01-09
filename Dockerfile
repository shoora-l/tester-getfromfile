FROM python:alpine3.17
WORKDIR /usr/local/
COPY .  .
RUN pip install -r pipreqs
CMD ["python3", "main.py"]
EXPOSE 8080/tcp