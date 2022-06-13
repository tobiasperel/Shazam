import sounddevice as sd

print(sd.query_devices())
print(sd.default.device)
print(sd.query_devices()[5])

#sd.default.device[0] = 4 # 0 o 1 escucho mi microfono
#sd.default.device[1] = 62

fs = 44100 # Hz
length = 5 # s
print("start recording")
recording = sd.rec(frames=fs * length, samplerate=fs, blocking=False, channels=2)
sd.wait()
print("stop recording")
from scipy.io import wavfile
wavfile.write('audio.wav', fs, recording)