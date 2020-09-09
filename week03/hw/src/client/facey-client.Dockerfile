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

CMD ["python3", "-u", "facey_client.py"]
