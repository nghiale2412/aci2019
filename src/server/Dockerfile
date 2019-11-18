FROM ubuntu:latest
RUN apt-get update && \
    apt-get -y install alsa-base \
	       	       alsa-utils \
                       python3 \
	               python3-pip \
                       libjack-jackd2-dev \
	               portaudio19-dev
COPY requirements.txt /
COPY server.py /
RUN pip3 install -r /requirements.txt
RUN chmod +x /server.py
CMD ["python3","./server.py"]
