import subprocess
import os 

def make_unique(video, new_name):
    new_name = new_name.replace("\n", "")
#   subprocess.run(["ffmpeg", "-i",video,"-acodec","copy","-vcodec","copy","-vbsf","h264mp4toannexb","-f","mpegts","./video.ts"])   
    subprocess.run(["ffmpeg", "-i",video,"-s","1280x720","-b:v","6.5M","-vf","eq=brightness=0.02:contrast=0.8",f"{new_name}.mp4"])
    os.replace(f"{new_name}.mp4", f"./result/{new_name}.mp4")
    


