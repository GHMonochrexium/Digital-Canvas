import tkinter as tk
screen = tk.Tk()
screen.configure(bg="light grey")
screen.title("Digital Canvas")
screen.geometry("1000x1000")

pencolour = "black"
pensize = 25
def ChangePenColour():
    global pensize,pencolour,colours
    x=list1.curselection()
    if x:
        selectedcolour = colours[x[0]]
        print(selectedcolour)
        pencolour = selectedcolour

canvas1 = tk.Canvas(width=1000,height=800)
canvas1.place(x=0,y=200)

pen = tk.Button(text="Pen",font=("Arial",18), fg="black",bg="lightblue",width=5,height=1,command=ChangePenColour)
pen.place(x=30,y=100)

brush = tk.Button(text="Brush",font=("Arial",18), fg="black",bg="lightblue",width=5,height=1)
brush.place(x=150,y=100)

eraser = tk.Button(text="Eraser",font=("Arial",18), fg="black",bg="lightblue",width=5,height=1)
eraser.place(x=270,y=100)
colours = ["red","orange","yellow","green","blue","purple","pink","black","grey","brown","indigo","lavender"]
list1 = tk.Listbox(width=30,height=10)
list1.place(x=400,y=20)

l1 = tk.Label(text="Enter your brush/pen size",font=("Arial",16), fg="black" ,bg="lightgrey",width=30,height=2)
l1.place(x=600,y=20)

s1 = tk.Scale(from_=1,to=100,length=300,orient=tk.HORIZONTAL)
s1.place(x=600,y=100)
for i in colours:
    list1.insert(tk.END, i)
screen.mainloop()
