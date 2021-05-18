import speech_recognition as sr
import pyaudio
import wave
import os

""" 使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站。
    参考思路：
    1：获取电脑录音-->WAV文件 python record wav
    2：录音文件-->文本
    STT: Speech to Text
    STT API Google API
    3:文本-->电脑命令
"""

def record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return WAVE_OUTPUT_FILENAME

def voice2text(audiofile):
    r = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = r.record(source)
    try:
        #content = r.recognize_google(audio, language='zh-CN')
        content = r.recognize_google(audio)
        print("Google Speech Recognition:" + content)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Google Speech Recognition error; {0}".format(e))
    return content

def main():
    s = input("你是要开始录音么yes or no ：")
    if s.lower() == "yes":
        audiofile = record()
        content = voice2text(audiofile)
        if "youtube" in content.lower():
            os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" https://www.youtube.com/')
        elif "amazon" in content.lower():
            os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" https://www.amazon.com/')
        else:
            os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" https://www.google.com/search?q={}'.format(content.lower().replace(" ","")))
    else:
        print("test.")

if __name__ == '__main__':
    main()
