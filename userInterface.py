from tkinter import *

class Window:
    
    def __init__(self):
        root = Tk()
        root.geometry("300x300")
        root.title("Encrypted Chat")
        
        self.inputtxt = Text(root, height = 10,
            width = 25,
            bg = "light yellow")

        self.Output = Text(root, height = 5,
                width = 25,
                bg = "light cyan")

        self.Display = Button(root, height = 2,
                    width = 20,
                    text ="Send",
                    command = lambda:self.Take_input())
            
    def Take_input(self):
        INPUT = self.inputtxt.get("1.0", "end-1c")
        self.Output.insert(END, INPUT)
        
    def run(self):
        self.inputtxt.pack()
        self.Display.pack()
        self.Output.pack()

        mainloop()


