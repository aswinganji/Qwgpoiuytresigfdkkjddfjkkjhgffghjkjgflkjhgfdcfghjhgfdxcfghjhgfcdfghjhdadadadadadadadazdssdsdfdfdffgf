from tkinter import*
import random
root = Tk()
root.title("Warp Drive")
root.geometry("500x500")

root.configure(background = "gold")


listi = ["bottle" , "lunch","pencil","box","book1","book2","book3","book4","plant"]
secre = Label(root,bg = "gold")
pointy = Label(root , bg = "gold")


def wer():
    secre["text"]="Thingi " + str(listi)
    pointya = random.sample(range(0,8),1)
    pointy["text"]= "Wiki = " + str(pointya)
    
btn = Button(root,text="Click To Preview", command = wer, bg = "gold")


secre.pack()
pointy.pack()
btn.pack()

root.mainloop()

    
   
    