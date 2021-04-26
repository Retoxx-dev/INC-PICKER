FROM python:3.9

WORKDIR /app

COPY --chown=app:app app.py .

RUN pip install requests && pip install pymsteams

CMD ["python","-u","app.py"]