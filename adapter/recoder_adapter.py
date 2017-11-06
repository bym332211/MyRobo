import pyaudio
import wave
import numpy as np
import pygame
import time
import threading

class recoder:
    def start(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        RECORD_SECONDS = 6
        WAVE_OUTPUT_FILENAME = "./recoder/output.wav"
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        self.imlistening()
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
        self.imlistening()

    def imlistening(self):
        # pass
        t = threading.Thread(target=self.playListening)
        t.start()

    def playListening(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./sounds/imlistening.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.delay(1)
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
if __name__ == '__main__':
    recoder = recoder()
    recoder.start()