import pygame
import threading

import webrtcvad
import collections
import sys
import signal
import pyaudio

from array import array
from struct import pack
import wave
import time

class recoder:
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        self.CHUNK_DURATION_MS = 30       # supports 10, 20 and 30 (ms)
        self.PADDING_DURATION_MS = 1500   # 1 sec jugement
        self.CHUNK_SIZE = int(self.RATE * self.CHUNK_DURATION_MS / 1000)  # chunk to read
        self.CHUNK_BYTES = self.CHUNK_SIZE * 2  # 16bit = 2 bytes, PCM
        self.NUM_PADDING_CHUNKS = int(self.PADDING_DURATION_MS / self.CHUNK_DURATION_MS)
        # NUM_WINDOW_CHUNKS = int(240 / CHUNK_DURATION_MS)
        self.NUM_WINDOW_CHUNKS = int(400 / self.CHUNK_DURATION_MS)  # 400 ms/ 30ms  ge
        self.NUM_WINDOW_CHUNKS_END = self.NUM_WINDOW_CHUNKS * 2

        self.START_OFFSET = int(self.NUM_WINDOW_CHUNKS * self.CHUNK_DURATION_MS * 0.5 * self.RATE)

        self.vad = webrtcvad.Vad(1)

        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=self.FORMAT,
                     channels=self.CHANNELS,
                     rate=self.RATE,
                     input=True,
                     start=False,
                     # input_device_index=2,
                     frames_per_buffer=self.CHUNK_SIZE)

        self.got_a_sentence = False
        self.leave = False


    def handle_int(self, sig, chunk):
        # global leave, got_a_sentence
        self.leave = True
        self.got_a_sentence = True


    def record_to_file(self, path, data, sample_width):
        "Records from the microphone and outputs the resulting data to 'path'"
        # sample_width, data = record()
        data = pack('<' + ('h' * len(data)), *data)
        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(self.RATE)
        wf.writeframes(data)
        wf.close()


    def normalize(self, snd_data):
        "Average the volume out"
        MAXIMUM = 32767  # 16384
        times = float(MAXIMUM) / max(abs(i) for i in snd_data)
        r = array('h')
        for i in snd_data:
            r.append(int(i * times))
        return r

    def start(self):
        print('start recoder')
        signal.signal(signal.SIGINT, self.handle_int)

        while not self.leave:
            ring_buffer = collections.deque(maxlen=self.NUM_PADDING_CHUNKS)
            triggered = False
            voiced_frames = []
            ring_buffer_flags = [0] * self.NUM_WINDOW_CHUNKS
            ring_buffer_index = 0

            ring_buffer_flags_end = [0] * self.NUM_WINDOW_CHUNKS_END
            ring_buffer_index_end = 0
            buffer_in = ''
            # WangS
            raw_data = array('h')
            index = 0
            start_point = 0
            StartTime = time.time()
            print("* recording: ")
            self.stream.start_stream()

            while not self.got_a_sentence and not self.leave:
                chunk = self.stream.read(self.CHUNK_SIZE)
                # add WangS
                raw_data.extend(array('h', chunk))
                index += self.CHUNK_SIZE
                TimeUse = time.time() - StartTime

                active = self.vad.is_speech(chunk, self.RATE)

                sys.stdout.write('1' if active else '_')
                ring_buffer_flags[ring_buffer_index] = 1 if active else 0
                ring_buffer_index += 1
                ring_buffer_index %= self.NUM_WINDOW_CHUNKS

                ring_buffer_flags_end[ring_buffer_index_end] = 1 if active else 0
                ring_buffer_index_end += 1
                ring_buffer_index_end %= self.NUM_WINDOW_CHUNKS_END

                # start point detection
                if not triggered:
                    ring_buffer.append(chunk)
                    num_voiced = sum(ring_buffer_flags)
                    if num_voiced > 0.9 * self.NUM_WINDOW_CHUNKS:
                        sys.stdout.write(' Open ')
                        # self.imlistening()
                        triggered = True
                        start_point = index - self.CHUNK_SIZE * 20  # start point
                        # voiced_frames.extend(ring_buffer)
                        ring_buffer.clear()
                # end point detection
                else:
                    # voiced_frames.append(chunk)
                    ring_buffer.append(chunk)
                    num_unvoiced = self.NUM_WINDOW_CHUNKS_END - sum(ring_buffer_flags_end)
                    if num_unvoiced > 0.9 * self.NUM_WINDOW_CHUNKS_END :
                            # or TimeUse > 100:
                        sys.stdout.write(' Close ')
                        self.imlistening()
                        triggered = False
                        self.got_a_sentence = True

                sys.stdout.flush()

            sys.stdout.write('\n')
            # data = b''.join(voiced_frames)

            self.stream.stop_stream()
            print("* done recording")
            self.got_a_sentence = False

            # write to file
            raw_data.reverse()
            for index in range(start_point):
                raw_data.pop()
            raw_data.reverse()
            raw_data = self.normalize(raw_data)
            self.record_to_file("./recoder/output.wav", raw_data, 2)
            self.leave = True

        self.stream.close()

    def start2(self):
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
        pygame.mixer.music.load('./sounds/1.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.delay(1)
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
if __name__ == '__main__':
    recoder = recoder()
    recoder.start()