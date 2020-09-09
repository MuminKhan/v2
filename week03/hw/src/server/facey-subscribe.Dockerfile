FROM alpine:latest


RUN apk add --no-cache \
        python3 \
        py3-pip && \
    pip install --no-cache-dir \
        boto3 \
        paho-mqtt

WORKDIR /facey-subscribe
COPY facey_subscription.py facey_subscription.py

CMD ["python3", "-u", "facey_subscription.py"]
