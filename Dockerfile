FROM alpine:latest
RUN apt update 
RUN apt install python3
RUN apt install python3-pip
RUN pip install -r pipreqs
CMD ["python3", "main.py"]
EXPOSE 8080/tcp