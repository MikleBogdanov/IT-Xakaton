                


from tkinter import Tk, Text, Button, Scrollbar, Frame

tk = Tk()
tk.title('D&D генеретор')
#tk.iconbitmap('иконка.ico')
tk.attributes("-topmost",True)

vopr = ['Выберите сеттинг:', "Выберите локацию:", "Выберите неигрового персонажа:", "Выберите клоючевой объект:"]
otv = []
vopr123 = [['Космический корабль', 'Логово злодеев', 'Набережная', 'Город на Диком Западе', 'Пустыня', 'Станция', 'Город', 'Лес', 'Пещера'],
           ['Охранник', 'Механик', 'Киборг', 'Шериф', 'Ковбой', 'Кочегар', 'Торговец', 'Орк', 'Гоблин'],
           ['Бинокль', 'Ящик', 'Телефонная будка', 'Лассо', 'Бумажка', 'Склянка', 'Зелье', 'Растение', 'Обломки']]

put = [['заготовки\\сетинги\\Будущее\\Космический корабль.txt', 'заготовки\\сетинги\\Будущее\\Логово злодеев.txt','заготовки\\сетинги\\Будущее\\Набережная.txt',
        'заготовки\\сетинги\\Дикий запад\\Город на Диком Западе.txt', 'заготовки\\сетинги\\Дикий запад\\Пустыня.txt', 'заготовки\\сетинги\\Дикий запад\\Станция.txt',
        'заготовки\\сетинги\\Средневековье\\Город.txt', 'заготовки\\сетинги\\Средневековье\\Лес.txt', 'заготовки\\сетинги\\Средневековье\\Пещера.txt'],
       ['заготовки\\npc\\Охранник.txt', 'заготовки\\npc\\Механик.txt','заготовки\\npc\\Киборг.txt','заготовки\\npc\\Шериф.txt','заготовки\\npc\\Ковбой.txt','заготовки\\npc\\Кочегар.txt','заготовки\\npc\\Торговец.txt','заготовки\\npc\\Орк.txt','заготовки\\npc\\Гоблин.txt'],
       ['заготовки\\объекты\\Бинокль.txt', 'заготовки\\объекты\\Ящик.txt','заготовки\\объекты\\Телефонная будка.txt','заготовки\\объекты\\Лассо.txt','заготовки\\объекты\\Бумажка.txt','заготовки\\объекты\\Склянка.txt','заготовки\\объекты\\Зелье.txt','заготовки\\объекты\\Растение.txt','заготовки\\объекты\\Обломки.txt']]
#in =)
    

class buttons:
    color_bg = '#282824'#'#3b3f40'
    color_fg = '#f5e9cc'
    
    def __init__(self, root, *variants):
        self.frame = Frame(root, bg=self.color_bg)
        self.buttons = [Button(self.frame, text = i, bg=self.color_bg,  bd = 4, fg = self.color_fg) for i in variants]
        [i.pack(side = 'left') for i in self.buttons]
        
        self.start()
    
    def start(self):
        self.frame.pack(side = 'top', fill='x')
    
    def new(self, *variants):
        for i in self.buttons:
            i.destroy()
        self.buttons = [Button(self.frame, command = f, text = i, bg=self.color_bg,  bd = 4, fg = self.color_fg) for i in variants]
        [i.pack(side = 'left') for i in self.buttons]
    
    def stop(self):
        self.frame.pack_forget()
    
##    class f:
##        def __init__(self, n):
##            self.n = n
##        def f(self,n):
##            global otv,
##            if otv:
##                pass
##            else:
            

class window:
    color_bg = '#282824'#'#3b3f40'
    color_fg = '#f5e9cc'
    width = 50
    height = 35
    

    def __init__(self, root, vopros):
        self.frame = Frame(root)
        
        self.text = Text(self.frame, width = self.width, height = self.height, state='disabled', wrap='word', bg=self.color_bg,  bd = 4, fg = self.color_fg, selectbackground = self.color_bg, selectforeground = self.color_fg)
        self.text.pack(side = 'left')
        
        self.scrollbar = Scrollbar(self.frame, orient="vertical", command=self.text.yview)
        self.scrollbar.pack(side = 'left', fill='y')
        
        self.text.config(yscrollcommand = self.scrollbar.set)
        self.start()
        self.new(vopros)
    
    def start(self):
        self.frame.pack(side = 'top')
    
    def new(self, vopros):
        self.text.config(state='normal')
        self.text.delete(1.0,'end')
        self.text.insert(1.0, vopros)
        self.text.config(state='disabled')
    
    def stop(self):
        self.frame.pack_forget()
    
