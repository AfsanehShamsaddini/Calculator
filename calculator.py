import math
from tkinter import *


root=Tk()
root.title("Calculator")
root.configure(background="#f1f5f9")
root.resizable(width=False, height=False)
root.geometry("360x496+20+20")

scientific_frame = Frame(root)
my_frame = Frame(root)

my_label_result = Entry(my_frame,  font=('Times', 20, 'bold'),width=23,bd=2,justify=RIGHT,bg="#f1f5f0",relief=SUNKEN,insertwidth=5)
my_label_result.grid(row=1, column=0,columnspan=4,pady=15,padx=10)
my_label_result.insert(0,'0')

calc_dict = [
     {
        'text': 'C',
        'command': lambda : calc.clear(),
         'bg':'#c7d2fe',
    },
    {
        'text': 'CE',
        'command': lambda : calc.clear_all(),
        'bg':'#c7d2fe',
    },
    {
        'text': "√",
        'command': lambda :calc. sqrt_num(),
        'bg':'#c7d2fe',
    },
    {
        'text': '+',
        'command': lambda : calc.opration('sum'),
         'bg':'#c7d2fe',
    },
    {
        'text': '7',
        'command': lambda : calc.add_num('7'),
        'bg':'#f1f5f9'
    },
    {
        'text': '8',
        'command': lambda : calc.add_num('8'),
'bg':'#f1f5f9'
    },
    {
        'text': '9',
        'command': lambda : calc.add_num('9'),
'bg':'#f1f5f9'
    },
    {
        'text': '-',
        'command': lambda : calc.opration('minus'),
         'bg':'#c7d2fe',
    },
    {
        'text': '4',
        'command': lambda : calc.add_num('4'),
'bg':'#f1f5f9'
    },
    {
        'text': '5',
        'command': lambda : calc.add_num('5'),
'bg':'#f1f5f9'
    },
    {
        'text': '6',
        'command': lambda : calc.add_num('6'),
'bg':'#f1f5f9'
    },
    {
        'text': '×',
        'command': lambda : calc.opration('multiply'),
         'bg':'#c7d2fe',
    },
    {
        'text': '1',
        'command': lambda : calc.add_num('1'),
'bg':'#f1f5f9'
    },
    {
        'text': '2',
        'command': lambda : calc.add_num('2'),
'bg':'#f1f5f9'
    },
    {
        'text': '3',
        'command': lambda : calc.add_num('3'),
'bg':'#f1f5f9'
    },
    {
        'text':chr(247),
        'command': lambda : calc.opration('divide'),
'bg':'#c7d2fe',
    },
    {
        'text':"0",
        'command': lambda : print("0"),
'bg':'#c7d2fe',
    },
   {
        'text':".",
        'command': lambda : calc.add_num("."),
'bg':'#c7d2fe',
    },
   {
        'text':"+/-",
        'command': lambda : calc.sign(),
'bg':'#c7d2fe',
    },
   {
        'text':"=",
        'command': lambda : calc.calc_total(),
'bg':'#818cf8',

    },
]
scientific_calc_dict = [
     {
        'text': 'deg',
        'command': lambda : print('deg'),
         'bg':'#c7d2fe',
    },
    {
        'text': 'π',
        'command': lambda: print('π'),
        'bg': '#c7d2fe',
    },
    {
        'text': 'C',
        'command': lambda : print('C'),
        'bg':'#c7d2fe',
    },
    {
        'text': 'CE',
        'command': lambda : print('CE'),
        'bg':'#c7d2fe',
    },
    {
        'text': '|x|',
        'command': lambda: print('|x|'),
        'bg': '#c7d2fe',
    },
    {
        'text':'2π',
        'command': lambda : print('2π'),
'bg':'#c7d2fe',
    },
    {
        'text': 'cos',
        'command': lambda : print('cos'),
        'bg':'#c7d2fe',
    },
    {
        'text': 'sin',
        'command': lambda : print('sin'),
        'bg':'#c7d2fe',
    },
    {
        'text': 'tan',
        'command': lambda : print('tan'),
        'bg':'#c7d2fe',
    },
    {
        'text': 'mod',
        'command': lambda : print('mod'),
        'bg':'#c7d2fe',
    },

    {
        'text': 'sinh',
        'command': lambda : print('sinh'),
        'bg':'#c7d2fe',
    },
    {
        'text': 'cosh',
        'command': lambda : print('cosh'),
        'bg':'#c7d2fe',
    },
    {
        'text': 'tanh',
        'command': lambda : print('tanh'),
        'bg':'#c7d2fe',
    },
    {
        'text': 'Inv',
        'command': lambda : print('Inv'),
        'bg':'#c7d2fe',
    },
    {
        'text':chr(247),
        'command': lambda : print(chr(247)),
        'bg':'#c7d2fe',
    },

    {
        'text': 'e',
        'command': lambda : print('e'),
         'bg':'#f1f5f9',
    },
    {
        'text': '7',
        'command': lambda : print('7'),
        'bg':'#f1f5f9'
    },
    {
        'text': '8',
        'command': lambda : print('8'),
'bg':'#f1f5f9'
    },
    {
        'text': '9',
        'command': lambda : print('9'),
'bg':'#f1f5f9'
    },
    {
        'text': '×',
        'command': lambda : print('×'),
         'bg':'#f1f5f9',
    },

    {
        'text': 'log10',
        'command': lambda : print('log10'),
'bg':'#f1f5f9'
    },
    {
        'text': '4',
        'command': lambda : print('4'),
'bg':'#f1f5f9'
    },
    {
        'text': '5',
        'command': lambda : print('5'),
'bg':'#f1f5f9'
    },
    {
        'text': '6',
        'command': lambda : print('6'),
'bg':'#f1f5f9'
    },
    {
        'text': '-',
        'command': lambda : print('-'),
         'bg':'#f1f5f9',
    },

    {
        'text': 'log',
        'command': lambda : print('log'),
'bg':'#f1f5f9'
    },
    {
        'text': '1',
        'command': lambda : print('1'),
'bg':'#f1f5f9'
    },
    {
        'text': '2',
        'command': lambda : print('2'),
'bg':'#f1f5f9'
    },
    {
        'text': '3',
        'command': lambda : print('3'),
'bg':'#f1f5f9'
    },
    {
        'text': '+',
        'command': lambda : print('+'),
'bg':'#f1f5f9'
    },

    {
        'text':"ln",
        'command': lambda : print("ln"),
'bg':'#c7d2fe',
    },
   {
        'text':"+/-",
        'command': lambda : print("+/-"),
'bg':'#c7d2fe',
    },
   {
        'text':"0",
        'command': lambda : print("0"),
'bg':'#c7d2fe',
    },
   {
        'text':".",
        'command': lambda : print("."),
'bg':'#c7d2fe',

    },
{
        'text':"=",
        'command': lambda : print("="),
'bg':'#818cf8',

    },
]
class  Calculator():
    def __init__(self, calc_dic,scientific_calc_dict):
        self.calc_dic = calc_dic
        self.scientific_calc_dict=scientific_calc_dict
        self.current = ""
        self.new_num = True
        self.total = 0
        self.operate = ""
        self.op_pending = False
        self.eq = False

    def hide_menu_frames(self):
        my_frame.pack_forget()
        scientific_frame.pack_forget()
        
    def standard(self):
        self.hide_menu_frames()
        my_frame.pack(fill=BOTH,expand=1)
        list_of_btn = []
        for calc_key_data  in self.calc_dic:
            btn = Button(my_frame,text=calc_key_data['text'],width=5,height=2,bd = 2,command=calc_key_data['command'],relief=GROOVE,bg=calc_key_data['bg'], font=('Times', 20, 'bold'))
            list_of_btn.append(btn)
        for i,btn in enumerate(list_of_btn):
            btn.grid(row= i // 4 + 2,column= i % 4)
    def scientific(self):
        self.hide_menu_frames()
        scientific_frame.pack(fill=BOTH,expand=1)
        my_label_result = Entry( scientific_frame,  font=('Times', 20, 'bold'),width=24,bd=0,justify=RIGHT,bg="#f1f5f0",relief=SUNKEN)
        my_label_result.grid(row=1, column=0,columnspan=5,pady=1)
        my_label_result.insert(0,'0.0')
        list_of_btn = []
        for calc_key_data  in self.scientific_calc_dict:
            btn = Button( scientific_frame,text=calc_key_data['text'],width=5,height=2,command=calc_key_data['command'],relief='groove',bg=calc_key_data['bg'], font=('Times', 16, 'bold'))
            list_of_btn.append(btn)
        for i,btn in enumerate(list_of_btn):
            btn.grid(row= i // 5 + 2,column= i % 5)

    def clear(self):
        self.current = self.current[:-1]
        if self.current == "":
            self.current = "0"
            self.new_num = True
        self.display(self.current)

    def clear_all(self):
        self.current = '0'
        self.display(self.current)
        self.new_num = True

    def add_num(self,num):
        first_num = my_label_result.get()
        second_num = str(num)
        if self.new_num:
            self.current = second_num
            self.new_num = False
        else:
            if second_num == ".":
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def display(self,num):
        my_label_result.delete(0,END)
        my_label_result.insert(0,num)


    def do_opration(self):
        if self.operate == "sum":
            self.total += self.current
        elif self.operate == "minus":
            self.total -= self.current
        elif self.operate == "multiply":
            self.total *= self.current
        elif self.operate == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def opration(self,op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_opration()
        elif not self.operate:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.operate = op
        self.eq = False

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_opration()
        else:
            self.total = float(my_label_result.get())
        self.current = '0'
        self.new_num = True
        self.operate = ''

    def sign(self):
        self.eq = False
        self.current = -(float(my_label_result.get()))
        self.display(self.current)
    def sqrt_num(self):
        self.eq = False
        self.current = math.sqrt(float(my_label_result.get()))
        self.display(self.current)

calc = Calculator(calc_dict,scientific_calc_dict)
calc.standard()

my_menu = Menu(root)
root.config(menu= my_menu)

file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='Standard',command=calc.standard)
file_menu.add_command(label='Scientific',command=calc.scientific)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.quit)

root.mainloop()