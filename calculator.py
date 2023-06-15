import math
from tkinter import *


root=Tk()
root.title("Calculator")
root.configure(background="#f1f5f9")
root.resizable(width=False, height=False)
root.geometry("351x530+20+20")

scientific_frame = Frame(root)
my_frame = Frame(root)

my_label_result = Entry(my_frame,  font=('Times', 20, 'bold'),width=23,bd=2,justify=RIGHT,bg="#f1f5f0",relief=SUNKEN,insertwidth=5)

my_label_scientific = Entry(scientific_frame,  font=('Times', 20, 'bold'),width=23,bd=2,justify=RIGHT,bg="#f1f5f0",relief=SUNKEN,insertwidth=5)


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
        'text': 'π',
        'command': lambda:  sci.pi(),
        'bg': '#c7d2fe',
    },
    {
        'text': 'e',
        'command': lambda: sci.e(),
         'bg': '#c7d2fe',
    },

    {
        'text': 'n!',
        'command': lambda : sci.fact(),
        'bg':'#c7d2fe',
    },
    {
        'text': '√',
        'command': lambda : sci. sqrt_num(),
        'bg':'#c7d2fe',
    },
    {
        'text': 'deg',
        'command': lambda: sci.deg(),
        'bg': '#c7d2fe',
    },
    {
        'text': 'sin',
        'command': lambda: sci.sin(),
        'bg': '#c7d2fe',
    },
    {
        'text': 'cos',
        'command': lambda : sci.cos(),
        'bg':'#c7d2fe',
    },

    {
        'text': 'tan',
        'command': lambda : sci.tan(),
        'bg':'#c7d2fe',
    },
    {
        'text': 'cot',
        'command': lambda: sci.cot(),
        'bg': '#c7d2fe',
    },
    {
        'text': 'mod',
        'command': lambda : sci.opration('mod'),
        'bg':'#c7d2fe',
    },

    {
        'text': "ln",
        'command': lambda: sci.ln(),
        'bg': '#c7d2fe',
    },
    {
        'text': 'inv',
        'command': lambda : sci.opration('inv'),
        'bg':'#c7d2fe',
    },
    {
        'text': '2π',
        'command': lambda: sci.p2(),
        'bg': '#c7d2fe',
    },
{
        'text': 'log2',
        'command': lambda : sci.log2(),
    'bg': '#c7d2fe',
        },
    {
            'text': 'log10',
            'command': lambda : sci.log10(),
     'bg': '#c7d2fe',
        },
 {
        'text': '7',
        'command': lambda :sci.add_number('7'),
        'bg':'#f1f5f9'
    },
    {
        'text': '8',
        'command': lambda : sci.add_number('8'),
'bg':'#f1f5f9'
    },
    {
        'text': '9',
        'command': lambda :sci.add_number('9'),
'bg':'#f1f5f9'
    },
{
        'text': 'C',
        'command': lambda : sci.clear(),
        'bg':'#818cf8',
    },
    {
        'text': 'CE',
        'command': lambda :sci.clear_all(),
        'bg':'#818cf8',
    },
 {
        'text': '4',
        'command': lambda : sci.add_number('4'),
'bg':'#f1f5f9'
    },
    {
        'text': '5',
        'command': lambda : sci.add_number('5'),
'bg':'#f1f5f9'
    },
    {
        'text': '6',
        'command': lambda : sci.add_number('6'),
'bg':'#f1f5f9'
    },
    {
        'text': '×',
        'command': lambda: sci.opration('multiply'),
        'bg': '#f1f5f9',
    },
    {
        'text': chr(247),
        'command': lambda: sci.opration('divide'),
        'bg': '#f1f5f9'
    },
{
        'text': '1',
        'command': lambda : sci.add_number('1'),
'bg':'#f1f5f9'
    },
    {
        'text': '2',
        'command': lambda : sci.add_number('2'),
'bg':'#f1f5f9'
    },
    {
        'text': '3',
        'command': lambda : sci.add_number('3'),
'bg':'#f1f5f9'
    },
    {
        'text': '+',
        'command': lambda : sci.opration('sum'),
'bg':'#f1f5f9'
    },
    {
        'text': '-',
        'command': lambda : sci.opration('minus'),
         'bg':'#f1f5f9',
    },
    {
            'text':"0",
            'command': lambda : sci.add_number('0'),
    'bg':'#f1f5f9'
        },

   {
        'text':"+/-",
        'command': lambda :  sci.sign(),
'bg':'#f1f5f9'
    },
     {
            'text':"EXP",
            'command': lambda : sci.exp(),
         'bg': '#f1f5f9'

        },
   {
        'text':".",
        'command': lambda : sci.add_number("."),
'bg':'#f1f5f9'

    },
{
        'text':"=",
        'command': lambda : sci.calc_total(),
    'bg':'#f1f5f9'
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
        my_label_result.grid(row=1, column=0, columnspan=4, pady=32, padx=10)
        my_label_result.delete(0,END)
        my_label_result.insert(0, '0')
        list_of_btn = []
        for calc_key_data  in self.calc_dic:
            btn = Button(my_frame,text=calc_key_data['text'],width=5,height=2,bd = 2,command=calc_key_data['command'],relief=GROOVE,bg=calc_key_data['bg'], font=('Times', 20, 'bold'))
            list_of_btn.append(btn)
        for i,btn in enumerate(list_of_btn):
            btn.grid(row= i // 4 + 2,column= i % 4)
        self.new_num = True

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

class  Scientific():
    def __init__(self, calc_dic,scientific_calc_dict):
        self.scientific_calc_dict=scientific_calc_dict
        self.current_sci= ""
        self.new_num_sci = True
        self.total_sci = 0
        self.operate_sci = ""
        self.op_pending_sci = False
        self.eq_sci = False

    def hide_menu_frames(self):
        my_frame.pack_forget()
        scientific_frame.pack_forget()

    def scientific(self):
        self.hide_menu_frames()
        scientific_frame.pack(fill=BOTH,expand=1)
        my_label_scientific .grid(row=1, column=0, columnspan=5, pady=15, padx=10)
        my_label_scientific.delete(0,END)
        my_label_scientific .insert(0, '0')
        list_of_btn = []
        for calc_key_data  in self.scientific_calc_dict:
            btn = Button( scientific_frame,text=calc_key_data['text'],width=5,height=2,command=calc_key_data['command'],relief='groove',bg=calc_key_data['bg'], font=('Times', 16, 'bold'))
            list_of_btn.append(btn)
        for i,btn in enumerate(list_of_btn):
            btn.grid(row= i // 5 + 2,column= i % 5)
        self.new_num_sci = True

    def clear(self):
        self.current_sci = self.current_sci [:-1]
        if self.current_sci  == "":
            self.current_sci  = "0"
            self.new_num_sci  = True
        self.display_scientific(self.current_sci )

    def clear_all(self):
        self.current_sci  = '0'
        self.display_scientific(self.current_sci )
        self.new_num_sci  = True

    def add_number(self,num):
        first_num = my_label_scientific.get()
        second_num = str(num)
        if self.new_num_sci:
            self.current_sci = second_num
            self.new_num_sci = False
        else:
            if second_num == ".":
                if second_num in first_num:
                    return
            self.current_sci = first_num + second_num
        self.display_scientific(self.current_sci)

    def do_opration(self):
        if self.operate_sci == "sum":
            self.total_sci += self.current_sci
        elif self.operate_sci == "minus":
            self.total_sci -= self.current_sci
        elif self.operate_sci == "multiply":
            self.total_sci *= self.current_sci
        elif self.operate_sci == "divide":
            self.total_sci /= self.current_sci
        elif self.operate_sci == "mod":
            self.total_sci %= self.current_sci
        elif self.operate_sci == "inv":
            self.total_sci = 1/self.current_sci
        self.new_num_sci = True
        self.op_pending_sci = False
        self.display_scientific(self.total_sci)

    def opration(self,op):
        self.current_sci = float(self.current_sci)
        if self.op_pending_sci:
            self.do_opration()
        elif not self.operate_sci:
            self.total_sci = self.current_sci
        self.new_num_sci = True
        self.op_pending_sci = True
        self.operate_sci = op
        self.eq_sci = False

    def display_scientific(self,num):
        my_label_scientific.delete(0,END)
        my_label_scientific.insert(0,num)

    def calc_total(self):
        self.eq_sci = True
        self.current_sci = float(self.current_sci)
        if self.op_pending_sci == True:
            self.do_opration()
        else:
            self.total_sci = float(my_label_scientific.get())
        self.current_sci = '0'
        self.new_num_sci = True
        self.operate_sci = ''

    def sign(self):
        self.eq_sci = False
        self.current_sci = -(float(my_label_scientific.get()))
        self.display_scientific(self.current_sci)
    def sqrt_num(self):
        self.eq_sci = False
        self.current_sci = math.sqrt(float(my_label_scientific.get()))
        self.display_scientific(self.current_sci)

    def pi(self):
        self.eq_sci = False
        self.current_sci = math.pi
        self.display_scientific(self.current_sci)

    def e(self):
        self.eq_sci = False
        self.current_sci = math.e
        self.display_scientific(self.current_sci)

    def factorial(self,n):
        if (n == 0 or n == 1):
                return 1
        else:
                return  n* self.factorial(n-1)
    def fact(self):
        self.eq_sci = False
        result = int(my_label_scientific.get())
        self.current_sci = self.factorial(result)
        self.display_scientific(self.current_sci)
        # self.current_sci = ""
        # self.new_num_sci = True

    def deg(self):
        self.eq_sci = False
        self.current_sci= math.degrees(float(my_label_scientific.get()))
        self.display_scientific(self.current_sci)

    def sin(self):
        self.eq_sci = False
        self.current_sci = math.sin(math.radians(float(my_label_scientific.get())))
        self.display_scientific(self.current_sci)

    def cos(self):
        self.eq_sci = False
        self.current_sci = math.cos(math.radians(float(my_label_scientific.get())))
        self.display_scientific(self.current_sci)

    def tan(self):
        self.eq_sci = False
        self.current_sci = math.tan(math.radians(float(my_label_scientific.get())))
        self.display_scientific(self.current_sci)

    def cot(self):
        self.eq_sci = False
        self.current_sci = 1/(math.tan(math.radians(float(my_label_scientific.get()))))
        self.display_scientific(self.current_sci)

    def ln(self):
        self.eq_sci = False
        self.current_sci = math.log(float(my_label_scientific.get()))
        self.display_scientific(self.current_sci)
    def log2(self):
        self.eq_sci = False
        self.current_sci = math.log2(float(my_label_scientific.get()))
        self.display_scientific(self.current_sci)

    def log10(self):
        self.eq_sci = False
        self.current_sci = math.log10(float(my_label_scientific.get()))
        self.display_scientific(self.current_sci)

    def p2(self):
        self.eq_sci = False
        self.current_sci = math.tau
        self.display_scientific(self.current_sci)

    def exp(self):
        self.eq_sci = False
        self.current_sci = math.exp(float(my_label_scientific.get()))
        self.display_scientific(self.current_sci)

calc = Calculator(calc_dict,scientific_calc_dict)
calc.standard()

sci= Scientific(calc_dict,scientific_calc_dict)
my_menu = Menu(root)
root.config(menu= my_menu)

file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='Standard',command=calc.standard)
file_menu.add_command(label='Scientific',command=sci.scientific)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.quit)

root.mainloop()