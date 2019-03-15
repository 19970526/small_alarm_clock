import datetime
import tkinter as tk
import winsound


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('alarm clock')
        self.geometry('300x300')
        tk.Button(self, text='确认', width=8, height=2, command=self.ring).pack()
        tk.Button(self, text='关闭', width=8, height=2).pack()

    def ring(self):
        while True:
            ring_time = datetime.datetime.now().strftime('%H:%M')
            
            if ring_time == '8:42':
                winsound.PlaySound(r'..\matter\music.wav', winsound.SND_NODEFAULT)


if __name__ == '__main__':
    app = Window()
    app.mainloop()

