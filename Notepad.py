from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title("Notepad")
root.geometry("500x250")

#open_img = ImageTk.PhotoImage(Image.open("open.png"))
#save_img = ImageTk.PhotoImage(Image.open("save.png"))
#exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root,text="File Name")
label_file_name.place(relx=0.2,rely=0.03,anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.03,anchor=CENTER)


my_text = Text(root,height=20,width=70)
my_text.place(relx=0.5,rely=0.35,anchor=CENTER)

def clear_input_field():
    input_file_name.delete(0,END)
    
def clear_text_area():
    my_text.delete(1.0,END)
    
def add_data():
    input_file_name.insert(END,"My File")

open_btn = Button(root,text="Clear Input Field",command=clear_input_field)
open_btn.place(relx=0.2,rely=0.7,anchor=CENTER)

save_btn = Button(root,text="Clear Text Area",command=clear_text_area)
save_btn.place(relx=0.4,rely=0.7,anchor=CENTER)

exit_btn = Button(root,text="Add Data",command=add_data)
exit_btn.place(relx=0.7,rely=0.7,anchor=CENTER)
root.mainloop()