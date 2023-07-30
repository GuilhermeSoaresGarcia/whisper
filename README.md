## Como usar

Criei um Dockerfile que utiliza uma imagem da Nvidia com suporte a CUDA, a fim de poder utilizar o processamento via GPU. Porém, essa imagem não vem com Python ou ffmpeg, então no Dockerfile tudo isso será instalado. Para rodar o container com essas instalações automatizadas:

```bash
# O container ficará com o nome de "whisper"
docker build -t whisper .
```

Após a o download da imagem e instalação das aplicações, poderemos acessar o terminal do container com o seguinte comando:

```bash
# O parâmetro "--gpus" é para selecionar todas as GPUS Nvidia presentes no sistema. O parâmetro "-v" mapeia o diretório local onde o whisper está localizado, separado por ":" no diretório do container 
docker run --gpus all -it -v /home/user/whisper/:/usr/src/app/whisper/ whisper bash
```

Já dentro do bash do container, navegando até o diretório **"/usr/src/app/whisper/"**, podemos executar o script **"transcribing_audio_to_text.py"** para transcrever o áudio de acordo com os parâmetros desejados:
```bash
python transcribing_audio_to_text.py
```
O whisper pode ser utilizado diretamente via linha de comando, mas com script é bem mais personalizável. O áudio transcrito será salvo no diretório **"audio_to_transcribe"** em um txt com nome gerado pelo datetime.
