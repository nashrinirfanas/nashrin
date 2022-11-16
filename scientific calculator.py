from tkinter import *
import math
window =Tk()
window.title('scientific calculator')
window.geometry('320x315')
window.resizable (width=FALSE,height=FALSE)

def click(number):
    ex = ent.get()
    operator = ""
    try:
        if number == 'c':
            ex = ex[0:len(ex) - 1]
            ent.delete(0, END)
            ent.insert(0, ex)
            return
        elif number == "ce":
            ent.delete(0, END)
        elif number == "=":
            operator =eval(ex)
        elif number == "√":
            operator = math.sqrt(eval(ex))
        elif number == "tan":
            operator = math.atan(math.radians(eval(ex)))
        elif number == "cos":
            operator = math.acos(math.radians(eval(ex)))
        elif number == "sin":
            operator = math.asin(math.radians(eval(ex)))
        elif number == "sinh":
            operator = math.asinh((eval(ex)))
        elif number == "cosh":
            operator = math.acosh((eval(ex)))
        elif number == "tanh":
            operator = math.atan((eval(ex)))
        elif number == "x!":
            operator = math.factorial(eval(ex))
        elif number == "x2":
            operator = eval(ex) ** 2
        elif number == "x3":
            operator = eval(ex) ** 3
        elif number == "//":
            operator = math.floor(eval(ex))
        elif number == "ceil":
            operator = math.ceil(eval(ex))
        elif number == "pi":
            operator = math.pi
        elif number == "tau":
            operator = math.tau
        elif number == "e":
            operator = math.e
        elif number == "deg":
            operator = math.degrees(eval(ex))
        elif number == "rad":
            operator = math.radians(eval(ex))
        elif number == "hypot":
            operator = math.hypot(eval(ex))
        elif number == "deg":
            operator = math.degrees(eval(ex))
        elif number == "log":
            operator = math.log(eval(ex))
        elif number == "log10":
            operator = math.log10(eval(ex))
        elif number == "gamma":
            operator = math.gamma(eval(ex))
        elif number == "1/x":
            operator=1/eval(ex)
        elif number == "exp":
            operator=math.exp(eval(ex))

        else:
            ent.insert(END, number)
            return
        ent.delete(0, END)
        ent.insert(0, operator)
    except SyntaxError :
        pass

# operator = ""
text_input=StringVar()
ent=Entry(window,textvariable=text_input,bg="lavender",relief=GROOVE,borderwidth=5,width=50)
ent.focus()
# ent.insert(0,"0")
btn=Button(text=7,fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click(7))
btn1=Button(text=8,fg='black',bg='thistle',width=10,relief=SUNKEN ,command=lambda:click(8))
btn2=Button(text=9,fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click(9))
btn3=Button(text="-",fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click("-"))
btn4=Button(text=4,fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click(4))
btn5=Button(text=5,fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click(5))
btn6=Button(text=6,fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click(6))
btn7=Button(text="+",fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click("+"))
btn8=Button(text=1,fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click(1))
btn9=Button(text=2,fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click(2))
btn10=Button(text=3,fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click(3))
btn11=Button(text="=",fg='black',bg='light grey',width=10,relief=SUNKEN,command=lambda:click("="))
btn12=Button(text="*",fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click("*"))
btn13=Button(text=0,fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click("0"))
btn14=Button(text="%",fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click("%"))
btn15=Button(text="c",fg='black',bg='light grey',width=10,relief=SUNKEN,command=lambda:click("ce"))
btn16=Button(text=".",fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click("."))
btn17=Button(text="x^y",fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click("**"))
btn18=Button(text="del",fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click("c"))
btn19=Button(text="/",fg='black',bg='thistle',width=10,relief=SUNKEN,command=lambda:click("/"))
btn20=Button(text="cos",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("cos"))
btn21=Button(text="√",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("√"))
btn22=Button(text="sin",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("sin"))
btn23=Button(text="tan",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("tan"))
btn24=Button(text="sinh",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("sinh"))
btn25=Button(text="cosh",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("cosh"))
btn26=Button(text="tanh",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("tanh"))
btn27=Button(text="x2",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("x2"))
btn28=Button(text="tau",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("tau"))
btn29=Button(text="pi",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("pi"))
btn30=Button(text="e",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("e"))
btn31=Button(text="x3",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("x3"))
btn32=Button(text="ceil",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("ceil"))
btn33=Button(text="floor division",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("//"))
btn34=Button(text="deg",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("deg"))
btn35=Button(text="rad",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("rad"))
btn36=Button(text="hypot",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("hypot"))
btn37=Button(text="log",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("log"))
btn38=Button(text="log10",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("log10"))
btn39=Button(text="gamma",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("gamma"))
btn40=Button(text="(",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("("))
btn41=Button(text=")",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click(")"))
btn42=Button(text="1/x",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("1/x"))
btn43=Button(text="exp",fg='black',bg='thistle2',width=10,relief=SUNKEN,command=lambda:click("exp"))


ent.grid(columnspan = 4)
btn.grid(row = 1, column = 0)
btn1.grid(row = 1, column = 1)
btn2.grid(row = 1, column = 2)
btn3.grid(row = 1, column = 3)
btn4.grid(row = 2, column = 0)
btn5.grid(row = 2, column = 1)
btn6.grid(row = 2, column = 2)
btn7.grid(row = 2, column = 3)
btn8.grid(row = 3, column = 0)
btn9.grid(row = 3, column = 1)
btn10.grid(row = 3, column = 2)
btn11.grid(row = 3, column = 3)
btn12.grid(row = 4, column = 0)
btn13.grid(row = 4, column = 1)
btn14.grid(row = 4, column = 2)
btn15.grid(row = 4, column = 3)
btn16.grid(row = 5, column = 0)
btn17.grid(row = 5, column = 1)
btn18.grid(row = 5, column = 2)
btn19.grid(row = 5, column = 3)
btn22.grid(row = 6, column = 0)
btn20.grid(row = 6, column = 1)
btn23.grid(row = 6, column = 2)
btn21.grid(row = 6, column = 3)
btn24.grid(row = 7, column = 0)
btn25.grid(row = 7, column = 1)
btn26.grid(row = 7, column = 2)
btn27.grid(row = 7, column = 3)
btn28.grid(row = 8, column = 0)
btn29.grid(row = 8, column = 1)
btn30.grid(row = 8, column = 2)
btn31.grid(row = 8, column = 3)
btn32.grid(row = 9, column = 0)
btn33.grid(row = 9, column = 1)
btn34.grid(row = 9, column = 2)
btn35.grid(row = 9, column = 3)
btn36.grid(row = 10, column = 0)
btn37.grid(row = 10, column = 1)
btn38.grid(row = 10, column = 2)
btn39.grid(row = 10, column = 3)
btn40.grid(row = 11, column = 0)
btn41.grid(row = 11, column = 1)
btn42.grid(row = 11, column = 2)
btn43.grid(row = 11, column = 3)
window.mainloop()
