FROM nvcr.io/nvidia/l4t-ml:r32.4.3-py3

RUN apt update && \
    apt install -y \
            libffi-dev \
            python3-pip \
            python3-tk \ 
            libopencv-dev \
            python3-opencv \
            python3-numpy 
RUN pip3 install --no-cache-dir paho-mqtt

WORKDIR /facey
COPY facey_client.py facey_client.py
COPY haarcascade_frontalface_default.xml haarcascade_frontalface_default.xml

ENV MQTT_SERVER="mqtt"
ENV MQTT_PORT=1883
ENV MQTT_TOPIC="facey"
ENV MQTT_QOS=0

CMD ["sh", "-c", \
    "python3 -u facey_client.py -s $MQTT_SERVER -p $MQTT_PORT -t $MQTT_TOPIC -q $MQTT_QOS"]
