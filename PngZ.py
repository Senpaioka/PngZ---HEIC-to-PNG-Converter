import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from heic2png import HEIC2PNG 

# file drop functionality

full_text = ""

def on_drop(event):
    global full_text
    text = ''
    files = event.data
    for file in files:
        text += file
    full_text = text


    if callback_func is not None:
        callback_func(full_text)
 

# common config

window = TkinterDnD.Tk()
window.title("PngZ - HEIC to Png Image Converter")

canvas = tk.Canvas(window, width=700, height=400, bg="#181818")
canvas.pack()

canvas.create_text(350, 200, text="Drag & Drop Your .HEIC File Here", font=("Arial", 20), fill="grey", anchor="center")

canvas.drop_target_register(DND_FILES)
canvas.dnd_bind('<<Drop>>', on_drop)


# converter functionality

def image_process(link):
        if __name__ == '__main__':
            heic_img = HEIC2PNG(link)
            heic_img.save() 

def handle_updated_full_text(text):
    str_text = str(text)
    result_string = str_text.replace("{", "").replace("}", "")
    image_process(result_string)
     

callback_func = handle_updated_full_text

window.mainloop()
