FROM arm32v7/ubuntu:16.04
COPY qemu-arm-static /usr/bin/qemu-arm-static
RUN apt-get update
RUN apt-get -y install git
RUN apt-get install -y alsa-base alsa-utils
RUN apt-get install -y python3 python3-pip wget
RUN apt-get install -y libjack-jackd2-dev portaudio19-dev
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
RUN git clone https://github.com/nl2412/aci2019.git
WORKDIR /aci2019/src/server
RUN chmod +x server.py
CMD ["python3","./server.py"]
