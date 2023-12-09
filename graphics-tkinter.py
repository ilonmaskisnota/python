from tkinter import *

# Создаем окошко программы 
root = Tk("Моя программа")
# Работаем с окошком 
root.geometry("500x300")
#  Можно ли изменить размер окна
root.resizable(width=True,height=False)
# Цвет окошка
root["bg"] = "#f803fc"


frame = Frame(root,padx=50,pady=100, width=200,height=200)
# Настраиваем местоположение фрейма
frame.place(anchor="e", relx=1, rely=0.5)
Button(frame,text="кнопочка в фрейм 1", foreground="red").pack()




frame2 = Frame(root,padx=100,pady=10, width=200,height=200)
frame2["bg"] = "#031cfc"

# Настраиваем местоположение фрейма
frame2.place(anchor="w", relx=0, rely=0.5)




root.mainloop()

