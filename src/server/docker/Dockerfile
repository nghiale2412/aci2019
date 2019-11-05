FROM ubuntu:16.04
RUN apt-get update
RUN apt-get -y install git
RUN apt-get install -y python3 python3-pip wget
RUN apt-get install -y libjack-jackd2-dev portaudio19-dev
RUN pip3 install pyaudio
RUN pip3 install asyncio
RUN git clone https://github.com/nl2412/aci2019.git
WORKDIR /aci2019/src/server
RUN chmod +x server.py
CMD ["python3","./server.py"]