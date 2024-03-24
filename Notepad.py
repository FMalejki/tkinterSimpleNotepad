import tkinter as tk


def msgbox(msg):
    window = tk.Tk()
    window.wm_withdraw()
    tk.messagebox.showinfo(title = "Informacja",message=msg)
    window.destroy()
    return None
def OPEN():
    filepath = tk.filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not filepath:
        return
    EditorField.delete(1.0,tk.END)
    with open(filepath,mode="r",encoding="utf-8") as file:
        text = file.read()
        EditorField.insert(tk.END,text)
    window.title(f"Uniwersalny notatnik - {filepath}")


def SAVEAS():
    filepath = tk.filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not filepath:
        return
    with open(filepath,mode="w",encoding="utf-8") as file:
        text = EditorField.get(1.0,tk.END)
        file.write(text)

    window.title(f"Uniwersalny notatnik - {filepath}")

def SAVE():
    txt = window.title()
    if txt.find("-") == -1:
        SAVEAS()
        return
    else:
        filepath = txt[txt.find("-")+2:len(txt)]
        with open(filepath, mode="w", encoding="utf-8") as file:
            text = EditorField.get(1.0, tk.END)
            file.write(text)
        msgbox("Zapisano!")

def ADD():
    value = FontSize["text"]
    FontSize["text"] = f"{int(value)+1}"
    EditorField.config(font=("Arial", int(value)+1))


def SUB():
    value = FontSize["text"]
    if int(value) >= 2:
        FontSize["text"] = f"{int(value)-1}"
        EditorField.config(font=("Arial", int(value) - 1))
    else:
        msgbox("Debilu jaka czcionka równa 0?!")


window = tk.Tk()
window.title("Uniwersalny notatnik")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)


EditorField = tk.Text(
    background="white",
    font=("Arial",15)
)
ContainerButtons = tk.Frame(
    relief=tk.RAISED,
    background="white",
    bd = 2
)
ContainerFontSize = tk.Frame(
    master=ContainerButtons,
    background="white",
    relief=tk.RAISED
)
ButtonPlus = tk.Button(
    background="white",
    master = ContainerFontSize,
    text = "+",
    command=ADD
)
ButtonMinus = tk.Button(
    background="white",
    master = ContainerFontSize,
    text = "-",
    command=SUB
)
FontSizeTitle = tk.Label(
    master = ContainerButtons,
    background="white",
    text = " ROZMIAR CZCIONKI ",
    font = ('Arial',10,'bold')
)
FontSize = tk.Label(
    master = ContainerFontSize,
    background="white",
    text = "15"
)
OpenButton = tk.Button(
    master = ContainerButtons,
    background="white",
    text = "Otwórz",
    command = OPEN,
    font = ("Arial", 10)
)
SaveAsButton = tk.Button(
    master = ContainerButtons,
    background="white",
    text = "Zapisz jako...",
    command = SAVEAS,
    font = ("Arial", 10)
)
SaveButton = tk.Button(
    master = ContainerButtons,
    background="white",
    text="Zapisz",
    command=SAVE,
    font=("Arial",10)
)
ButtonMinus.grid(row=0,column=0,sticky="ns")
FontSize.grid(row=0,column=1,sticky="nsew")
ButtonPlus.grid(row=0,column=2,sticky="ns")
OpenButton.grid(row = 0, column = 0, sticky = "new",padx=5, pady=5)
SaveAsButton.grid(row = 1, column = 0, sticky = "new",padx=5, pady=5)
SaveButton.grid(row = 2, column = 0, sticky = "new",padx=5, pady=5)
FontSizeTitle.grid(row = 3, column = 0, sticky = "new",padx=5, pady=5)
ContainerFontSize.grid(row = 4, column = 0, sticky = "ns",padx=5, pady=5)
ContainerButtons.grid(row = 0, column = 0, sticky = "nsw")
EditorField.grid(row = 0, column = 1, sticky = "nsew")


window.mainloop()
