FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install reflex==0.6.3 requests



CMD reflex run --env prod --backend-only