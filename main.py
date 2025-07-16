import time
import threading
from playsound import playsound
from tkinter import *
from tkinter import ttk

def count():
    def countdown_thread():
        try:
            total_time = int(input_time.get())
            time_unit.set(str("seconds"))
        except ValueError:
            display_time.set("Invalid")
            return

        while total_time >= 0:
            display_time.set(str(total_time))
            time.sleep(1)
            total_time -= 1

            if total_time == 10:
                def play_audio():
                    playsound('egg_clock.wav')
                audio_thread = threading.Thread(target=play_audio).start()

        else:
            display_time.set(str("Time is over!"))
            time_unit.set(str(""))

    threading.Thread(target=countdown_thread).start()

root = Tk()
root.title("Countdown")

mainframe = ttk.Frame(root, padding=" 3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, E, W, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

input_time = StringVar()
display_time = StringVar()
time_unit = StringVar()

counting_time_entry = ttk.Entry(mainframe, width=7, textvariable=input_time)
counting_time_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=display_time).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Count", command=count).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="seconds").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, textvariable=time_unit).grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
counting_time_entry.focus()

def on_return(event):
    count()
root.bind("<Return>", on_return)

root.mainloop()
