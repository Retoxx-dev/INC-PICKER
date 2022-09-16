FROM python:3.8-alpine

WORKDIR /app

COPY ./DevOps/Docker/TASK_PICKER/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app ./TASK_PICKER/main.py .

CMD ["python","-u","main.py"]