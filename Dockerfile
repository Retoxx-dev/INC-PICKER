FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app app.py .

CMD ["python","-u","app.py"]