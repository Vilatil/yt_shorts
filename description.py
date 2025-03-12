import os
import time
from google import genai
from dotenv import load_dotenv


def get_description(video):
    load_dotenv()
    prompt = """
Generate only: 
1. Up to ten words describing this video (no introduction)
2. 5 tags for this video 
Format must be exact: [description] #tag1 #tag2 #tag3 #tag4 #tag5
Do not include any additional text or explanations.
"""
    special_characters=[':','.',',','*', '\\', "'"]
    i=0
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
    print(f"my path is {video}")
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
        contents=[video_file, prompt]
        )
    response = response.text
    for i in special_characters:
        response=response.replace(i, "")
    return response