class game:
    frame = Frame(tk)
    
    color_bg = '#282824'#'#3b3f40'
    color_fg = '#f5e9cc'
    
    def __init__(self, vopros, *variants):
        self.window = window(self.frame, vopros)
        self.buttons = buttons(self.frame, *variants)
        self.start()
    
    def start(self):
        self.frame.pack()
    
    def new(self, vopros, *variants):
        self.window.new(vopros)
        self.buttons.new(*variants)
    
    def stop(self):
        self.frame.pack_forget()
    
    def new_color(color_bg, color_fg):
        self.window.color_bg = self.buttons.color_bg = self.color_bg = color_bg
        self.window.color_fg = self.buttons.color_fg = self.color_fg = color_fg
        



game_root = game(vopr[0], 'Будущее','Дикий запад','Средневековье')
tk.resizable(width=False, height=False)



def f(*f):
    for i in range(len(f)):
        game_root.buttons.buttons[i].config(command=f[i])

def f1():
    global otv
    otv=[0]
    game_root.new(vopr[1], *vopr123[0][otv[0]*3:(otv[0]+1)*3])
    g()

def f2():
    global otv
    otv=[1]
    game_root.new(vopr[1], *vopr123[0][otv[-1]*3:(otv[0]+1)*3])
    g()

def f3():
    global otv
    otv=[2]
    game_root.new(vopr[1], *vopr123[0][otv[0]*3:(otv[0]+1)*3])
    g()


f(f1, f2, f3)



def g():
    def f1():
        global otv
        otv.append(0+otv[0]*3)
        game_root.new(vopr[2], *vopr123[1][otv[0]*3:(otv[0]+1)*3])
        g2()

    def f2():
        global otv
        otv.append(1+otv[0]*3)
        game_root.new(vopr[2], *vopr123[1][otv[0]*3:(otv[0]+1)*3])
        g2()

    def f3():
        global otv
        otv.append(2+otv[0]*3)
        game_root.new(vopr[2], *vopr123[1][otv[0]*3:(otv[0]+1)*3])
        g2()


    f(f1, f2, f3)



def g2():
    def f1():
        global otv
        otv.append(0+otv[0]*3)
        game_root.new(vopr[3], *vopr123[2][otv[0]*3:(otv[0]+1)*3])
        g3()

    def f2():
        global otv
        otv.append(1+otv[0]*3)
        game_root.new(vopr[3], *vopr123[2][otv[0]*3:(otv[0]+1)*3])
        g3()

    def f3():
        global otv
        otv.append(2+otv[0]*3)
        game_root.new(vopr[3], *vopr123[2][otv[0]*3:(otv[0]+1)*3])
        g3()


    f(f1, f2, f3)



def g3():
    def f1():
        global otv
        otv.append(0+otv[0]*3)
        game_root.new('Нажмите "Сгенерировать"', "Сгенерировать")
        f(end)

    def f2():
        global otv
        otv.append(1+otv[0]*3)
        game_root.new('Нажмите "Сгенерировать"', "Сгенерировать")
        f(end)

    def f3():
        global otv
        otv.append(2+otv[0]*3)
        game_root.new('Нажмите "Сгенерировать"', "Сгенерировать")
        f(end)


    f(f1, f2, f3)


def end():
    global otv
    otv = otv[1:]
    t=''
    while otv:
        f = open(put.pop(0)[otv.pop(0)], 'rb')
        r = f.read().decode()
        f.close()
        t+=r
    game_root.new(t,'Заново')
    def reset():
        import os
        os.startfile('main.py')
    game_root.buttons.buttons[0].config(command=reset)
          





tk.mainloop()



