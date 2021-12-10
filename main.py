import tkinter



def novo():
    text_area.delete(1.0, "end")



def salvar():
    texto = text_area.get(1.0, "end")
    file = open('notepad.txt', 'w')
    file.write(texto)
    file.close()

def abrir():
    file = open('notepad.txt', 'r')
    texto = file.read()
    text_area.insert(1.0, texto)

def salvar_como():
    print('Salva o arquivo em um lugar')

def updateFont():
    size = spin_size.get()
    font = spin_font.get()
    text_area.config(font="{} {}".format(font, size))



window = tkinter.Tk()
window.title("Notepad")
window.geometry("1280x720")

frame = tkinter.Frame(window, height=30)
frame.pack(fill="x")

font_text = tkinter.Label(frame, text=" Font: ")
font_text.pack(side="left")

spin_font = tkinter.Spinbox(frame, values=("Arial", "Verdana"))
spin_font.pack(side="left")

font_size = tkinter.Label(frame, text=" Font Size: ")
font_size.pack(side="left")

spin_size = tkinter.Spinbox(frame, values=(50,55,60,65,70,75,80))
spin_size.pack(side="left")

button_update = tkinter.Button(frame, text="UP", command= updateFont)
button_update.pack(side="left")


text_area = tkinter.Text(window, font="Arial 20 bold", width=1280, height=720)
text_area.pack()


#Cria o menu
main_menu = tkinter.Menu(window)

file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="Novo", command=novo)
file_menu.add_command(label="Salvar", command=salvar)
file_menu.add_command(label="Salvar Como...", command=salvar_como)
file_menu.add_command(label="Abrir", command=abrir)
file_menu.add_command(label="Sair", command=window.quit)

main_menu.add_cascade(label="File", menu=file_menu)
window.configure(menu=main_menu)



window.mainloop()

