import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()
i = 0 

def get_description(video):
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

    print(f"Uploading file...")
    video_file = client.files.upload(file=video)

    while video_file.state.name == "PROCESSING":
        time.sleep(1)
        video_file = client.files.get(name=video_file.name)
        print(f"seconds: {i}, status: {video_file.state.name}")
        i += 1

    if video_file.state.name == "FAILED":
        raise ValueError(video_file.state.name)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            video_file,
            "напиши два предложения на английском языке который вкратце описывают что происходит на видео, добавь 5 тегов в конце, сделай это одним предложением"])

    return reponse.text

