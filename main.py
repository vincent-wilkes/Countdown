import time
import threading
from playsound import playsound

counting_time = input("Gebe die Länge des Countdowns in Sekunden an:")
counting_time = int(counting_time)

def play_audio():
    playsound('egg_clock.wav')

audio_thread = threading.Thread(target=play_audio)

time.sleep(counting_time-10)
print("Zehn Sekunden verbleibend.")
audio_thread.start()

time.sleep(7)
print("Drei Sekunden verbleibend.")

time.sleep(1)
print("Zwei Sekunden verbleibend.")

time.sleep(1)
print("Eine Sekunde verbleibend.") #

time.sleep(1)
print("Die Zeit ist vorbei!")
