from tkinter import *


class Window:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x300")
        self.root.title("Encrypted Chat")

        self.inputtxt = Text(self.root, height=5,
                             width=25,
                             bg="light yellow")

        self.Output = Text(self.root, height=10,
                           width=25,
                           bg="light cyan", state=DISABLED)

        self.Display = Button(self.root, height=2,
                              width=20,
                              text="Send",
                              command=lambda: self.take_input())
        self.INPUT = None

    def reset_input(self):
        self.INPUT = None

    def get_input(self):
        return self.INPUT

    def take_input(self):
        self.INPUT = self.inputtxt.get("1.0", "end-1c")
        self.Output.configure(state=NORMAL)
        self.Output.insert(END, "You: " + self.INPUT + '\n')
        self.Output.configure(state=DISABLED)
        self.inputtxt.delete('1.0', END)

    def receive_message(self, message):
        self.Output.configure(state=NORMAL)
        self.Output.insert(END, "Them: " + message + '\n')
        self.Output.configure(state=DISABLED)

    def run(self):
        self.inputtxt.pack()
        self.Display.pack()
        self.Output.pack()
