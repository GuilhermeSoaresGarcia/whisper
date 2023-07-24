FROM python:bookworm

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

RUN apt --yes update && apt --yes --force-yes install ffmpeg
