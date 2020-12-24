import subprocess

def toWav():
    src_filename = 'audio.oga'
    dest_filename = 'audio.wav'

    process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename])
    if process.returncode != 0:
        raise Exception("Something went wrong")
    else:
        print("[ Conversion Done ]")
