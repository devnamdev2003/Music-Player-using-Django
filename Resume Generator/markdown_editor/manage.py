import os
import openai

openai.api_key = os.getenv('OPENAI_KEY')

audio_file = open("song.mp3", "rb")
transcript = openai.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
)
print(transcript)

output_text_file_path = "transcript.txt"
with open(output_text_file_path, "w", encoding="utf-8") as text_file:
    text_file.write(transcript)
