FROM python:3.8-alpine

WORKDIR /app

COPY ./DevOps/Docker/INC_PICKER/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app ./INC_PICKER/main.py .

CMD ["python","-u","main.py"]