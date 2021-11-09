import pyaudio
import wave
import speech_recognition as sr
import subprocess
from command import Commander


r = sr.Recognizer()
cmd = Commander()
running = True


def say(text):
    filename = "command.txt"
    filepath = "./" + filename
    with open("command.txt", 'w+') as f:
        f.write(text)
        f.close()

    subprocess.call('cscript "C:\Program Files\Jampal\ptts.vbs" < ' + filepath, shell=True)


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


def init_speech():
    global running

    print("Listening")
    play_audio('./media/ahem_x.wav')

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    play_audio("./media/ahem_x.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand.")

    if command in ["quit", "exit", "bye", "goodbye"]:
        running = False
    else:
        cmd.discover("Your command: %s" % command)


if __name__ == "__main__":

    while running:
        init_speech()

