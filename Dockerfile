FROM nvidia/cuda:11.6.2-devel-ubuntu20.04

# export timezone - for python installation
ENV TZ=America/Sao_Paulo

# place timezone data /etc/timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app/

COPY requirements.txt ./

RUN apt --yes update && apt --yes --force-yes install ffmpeg && apt --yes --force-yes install python3 pip && apt --yes --force-yes install git

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

RUN pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

RUN apt --yes update && apt --yes --force-yes install ffmpeg
