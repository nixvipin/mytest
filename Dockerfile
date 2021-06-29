FROM python:2.7-aphine
RUN apk update && pip install bottle \
    && mkdir /app
WORKDIR /app
COPY . .
EXPOSE 22
CMD ["python","-u","myprogram.py"]
