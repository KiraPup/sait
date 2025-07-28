from tkinter import *
from PIL import Image, ImageTk #работа с картинками
import requests
from io import BytesIO #работа с двоичной системой


window = Tk()
window.title('Cats!')
window.geometry('600x480')

#создаем местку. где будет изображение
label=Label()
label.pack()

#адрес из интернета, из которого берем информацию
url = "https://cataas.com/cat"
img = load_image(url) #сделать загрузку изображения

#проверка если не пустая переменная,
if img:
    label.config(image=img)
    label.image = img #если эту строчку не написать, то комп ее выдаст, а так какмусор удалтит

window.mainloop()