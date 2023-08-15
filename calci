# python_based_projects presents a 'Basic Calculator' using python and package used is 'Tkinter'
#Here are the line of codes


from tkinter import Tk, END, Entry, N, E, S, W, Button, font, Label
from functools import partial

def get_in(entry, argu):
    entry.insert(END, argu)

    
def back_space(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

    
def clear(entry):
    entry.delete(0, END)

    
def calcu(entry):
    input_data = entry.get()
    try:
        output_data = str(eval(input_data.strip()))
    except ZeroDivisionError:
        popup_msg()
        output_data = ""
    clear(entry)
    entry.insert(END, output_data)


def popup_msg():
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("120x100")
    popup.title("Alert!")
    label = Label(popup, text="Number isn't divisible by 0. \n Please Enter valid values!")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()


def calci():
    root = Tk()
    root.title("myCalci")
    root.resizable(0, 0)

    entryFont = font.Font(size=15)
    entry = Entry(root, justify="right", font=entryFont)
    entry.grid(row=0, column=0, columnspan=4,
               sticky=N + W + S + E, padx=5, pady=5)

    Cal_Button_bg = '#BEADFA'
    Num_Button_bg = '#D0BFFF'
    Other_Button_bg = '#DFCCFB'
    Text_fg = '#FFFFFF'
    Button_Active_bg = '#FFF3DA'

    Num_Button = partial(Button, root, fg=Text_fg, bg=Num_Button_bg,
                         padx=10, pady=3, activebackground=Button_Active_bg)
    Cal_Button = partial(Button, root, fg=Text_fg, bg=Cal_Button_bg,
                         padx=10, pady=3, activebackground=Button_Active_bg)

    b7 = Num_Button(text='7', bg=Num_Button_bg,
                         command=lambda: get_in(entry, '7'))
    b7.grid(row=2, column=0, pady=5)

    b8 = Num_Button(text='8', command=lambda: get_in(entry, '8'))
    b8.grid(row=2, column=1, pady=5)

    b9 = Num_Button(text='9', command=lambda: get_in(entry, '9'))
    b9.grid(row=2, column=2, pady=5)

    b10 = Cal_Button(text='+', command=lambda: get_in(entry, '+'))
    b10.grid(row=4, column=3, pady=5)

    b4 = Num_Button(text='4', command=lambda: get_in(entry, '4'))
    b4.grid(row=3, column=0, pady=5)

    b5 = Num_Button(text='5', command=lambda: get_in(entry, '5'))
    b5.grid(row=3, column=1, pady=5)

    b6 = Num_Button(text='6', command=lambda: get_in(entry, '6'))
    b6.grid(row=3, column=2, pady=5)

    b11 = Cal_Button(text='-', command=lambda: get_in(entry, '-'))
    b11.grid(row=3, column=3, pady=5)

    b1 = Num_Button(text='1', command=lambda: get_in(entry, '1'))
    b1.grid(row=4, column=0, pady=5)

    b2 = Num_Button(text='2', command=lambda: get_in(entry, '2'))
    b2.grid(row=4, column=1, pady=5)

    b3 = Num_Button(text='3', command=lambda: get_in(entry, '3'))
    b3.grid(row=4, column=2, pady=5)

    b12 = Cal_Button(text='*', command=lambda: get_in(entry, '*'))
    b12.grid(row=2, column=3, pady=5)

    b0 = Num_Button(text='0', command=lambda: get_in(entry, '0'))
    #button0.grid(row=5, column=0, columnspan=2, padx=3, pady=5, sticky=N + S + E + W)
    b0.grid(row=5, column=0,  pady=5)

    b13 = Num_Button(text='.', command=lambda: get_in(entry, '.'))
    b13.grid(row=5, column=1, pady=5)

    b14 = Button(root, text='/', fg=Text_fg, bg=Cal_Button_bg, padx=10, pady=3,
                      command=lambda: get_in(entry, '/'))
    b14.grid(row=1, column=3, pady=5)

    b15 = Button(root, text='<-', bg=Other_Button_bg, padx=10, pady=3,
                      command=lambda: back_space(entry), activebackground=Button_Active_bg)
    b15.grid(row=1, column=0, columnspan=2,
                  padx=3, pady=5, sticky=N + S + E + W)

    b16 = Button(root, text='C', bg=Other_Button_bg, padx=10, pady=3,
                      command=lambda: clear(entry), activebackground=Button_Active_bg)
    b16.grid(row=1, column=2, pady=5)

    b17 = Button(root, text='=', fg=Text_fg, bg=Cal_Button_bg, padx=10, pady=3,
                      command=lambda: calcu(entry), activebackground=Button_Active_bg)
    b17.grid(row=5, column=3, pady=5)

    b18 = Button(root, text='^', fg=Text_fg, bg=Cal_Button_bg, padx=10, pady=3,
                      command=lambda: get_in(entry, '**'))
    b18.grid(row=5, column=2, pady=5)
    def quit():
        exit['command'] = root.quit()
    exit = Button(root, text='Quit', fg='black', bg='white', command=quit, height=1, width=7)
    exit.grid(row=6, column=1)

    root.mainloop()


if __name__ == '__main__':
    calci()
