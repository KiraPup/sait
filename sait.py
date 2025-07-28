from tkinter import *
from PIL import Image, ImageTk #работа с картинками
import requests
from io import BytesIO #работа с двоичной системой

#создаем функцию
def load_imidge():
    try:
        response = requests.get(url) #запрос и то что вернется положим в респонс
        response.raise_for_status() #обработка исключений
        image_data = BytesIO(response.content)#положим обработанное изображение
        img = Image.open(image_data) #открываем
        return ImageTk.PhotoImage(img) #это имг положим в нижний имг
    except Exception as e:
        print (f'ПРоизошла ошибка {e}')
        return None #если функуция ничего не вернет



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