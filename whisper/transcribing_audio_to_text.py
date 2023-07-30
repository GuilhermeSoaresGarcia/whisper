import whisper
from datetime import datetime
import torch

torch.backends.cuda.cufft_plan_cache.max_split_size_mb = 4

now = str(datetime.now()).replace(":", "")

try:
    # Aqui é possível selecionar o model (tiny, small, medium, large, large-v2) e se 
    # o processamento será feito em GPU ou CPU. O model large (ou mesmo o medium) requer
    # muita VRAM em caso de uso via GPU, mas a velocidade de processamento é muito maior.
    # Infelizmente, não consegui usar esses models maiores na minha GPU pois ela possui
    # apenas 4GB de VRAM (a documentação sugere pelo menos 10GB para essas models.)

    model = whisper.load_model("large-v2", device="gpu")
    result = model.transcribe(
        "audio_to_transcribe/teste_curto.mp3",
        language="pt",
        fp16=False,
        verbose=True,
        patience=2,
        beam_size=5,
    )

    segments = result["segments"]

    with open(f"audio_to_transcribe/{now}.txt", "w") as f:
        for segment in segments:
            start_time = segment["start"]
            end_time = segment["end"]
            text = segment["text"]
            f.write(f"[{start_time} - {end_time}]: {text}\n")

except Exception as error:
    print(error)
