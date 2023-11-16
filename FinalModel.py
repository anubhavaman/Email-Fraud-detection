
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import re

import joblib
modal = joblib.load('model.joblib')
modal2 = joblib.load('modelNB.joblib')

win = Tk()
win.title('Email Fraud Detection')

#validate email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#setting window size
width=600
height=500
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
win.geometry(alignstr)
win.resizable(width=False, height=False)

def MainPage():
    def OnlineSpamCheck():
        #destroying the mainPage Buttons
        HeadingLabel.destroy()
        mp_Button_Online.destroy()
        mp_Button_Offline.destroy()
        
        TextBox4 = tk.Text(win,width = 16,height = 5)
       
        def BackfromOfflineToMp2():
            #destroying Buttons
            label.destroy()
            UsernameText.destroy()
            UsernameEntryBox.destroy()
            PasswordText.destroy()
            PasswordEntryBox.destroy()
            button.destroy()
            backButton.destroy()
            #Calling main Page
            MainPage()
            
        
            
        def CleaningText(emailString):
            Output(emailString)
            
        def Action3(df2):
             inputValue = df2
             import pandas as pd
             df = pd.DataFrame()
             df = pd.DataFrame(columns = ['Emails'])
             df.loc[0,'Emails'] = inputValue
             #print(df.shape)
             output = modal.predict(df['Emails'])
             output2 = modal2.predict(df['Emails'])
             if output == 1 or output2 == 1:
                 TextBox4.delete('1.0',END)
                 TextBox4.insert(END, 'Spam')
             else :
                 TextBox4.delete('1.0',END)
                 TextBox4.insert(END, 'Not Spam')
            
        def Output(df):
            label.destroy()
            UsernameText.destroy()
            UsernameEntryBox.destroy()
            PasswordText.destroy()
            PasswordEntryBox.destroy()
            button.destroy()
            backButton.destroy()
            
            def BackfromOfflineToMp3():
                #destroying Buttons
                label2.destroy()
                TextBox3.destroy()
                TextBox4.destroy()
                button2.destroy()
                backButton2.destroy()
                #Calling main Page
                MainPage()
                
            #Offline Label        
            label2 = tk.Label(win,text ="Online Spam Check")
            ft = tkFont.Font(family='Times',size=28)
            label2["font"] = ft
            label2.place(x=130,y=20,width=349,height=66)

            TextBox3 = tk.Text(win,width = 16,height = 20)
            TextBox3.place(x=10,y=90,width=573,height=253)
            
            TextBox3.insert(END,df)
            
            TextBox4.place(x=210,y=390,width=161,height=67)

            button2 = tk.Button(win,text = 'Test', command = lambda:Action3(df))
            button2.place(x=260,y=350,width=70,height=25)
            
            backButton2 = tk.Button(win,text = 'Back')
            backButton2["command"] = BackfromOfflineToMp3
            backButton2.place(x=10,y=40,width=70,height=25)
            
        
        def FetchEmails():
            import imaplib,email
            import pandas as pd
            
            df = pd.DataFrame()
            df = pd.DataFrame(columns = ['Emails'])
            user = UsernameEntryBox.get()
            password = PasswordEntryBox.get()
            print(user,password)
            imap_url = 'imap.gmail.com'
            
            # Function to get email content part i.e its body part
            def get_body(msg):
                if msg.is_multipart():
                    return get_body(msg.get_payload(0))
                else:
                    return msg.get_payload(None, True)
                
            # Function to search for a key value pair
            def search(key, value, con):
                result, data = con.search(None, key, '"{}"'.format(value))
                return data
 
            # Function to get the list of emails under this label
            def get_emails(result_bytes):
                msgs = [] # all the email data are pushed inside an array
                for num in result_bytes[0].split():
                    #typ, data = con.fetch(num, '(RFC822)')
                    typ, data = con.fetch(num, "(UID BODY[TEXT])")
                    msgs.append(data)
             
                return msgs
            # this is done to make SSL connection with GMAIL
            con = imaplib.IMAP4_SSL(imap_url)
             
            # logging the user in
            con.login(user, password)
             
            # calling function to check for email under this label
            con.select('Inbox')
             
             # fetching emails from this user "tu**h*****1@gmail.com"
            msgs = get_emails(search('FROM', 'chapranakumarprince@gmail.com', con))
            
            # printing them by the order they are displayed in your gmail
            index = 0
            for msg in msgs[::-1]:
                for sent in msg:
                    if type(sent) is tuple:
             
                        # encoding set as utf-8
                        content = str(sent[1], 'utf-8')
                        data = str(content)
             
                        # Handling errors related to unicodenecode
                        try:
                            indexstart = data.find("ltr")
                            data2 = data[indexstart + 5: len(data)]
                            indexend = data2.find("</div>")
             
                            # printtng the required content which we need
                            # to extract from our email i.e our body
                            #print(data2[0: indexend])
                            df.loc[index,'Emails'] = data2[0:indexend]
                            index += 1
             
                        except UnicodeEncodeError as e:
                            pass
            #df.head(0)
            #checking the spam or not
            df['Emails'] = df['Emails'].apply(str)
            emailString = df.loc[0,'Emails']
            #print(emailString)
            CleaningText(emailString)
            #Output(emailString)
            
        def Action():
            PasswordString = PasswordEntryBox.get()
            if(check(UsernameEntryBox.get())):
                UsernameString = UsernameEntryBox.get()
                FetchEmails()
            else:
                UsernameString = "Invalid"
            print(UsernameString,PasswordString)
        def check(email):
            # pass the regular expression
            # and the string into the fullmatch() method
            if(re.fullmatch(regex, email)):
                return True
         
            else:
                return False
 
        #Offline Label        
        label = tk.Label(win,text ="Online Spam Check")
        ft = tkFont.Font(family='Times',size=28)
        label["font"] = ft
        label.place(x=130,y=20,width=349,height=66)

        #username label
        UsernameString = tk.StringVar()
        UsernameText = tk.Label(win)
        ft = tkFont.Font(family='Times',size=13)
        UsernameText["font"] = ft
        UsernameText["text"] = "Username"
        UsernameText.place(x=160,y=140,width=77,height=38)
         
        #username entry
        UsernameEntryBox=tk.Entry(win,textvariable = UsernameString)
        UsernameEntryBox["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        UsernameEntryBox["font"] = ft
        UsernameEntryBox.place(x=260,y=140,width=262,height=36)
        
        #passwordlabel
        PasswordText = tk.Label(win)
        ft = tkFont.Font(family='Times',size=13)
        PasswordText["font"] = ft
        PasswordText["text"] = "Password"
        PasswordText.place(x=160,y=190,width=77,height=39)
        
        #passeord entry
        PasswordString = tk.StringVar()
        PasswordEntryBox=tk.Entry(win,textvariable = PasswordString,show = "*")
        PasswordEntryBox["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        PasswordEntryBox["font"] = ft
        PasswordEntryBox["text"] = " "
        PasswordEntryBox.place(x=260,y=190,width=260,height=37)

        #button Fetch
        button = tk.Button(win,text = 'Test', command = lambda:Action())
        button.place(x=260,y=350,width=70,height=25)
        ft = tkFont.Font(family='Times',size=13)
        button["font"] = ft        
        button["text"] = "Fetch Emails"
        button.place(x=230,y=260,width=107,height=34)
        
        #back Button
        backButton = tk.Button(win,text = 'Back')
        backButton["command"] = BackfromOfflineToMp2
        backButton.place(x=10,y=40,width=70,height=25)
        
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
            output2 = modal2.predict(df['Emails'])
            if output == 1 or output2 == 1:
                TextBox2.delete('1.0',END)
                TextBox2.insert(END, 'Spam')
            else :
                TextBox2.delete('1.0',END)
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
    mp_Button_Online["command"] = OnlineSpamCheck

    mp_Button_Offline=tk.Button(win)
    ft = tkFont.Font(family='Times',size=10)
    mp_Button_Offline["font"] = ft
    mp_Button_Offline["text"] = "Enter Email "
    mp_Button_Offline.place(x=250,y=190,width=124,height=30)
    mp_Button_Offline["command"] = OfflineSpamCheck


MainPage()
win.mainloop()