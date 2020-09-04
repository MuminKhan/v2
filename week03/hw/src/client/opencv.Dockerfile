FROM nvcr.io/nvidia/l4t-ml:r32.4.3-py3

RUN apt update && \
    apt install -y \
            libffi-dev \
            python3-pip \
            python3-tk \ 
            libopencv-dev \
            python3-opencv \
            python3-numpy

#RUN apt install -y python3-scipy python3-matplotlib python3-numpy

COPY recognize_faces.py recognize_faces.py
COPY haarcascade_frontalface_default.xml haarcascade_frontalface_default.xml

CMD ["python3", "-u", "recognize_faces.py"]
