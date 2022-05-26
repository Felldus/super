from tkinter import *
from tkinter import messagebox
from pygame import *
from PIL import Image, ImageTk

w =Tk()

mixer.init()

img_gif = PhotoImage(file = 'D:\Exeeeeeeeee\ggg.gif')
label_img = Label(w, image = img_gif,width = 720 , height = 1080,)
label_img.pack()


img_back = ('mos.jpg')
pabol = mixer.Sound('bara.mp3')
aauh = mixer.Sound('auh.ogg')


w.title("el primo")

w.geometry("600x360")
m = Label(w,text = 'введи "номер маминой карты":', font = ('segeo script', 15))
m.place(x = 50, y = 80)
i = Label(w,text = 'ХОтите 10000000000000000000 ГЕмав из бравл старс:', font = ('segeo script', 15))
i.place(x = 50, y = 50)

w_i = Entry(w)
w_i.place(x = 50, y =150, width = 150, height = 30)

def print_text():
    answer = w_i.get()
    if answer == 'номер маминой карты':
        pabol.play()
        messagebox.showinfo(title = "хахахха", message = "Тебя абманули мащеники")
    else:
        aauh.play()
        messagebox.showerror(title = "AAAAAAAUAUAGHGHGH", message = "AAAAAAAUAUAGH")
bd = Button(w, text = "жми", command = print_text)
bd.place(x = 50, y = 190, width =150 ,height = 50)

w.mainloop()