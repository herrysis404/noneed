FROM ubuntu:groovy
RUN mkdir ./app
#RUN chmod 777 ./app
WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Singapore

RUN apt-get update --fix-missing && apt-get -qq install -y git wget curl aria2 busybox unzip unrar tar python3 ffmpeg python3-pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt --upgrade youtube-dl
COPY . .
CMD ["bash","start.sh"]
