import time

counting_time = input("Gebe die Länge des Countdowns in Sekunden an:")
counting_time = int(counting_time)

time.sleep(counting_time-10)
print("Zehn Sekunden verbleibend.")

time.sleep(7)
print("Drei Sekunden verbleibend.")

time.sleep(1)
print("Zwei Sekunden verbleibend.")

time.sleep(1)
print("Eine Sekunde verbleibend.") #

time.sleep(1)
print("Die Zeit ist vorbei!")
