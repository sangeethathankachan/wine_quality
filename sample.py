import tkinter as tk
from functools import partial

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

def dataset_prediction(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9,
n10):
     df=pd.read_csv("wine.csv")

     x = df.iloc[:,0:11].values
     y = df.iloc[:,11].values
     x_train, x_test, y_train, y_test = train_test_split(x,y, test_size
= 0.3, random_state = 0)
     from sklearn.linear_model import LogisticRegression
     model=LogisticRegression()
     model.fit(x_train,y_train)
     num0 = (n1.get())
     num1 = (n1.get())
     num2 = (n2.get())
     num3 = (n3.get())
     num4 = (n4.get())
     num5 = (n5.get())
     num6 = (n6.get())
     num7 = (n7.get())
     num8 = (n8.get())
     num9 = (n9.get())
     num10 = (n10.get())


     y_pred=model.predict([[float(num0), float(num1), float(num2), float(num3), float(num4),
float(num5), float(num6), float(num7), float(num8), float(num9),
float(num10)]])
     label_Result.config(text="Wine Quality: ")     
     labelResult.config(text=y_pred)
     return 0

    

root = tk.Tk()
root.geometry('400x400')
root.title('pre')

num0 = tk.StringVar()

num1 = tk.StringVar()
num2 = tk.StringVar()
num3 = tk.StringVar()
num4 = tk.StringVar()
num5 = tk.StringVar()
num6 = tk.StringVar()
num7 = tk.StringVar()
num8 = tk.StringVar()
num9 = tk.StringVar()
num10 = tk.StringVar()




labelNum0 = tk.Label(root, text="Fixed Acidity").grid(row=0, column=0)
labelNum1 = tk.Label(root, text="Volatile Acidity").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Citric Acid").grid(row=2, column=0)
labelNum3 = tk.Label(root, text="Residual Sugar").grid(row=3, column=0)
labelNum4 = tk.Label(root, text="chlorides").grid(row=4, column=0)
labelNum5 = tk.Label(root, text="Free sulfur dioxide").grid(row=5, column=0)
labelNum6 = tk.Label(root, text="Total sulfur dioxide").grid(row=6, column=0)
labelNum7 = tk.Label(root, text="Density").grid(row=7, column=0)
labelNum8 = tk.Label(root, text="PH").grid(row=8, column=0)
labelNum9 = tk.Label(root, text="Sulphates").grid(row=9, column=0)
labelNum10 = tk.Label(root, text="Alcohol").grid(row=10, column=0)




label_Result=tk.Label(root)

labelResult = tk.Label(root)
label_Result.grid(row=17, column=0)
labelResult.grid(row=17, column=2)

entryNum1 = tk.Entry(root, textvariable=num0).grid(row=0, column=2)
entryNum2 = tk.Entry(root, textvariable=num1).grid(row=1, column=2)
entryNum3 = tk.Entry(root, textvariable=num2).grid(row=2, column=2)
entryNum4 = tk.Entry(root, textvariable=num3).grid(row=3, column=2)
entryNum5 = tk.Entry(root, textvariable=num4).grid(row=4, column=2)
entryNum6 = tk.Entry(root, textvariable=num5).grid(row=5, column=2)
entryNum7 = tk.Entry(root, textvariable=num6).grid(row=6, column=2)
entryNum8 = tk.Entry(root, textvariable=num7).grid(row=7, column=2)
entryNum9 = tk.Entry(root, textvariable=num8).grid(row=8, column=2)
entryNum10 = tk.Entry(root, textvariable=num9).grid(row=9, column=2)
entryNum11 = tk.Entry(root, textvariable=num10).grid(row=10, column=2)





dataset_prediction= partial(dataset_prediction,num0,num1
,num2,num3,num4,num5 ,num6 ,num7,num8,num9,num10)
buttonCal = tk.Button(root, text="submit", command=dataset_prediction)

buttonCal.grid(row=14, column=0)
if __name__ =="__dataset_prediction__":
    dataset_prediction()
root.mainloop()
