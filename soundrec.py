import os
import sounddevice as sd
import wavio

duration = int(input("Enter duration of recording in seconds :"))
fs = 50000  
name=input("Enter name for file:")
folder_name = "recordings"
filename = os.path.join(folder_name, f"{name}.wav")

if not os.path.exists(folder_name):
    os.makedirs(folder_name)


print("Recording...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()
print("Recording finished....")


wavio.write(filename, recording, fs, sampwidth=2)
print(f"Audio saved as {filename}")


