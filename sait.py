from tkinter import *
from PIL import Image, ImageTk #работа с картинками
import requests
from io import BytesIO #работа с двоичной системой




#создаем функцию
def load_image(url):
    try:
        response = requests.get(url) #запрос и то что вернется положим в респонс
        response.raise_for_status() #обработка исключений
        image_data = BytesIO(response.content)#положим обработанное изображение
        img = Image.open(image_data) #открываем
        #подгоняем под размер окна изображение
        img.thumbnail(600,480, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img) #это имг положим в нижний имг
    except Exception as e:
        print (f'ПРоизошла ошибка {e}')
        return None #если функуция ничего не вернет


#Функция будет делать проверку и установку каждый раз в новом окне
def open_new_window():
    tag = tag_entry.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"
    img = load_image(url_tag)

    if img:
        #создать окно а внем изображение потом
        new_window = Toplevel()
        new_window.title('Картинка')
        new_window.geometry('600x480')
        label=Label(new_window, image=img)
        label.pack()
        label.image = img

def exit():
    window.destroy()



window = Tk()
window.title('Cats!')
window.geometry('600x520')

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack()

#создаем местку. где будет изображение
# label=Label()
# label.pack()

#добавим кнопку, при нажатии , чтоб давала следующую картинку
# update_button = Button(text ='Обновить', command=set_image)#set image функция
# update_button.pack()


#создадим меню
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход',command=exit)



#адрес из интернета, из которого берем информацию
url = "https://cataas.com/cat"
# img = load_image(url) #сделать загрузку изображения

# #проверка если не пустая переменная,
# if img:
#     label.config(image=img)
#     label.image = img #если эту строчку не написать, то комп ее выдаст, а так какмусор удалтит

open_new_window() #для первой картинке при запуске

window.mainloop()