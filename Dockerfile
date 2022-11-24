FROM ubuntu:alpine
RUN apt update 
RUN cat sysreqs | xargs -d '\n' apt install -y
RUN pip install -r pipreqs
CMD ["python3", "main.py"]