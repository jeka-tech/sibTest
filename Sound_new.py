

import pyaudio
import wave

# задаем параметры записи
FORMAT = pyaudio.paInt16
CHANNELS = 1
# RATE = 44100  11025
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10

# создаем объект pyaudio для записи звука
p = pyaudio.PyAudio()

# открываем поток для записи звука с микрофона
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# создаем список для хранения фреймов звука
frames = []
# zz = int(RATE / CHUNK * RECORD_SECONDS)
# print(zz)

print("Говорите речь или комнады")
# записываем звук в список фреймов
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    if i == (int(RATE / CHUNK * RECORD_SECONDS)) - 70:
        print("Завершите речь")

# останавливаем запись звука и закрываем поток
stream.stop_stream()
stream.close()
p.terminate()

# сохраняем список фреймов в файл wav
wf = wave.open("output_txt.wav", "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()



if __name__ == "__main__":
   #  play(audiopcm_n)
   pass