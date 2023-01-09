FROM python:alpine3.17
COPY pipreqs  .
RUN pip install -r pipreqs
COPY main.py .
CMD ["python3", "main.py"]
EXPOSE 8080/tcp