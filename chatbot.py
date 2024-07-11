from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   #pip install pillow

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("740x630+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open('chatbot.png')
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='black',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',15,'bold'),width=8,bg='light green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),width=8,bg='orange',fg='black')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label2=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label2.grid(row=1,column=1,padx=5,sticky=W)

    #============================================ Funcion declare=======================================================
        
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
        
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='Please enter some input'
            self.label2.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label2.config(text=self.msg,fg='red')

        if(self.entry.get()=="hello"):
            self.text.insert(END,'\n\n'+"Bot: Hi there! How can I assist you today?")

        elif(self.entry.get()=="hi"):
            self.text.insert(END,'\n\n'+"Bot: hello")

        elif (self.entry.get()=="how are you"):
            self.text.insert(END,'\n\n'+"Bot: fine and you")

        elif(self.entry.get()=="kesa hae"):
            self.text.insert(END,'\n\n'+"Bot: Bdya aap batao")

        elif (self.entry.get()=='fine'):
            self.text.insert(END,'\n\n'+"Bot: Nice to hear")

        elif (self.entry.get()=="who create you"):
            self.text.insert(END,'\n\n'+"Bot: pradeep")

        elif (self.entry.get()=="what is your name"):
            self.text.insert(END,'\n\n'+'Bot: my name is smart Bot')

        elif (self.entry.get()=='How do I reset my password?'):
            self.text.insert(END,'\n\n'+"Bot: To reset your password,\n go to website and click on the 'Forgot Password' link.\n Follow the instructions sent to your email to reset it.")

        elif (self.entry.get()=='How was your day'):
            self.text.insert(END,'\n\n'+"Bot: I'm just a computer program,\n but I'm here and ready to help you!\n How can I assist you today?")
        
        elif (self.entry.get()=='What are your hobbies?'):
            self.text.insert(END,'\n\n'+"Bot: I don't have hobbies, \nbut I'm here to help you with any questions you may have.\n Is there something specific on your mind")

        elif (self.entry.get()=='Tell me a joke.'):
            self.text.insert(END,'\n\n'+'Bot: you are intelligent and smart')

        elif (self.entry.get()=='What is artificial intelligence'):
            self.text.insert(END,'\n\n'+'Bot: Artificial intelligence (AI)\n refers to the simulation \nof human intelligence in machines,\n allowing them to perform tasks that typically require human intelligence,\n such as learning and problem-solving.')

        elif (self.entry.get()=='can you speak hindi'):
            self.text.insert(END,'\n\n'+'Bot: im still learning it..')

        elif (self.entry.get()=='what is machine learning'):
            self.text.insert(END,'\n\n'+"Bot: Machine learning (ML) is a subfield\n of artificial intelligence (AI)\nthat focuses on the\n development of algorithms\n and models that enable\n computers to learn from and make predictions\n or decisions based on data.")

        elif (self.entry.get()=="how does face recognition work"):
            self.text.insert(END,'\n\n'+"Bot: The process typically involves the following key steps:Face Detection,Feature Extraction,Face Representation,Database Comparison,Matching Algorithm,Decision Making")

        elif (self.entry.get()=="what is chatbot"):
            self.text.insert(END,'\n\n'+"Bot: A chatbot is a computer program designed to simulate conversation with human users, especially over the internet.")

        elif (self.entry.get()=='what is python programming'):
            self.text.insert(END,'\n\n'+"Bot: Python is a high-level,\n versatile programming language \nknown for its readability\n and ease of use.\n It was created by Guido van Rossum \nand first released in 1991.\n Python supports multiple programming paradigms,\n including procedural,\n object-oriented, \nand functional programming,\n making it suitable for a wide range of applications")

        elif (self.entry.get()=="what is programming language"):
            self.text.insert(END,'\n\n'+'Bot: A programming language is a formal \nset of rules and instructions \nused to create computer programs\n or software.')

        elif (self.entry.get()=='who is your owner'):
            self.text.insert(END,'\n\n'+'Bot: pradeep is my owner')

        elif (self.entry.get()=='what is your identity'):
            self.text.insert(END,'\n\n'+'Bot: i am a software develop \nfor some specific purpose')

        elif (self.entry.get()=='good morning'):
            self.text.insert(END,'\n\n'+'Bot: good morning sir')

        elif (self.entry.get()=='what is your favourate color'):
            self.text.insert(END,'\n\n'+'Bot: i like every color')

        elif (self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: Thank you for chatting')

        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I didn't get it")





if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()

