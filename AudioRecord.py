import pyaudio
import wave
import keyboard

def record_audio(output_filename, record_seconds=3600):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Start to speak, press enter to stop.")

    frames = []

    try:
        while not keyboard.is_pressed("enter"):
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        pass



    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()



if __name__ == "__main__":
    record_audio("AUDIOCHAT/AudioChatTest.wav")
