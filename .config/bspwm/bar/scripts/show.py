import tkinter as tk
import os
from PIL import Image, ImageTk

is_playing = False

root = tk.Tk()
root.configure(bg='#24283b')

frame = tk.Frame(root, bg='#24283b')
frame.pack()

def resize_image(image_path, base_width):
    image = Image.open(image_path)
    w_percent = (base_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    return image.resize((base_width, h_size), Image.LANCZOS)

def toggle_music():
    global is_playing
    # Obtén el estado actual de la música
    status = os.popen('playerctl status').read().strip()
    if status == 'Playing':
        os.system('playerctl pause')
        music_button.config(image=play_icon, text="STOP")
        is_playing = False
    elif status == 'Paused':
        os.system('playerctl play')
        music_button.config(image=stop_icon, text="PLAY")
        is_playing = True

def next_song():
    os.system('playerctl next')

def previous_song():
    os.system('playerctl previous')

stop_image = resize_image(os.path.expanduser('~/.config/bspwm/assets/icons/system/stop.png'), 80)
stop_icon = ImageTk.PhotoImage(stop_image)

play_image = resize_image(os.path.expanduser('~/.config/bspwm/assets/icons/system/play.png'), 80)
play_icon = ImageTk.PhotoImage(play_image)

next_image = resize_image(os.path.expanduser('~/.config/bspwm/assets/icons/system/next.png'), 80)
next_icon = ImageTk.PhotoImage(next_image)

previous_image = resize_image(os.path.expanduser('~/.config/bspwm/assets/icons/system/previous.png'), 80)
previous_icon = ImageTk.PhotoImage(previous_image)

generic_image = resize_image(os.path.expanduser('~/.config/bspwm/assets/icons/system/generic.png'), 150)
generic_icon = ImageTk.PhotoImage(generic_image)

generic_button = tk.Button(frame,
                   image=generic_icon,
                   text="GENERIC", 
                   fg="#c0caf5",
                   bg="#24283b",
                   height=150,  
                   width=150,
                   borderwidth=0,
                   highlightbackground="#24283b",
                   state=tk.DISABLED)
#generic_button.place(x=800,y=800)
generic_button.pack(side=tk.TOP)

previous_button = tk.Button(frame,
                   image=previous_icon,
                   text="PREVIOUS", 
                   fg="#c0caf5",
                   bg="#24283b",
                   activebackground="#cba6f7",
                   height=80,  
                   width=80,
                   borderwidth=0,
                   highlightbackground="#24283b",
                   command=previous_song)
#previous_button.place(x=150, y=400)
previous_button.pack(side=tk.LEFT)

music_button = tk.Button(frame,
                   image=play_icon,
                   text="PLAY", 
                   fg="#c0caf5",
                   bg="#24283b",
                   activebackground="#cba6f7",
                   height=80,  
                   width=80, 
                   borderwidth=0,
                   highlightbackground="#24283b",
                   command=toggle_music)
#music_button.place(x=150, y=400)
music_button.pack(side=tk.LEFT)

next_button = tk.Button(frame,
                   image=next_icon,
                   text="NEXT", 
                   fg="#c0caf5",
                   bg="#24283b",
                   activebackground="#cba6f7",
                   height=80,  
                   width=80,
                   borderwidth=0,
                   highlightbackground="#24283b",
                   command=next_song)
#next_button.place(x=150, y=400)
next_button.pack(side=tk.LEFT)

root.mainloop()
