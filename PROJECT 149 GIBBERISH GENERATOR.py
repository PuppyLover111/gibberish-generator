from tkinter import*
import random

root=Tk()
root.geometry("500x500")
root.configure(bg='teal')
root.title("WHAT COULD IT BE?!?!")

ppl=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def find():
    P1=random.randint(0,25)
    P2=random.randint(0,25)
    P3=random.randint(0,25)
    P4=random.randint(0,25)
    P5=random.randint(0,25)
    c1=ppl[P1]
    c2=ppl[P2]
    c3=ppl[P3]
    c4=ppl[P4]
    c5=ppl[P5]

    character=c1+c2+c3+c4+c5
    print(character)

btn=Button(root,text="GENERATE SOME GIBBERISH",command=find)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()