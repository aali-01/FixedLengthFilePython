FROM python:3.9-bullseye

WORKDIR /app
COPY app ..

VOLUME [ "/app","/app" ]
EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["ReadDataFromJSON.py"]