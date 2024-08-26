
from tkinter import *
from customtkinter import *

root=Tk()
root.geometry("800x550")
root.title("log in")
root.resizable(False,False)
root.configure(background="#e7e7dd")

img=PhotoImage(file="word-image-5.png")
imglabel=Label(root,image=img,width=400,height=500,bg="#e7e7dd")
imglabel.place(x=60,y=10)


frame=CTkFrame(root,bg_color="#e7e7dd",fg_color="#ffffff",width=310,height=400,corner_radius=20)
frame.place(x=460,y=70)

font=CTkFont(family="Helvetica",size=30,slant="italic")
label_name=CTkLabel(root,text="log in",font=font,bg_color="#ffffff")
label_name.place(x=575,y=100)

font2=CTkFont(family="Helvetica",size=18,slant="italic")
user_label=CTkLabel(root,text="user",font=font2,bg_color="#ffffff")
user_label.place(x=490,y=180)

user_entry=CTkEntry(root,placeholder_text="enter youe username...",width=200,corner_radius=15,bg_color="#ffffff")
user_entry.place(x=550,y=180)

pass_label=CTkLabel(root,text="pass",font=font2,bg_color="#ffffff")
pass_label.place(x=485,y=225)

pass_entry=CTkEntry(root,placeholder_text="enter youe password...",width=200,corner_radius=15,bg_color="#ffffff")
pass_entry.place(x=550,y=225)

btn_sign=CTkButton(root,text="log in ",text_color="#ffffff",width=240,bg_color="#ffffff",corner_radius=15,fg_color="#673dff",hover_color="#b38bff")
btn_sign.place(x=500,y=300)

label_logtext=CTkLabel(root,text="don't have an account? ",bg_color="#ffffff")
label_logtext.place(x=520,y=345)

btn_log=CTkButton(root,text_color="#673dff",width=70,text="sign up",fg_color="#e7e7dd",bg_color="#ffffff",hover_color="#b38bff",corner_radius=30)
btn_log.place(x=675,y=342)

icon_img=PhotoImage(file="photo2.png")
root.iconphoto(True,icon_img)


root.mainloop()