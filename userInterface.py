from tkinter import *


class InputWindow:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x150")
        self.root.title("Encrypted Chat")

        self.portLabel = Label(self.root, text="Port")
        self.portEntry = Entry(self.root)

        self.ipLabel = Label(self.root, text="IP Adress")
        self.ipEntry = Entry(self.root)

        self.button = Button(self.root, command=lambda: self.validate(), text="Connect")

        self.EXIT = False

        self.port = ""
        self.ipadress = ""

    def validate(self):
        self.EXIT = True
        self.port, self.ipadress = self.portEntry.get(), self.ipEntry.get()

    def run(self):
        self.portLabel.pack()
        self.portEntry.pack()
        self.ipLabel.pack()
        self.ipEntry.pack()

        self.button.pack()

        while not self.EXIT:
            self.root.update_idletasks()
            self.root.update()


class Window:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x300")
        self.root.title("Encrypted Chat")
        self.root.protocol("WN_DELETE_WINDOW", self.exit_window)

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

        self.EXIT = False

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

    def exit_window(self):
        self.EXIT = True

    def run(self):
        self.inputtxt.pack()
        self.Display.pack()
        self.Output.pack()
