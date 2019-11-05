FROM ubuntu
RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    python-pip \
    python-virtualenv \
    git \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/nl2412/aci2019.git
WORKDIR /aci2019/src/deploy
RUN pip install -U setuptools
RUN pip install --upgrade pip
RUN pip install kubernetes
RUN chmod +x rpi-deploy.py
CMD ["python","./rpi-deploy.py"]