import subprocess

def toWav(filename):
    src_filename = 'audio_files/audio.oga'
    print(filename.split(".")[0]+".wav")
    dest_filename = "audio_files/"+filename.split(".")[0]+".wav"

    process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename])
    if process.returncode != 0:
        raise Exception("Something went wrong")
    else:
        print("[ Conversion Done ]")
