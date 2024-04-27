import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GUI Application")
        
    def run(self):
        self.window.mainloop()
        
    def add_label(self, text):
        label = tk.Label(self.window, text=text)
        label.pack()
        
    def add_button(self, text, command):
        button = tk.Button(self.window, text=text, command=command)
        button.pack()
        
    def add_entry(self):
        entry = tk.Entry(self.window)
        entry.pack()

if __name__ == "__main__":
    '''
    if main is for testing purposes.\n
    use it to show how to use your code.\n
    '''
    gui = GUI()
    gui.add_label("Hello, World!")
    gui.add_button("Click me", lambda: print("Button clicked!"))
    gui.add_entry()
    gui.run()