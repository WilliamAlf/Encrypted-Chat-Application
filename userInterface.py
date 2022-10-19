from tkinter import *


class Window:

    def __init__(self):
        root = Tk()
        root.geometry("300x300")
        root.title("Encrypted Chat")

        self.inputtxt = Text(root, height=10,
                             width=25,
                             bg="light yellow")

        self.Output = Text(root, height=5,
                           width=25,
                           bg="light cyan", state=DISABLED)

        self.Display = Button(root, height=2,
                              width=20,
                              text="Send",
                              command=lambda: self.take_input())

    def take_input(self):
        self.INPUT = self.inputtxt.get("1.0", "end-1c")
        self.Output.configure(state=NORMAL)
        self.Output.insert(END, self.INPUT)
        self.Output.configure(state=DISABLED)
        self.inputtxt.delete('1.0', END)

    def run(self):
        self.inputtxt.pack()
        self.Display.pack()
        self.Output.pack()

        mainloop()
