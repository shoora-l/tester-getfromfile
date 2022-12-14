FROM ubuntu:latest
RUN apt update 
RUN apt -y install python3
RUN apt -y install python3-pip
RUN pip install -r pipreqs
CMD ["python3", "main.py"]
EXPOSE 8080/tcp