
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont

import joblib
modal = joblib.load('model.joblib')

win = Tk()
win.title('Email Fraud Detection')


#setting window size
width=600
height=500
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
win.geometry(alignstr)
win.resizable(width=False, height=False)

def MainPage():
    def OfflineSpamCheck():
        #destroying the mainPage Buttons
        HeadingLabel.destroy()
        mp_Button_Online.destroy()
        mp_Button_Offline.destroy()

        
        def Action():
            inputValue = TextBox.get("1.0","end-1c")
            import pandas as pd
            df = pd.DataFrame()
            df = pd.DataFrame(columns = ['Emails'])
            df.loc[0,'Emails'] = inputValue
            #print(df.shape)
            output = modal.predict(df['Emails'])
            if output == 1:
                TextBox2.insert(END, 'Spam')
            else :
                TextBox2.insert(END, 'Not Spam')
        def BackfromOfflineToMp():
            #destroying Buttons
            label.destroy()
            TextBox.destroy()
            TextBox2.destroy()
            button.destroy()
            backButton.destroy()
            #Calling main Page
            MainPage()
        
        #Offline Label        
        label = tk.Label(win,text ="Offline Spam Check")
        ft = tkFont.Font(family='Times',size=28)
        label["font"] = ft
        label.place(x=130,y=20,width=349,height=66)

        TextBox = tk.Text(win,width = 16,height = 20)
        TextBox.place(x=10,y=90,width=573,height=253)
        TextBox2 = tk.Text(win,width = 16,height = 5)
        TextBox2.place(x=210,y=390,width=161,height=67)

        button = tk.Button(win,text = 'Test', command = lambda:Action())
        button.place(x=260,y=350,width=70,height=25)
        backButton = tk.Button(win,text = 'Back')
        backButton["command"] = BackfromOfflineToMp
        backButton.place(x=10,y=40,width=70,height=25)
        #Back Button Implementation
        
    #mainPage
    HeadingLabel = tk.Label(win)
    ft = tkFont.Font(family='Times',size=28)
    HeadingLabel["font"] = ft
    HeadingLabel["fg"] = "#333333"
    HeadingLabel["justify"] = "center"
    HeadingLabel["text"] = "Email Fraud Detection"
    HeadingLabel.place(x=130,y=30,width=412,height=59)
    
    mp_Button_Online=tk.Button(win)
    ft = tkFont.Font(family='Times',size=10)
    mp_Button_Online["font"] = ft
    mp_Button_Online["text"] = "Fetch Emails"
    mp_Button_Online.place(x=250,y=120,width=127,height=30)
    mp_Button_Online["command"] = OfflineSpamCheck

    mp_Button_Offline=tk.Button(win)
    ft = tkFont.Font(family='Times',size=10)
    mp_Button_Offline["font"] = ft
    mp_Button_Offline["text"] = "Enter Email "
    mp_Button_Offline.place(x=250,y=190,width=124,height=30)
    mp_Button_Offline["command"] = OfflineSpamCheck


MainPage()
win.mainloop()