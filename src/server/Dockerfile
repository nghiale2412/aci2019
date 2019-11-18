FROM alpine:latest
RUN apk add --no-cache alpine-sdk \
	    alsa-lib \
	    alsa-utils \
            python3 \
	    python3-dev \
	    py3-pip \
	    portaudio-dev
COPY ["requirements.txt", "scripts/__init__.py", "scripts/server.py", "./"]
RUN pip3 install -r /requirements.txt
RUN chmod +x server.py
CMD ["python3","./server.py"]
