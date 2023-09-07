
import wave

from pydub.playback import play

import io
import sys
import os
import json
import vosk

import gc

# import speech_recognition as sr
# r = sr.Recognizer()


import winsound
# f_name = 'decoder-test.wav'
# winsound.PlaySound(f_name, winsound.SND_FILENAME)


# path = '/Users/admin/PycharmProjects/pyLearning/thanks/venv/Lib/site-packages/vosk/vosk-model-ru-0.22'
# path = '/Users/admin/PycharmProjects/pyLearning/thanks/venv/Lib/site-packages/vosk/vosk-model-small-ru-0.22'
# path = '/Users/admin/PycharmProjects/pyLearning/thanks/venv/Lib/site-packages/vosk/vosk-model-ru-0.10'
# path = '/Users/admin/PycharmProjects/pyLearning/thanks/venv/model'
# path = '/Users/admin/PycharmProjects/pyLearning/thanks/venv/Lib/vosk-model-small-ru-0.22'
path = '/Users/admin/PycharmProjects/pyLearning/thanks/venv/model02'

model = vosk.Model(path)

if not model:
    print("Ошибка при создании модели")
print(type(model))

# Создаем объект VoskAPI()
# vosk_api = vosk.VoskAPI()
# print(type(vosk_api))

# Определяем путь к аудиофайлу
audio_path = 'output_txt.wav'
# audio_path = 'decoder-test.wav'
# audio_path = 'thanks.wav'
# audio_path = 'buratino_thanks.wav'
#
# wf = wave.open(audio_path, "rb")
# # wave_audio_file = wf
# # offline_recognizer = vosk.KaldiRecognizer(model, wave_audio_file.getframerate())
# data = wf.readframes(wf.getnframes())
# print(len(data))




# sample_rate = [20, 1000, 2000, 3000, 4000, 8000, 11025, 22050, 44100, 48000, 96000, 192000]
sample_rate = 44100
vad = False
# rec = vosk.KaldiRecognizer(model, sample_rate)
# rec.SetWords(True)
rec = vosk.KaldiRecognizer(model, sample_rate)
print("0")

with open(audio_path, "rb") as f:
    data = f.read()
    if len(data) > 0:
        if rec.AcceptWaveform(data):
            # rec.AcceptWaveform(data):
            result = rec.Result()
            print(result)
            # Получаем результаты распознавания в формате JSON
            result = json.loads(rec.FinalResult())
            # Выводим распознанный текст на экран
            print(result["text"])
        else:
            print(rec.PartialResult())
# print(rec.FinalResult())

rec.Reset()


if sys.version_info < (3, 6):
    print("Требуется Python версии 3.6 или выше")
else:
    # audio_data = b"test"
    if rec.AcceptWaveform(data):
        print("Распознавание прошло успешно")
        # Получаем результаты распознавания в формате JSON
        result = json.loads(rec.FinalResult())
        # Получаем распознанный текст
        # result = rec.FinalResult()
        # Выводим распознанный текст на экран
        print(result["text"])
        # print(result)
    else:
        print("Не удалось распознать аудио")



# rec.Reset()
# gc.collect()

# Получаем результаты распознавания в формате JSON
result = json.loads(rec.FinalResult())
# Получаем распознанный текст
results = rec.FinalResult()
print(type(results))
print(results)
# Выводим распознанный текст на экран
print(result[""
"text"
""])


first_result = result.get(0)
if first_result is not None:
    if "text" in first_result:
        text = first_result["text"]
        print(text)
    else:
        print("Ключ 'text' отсутствует в первом элементе списка.")
else:
    print("Список результатов распознавания пустой.")



rec.Reset()
#
gc.collect()




if __name__ == "__main__":
   #  play(audiopcm_n)
   pass