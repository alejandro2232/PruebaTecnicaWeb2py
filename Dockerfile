FROM python:3.12.1-alpine3.18

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --upgrade pip && \
    pip install psycopg2-binary

RUN pip install -r requirements.txt
					
COPY ./ ./

CMD ["python", "web2py.py", "-a", "1234", "-i", "0.0.0.0", "-p", "8000"]

