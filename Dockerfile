FROM ubuntu:20.04
RUN apt update -y
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt --yes --force-yes install software-properties-common
RUN add-apt-repository ppa:jonathonf/ffmpeg-4
RUN apt update -y && install -y ffmpeg

WORKDIR /Shazam
COPY . .

RUN pip install -r requirements.txt
CMD [“python”, “./main.py”] 