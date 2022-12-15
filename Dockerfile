FROM ubuntu:latest
RUN apt update 
RUN apt -y install python3
RUN apt -y install python3-pip
COPY pipreqs  .
RUN pip install -r pipreqs
COPY main.py .
CMD ["python3", "main.py"]
EXPOSE 8080/tcp