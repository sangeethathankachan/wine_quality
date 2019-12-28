from tkinter import *
from PIL import  ImageTk,Image
#import tkFont
from tkinter import font

root=Tk(className='wine quality')
root.geometry('500x500')
label1=Label(root,text='Fixed Acidity').grid(row=0)
label2=Label(root,text='Volatile Acidity').grid(row=1)
label3=Label(root,text='Citric Acid').grid(row=2)
label4=Label(root,text='Residual Sugar').grid(row=3)
label5=Label(root,text='chlorides').grid(row=4)
label=Label(root,text='Free sulfur dioxide').grid(row=5)
label=Label(root,text='Total sulfur dioxide').grid(row=6)
label=Label(root,text='Density').grid(row=7)
label=Label(root,text='PH').grid(row=8)
label=Label(root,text='Sulphates').grid(row=9) 
label=Label(root,text='Alcohol').grid(row=10)
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)
e6=Entry(root)
e7=Entry(root)
e8=Entry(root)
e9=Entry(root)
e10=Entry(root)
e11=Entry(root)  
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
e3.grid(row=2, column=1) 
e4.grid(row=3, column=1) 
e5.grid(row=4, column=1) 
e6.grid(row=5, column=1) 
e7.grid(row=6, column=1) 
e8.grid(row=7, column=1) 
e9.grid(row=8, column=1) 
e10.grid(row=9, column=1) 
e11.grid(row=10, column=1) 

#img=ImageTk.PhotoImage(Image.open("thumb-350-394343.jpg"))

#lab2=Label(root, image=img)
#lab2.grid(row=0,coloumn=1)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
root.mainloop()
