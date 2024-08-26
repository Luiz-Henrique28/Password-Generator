import customtkinter
import pyperclip
from passwordGenerator import generatorPassword

def update_char_count(value):
    char_count_label.configure(text=f"{int(value)}")

def updatePassword():
    newPassword = generatorPassword(check_var1, check_var2, check_var3, char_count_label)
    fieldPassword.delete(0, customtkinter.END)
    fieldPassword.insert(0, newPassword)

def clipPasswor():
    pyperclip.copy(fieldPassword.get())

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = customtkinter.CTk()

    app.title("Password Generator")
    app.geometry("350x400")

    frame = customtkinter.CTkFrame(app, corner_radius=15)
    frame.pack(pady=20, padx=20, fill="x")

    # Password Field
    fieldPassword = customtkinter.CTkEntry(frame)
    fieldPassword.pack(side="left", padx=5, pady=10, fill="x", expand=True)

    # btn 1
    btnCopy = customtkinter.CTkButton(frame, text="copy", width=30,
                                      command= clipPasswor)
    btnCopy.pack(side="left", padx=5)

    # btn 2
    btnResetPassword = customtkinter.CTkButton(frame, text="refresh", width=30,
                                               command= updatePassword)
    btnResetPassword.pack(side="left", padx=5)

    frame2 = customtkinter.CTkFrame(app, corner_radius=15)
    frame2.pack(padx=20, fill="x")

    frame2.grid_rowconfigure(0, weight=1)  
    frame2.grid_rowconfigure(1, weight=1)
    frame2.grid_rowconfigure(2, weight=1)
    frame2.grid_rowconfigure(3, weight=1)
    frame2.grid_rowconfigure(4, weight=1)
    frame2.grid_rowconfigure(5, weight=1)
    frame2.grid_columnconfigure(0, weight=1)
    frame2.grid_columnconfigure(1, weight=1)  
    frame2.grid_columnconfigure(2, weight=1)  
    frame2.grid_columnconfigure(3, weight=1) 
    frame2.grid_columnconfigure(4, weight=1)
    frame2.grid_columnconfigure(5, weight=1)

    # Frame Title
    title_label = customtkinter.CTkLabel(frame2, text="Personalize sua senha", font=("Arial", 20))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Slide bar title
    title_label = customtkinter.CTkLabel(frame2, text="Número de caracteres", font=("Arial", 14))
    title_label.grid(row=1, column=0, sticky="w", padx=10)

    # Slide bar
    char_slider = customtkinter.CTkSlider(frame2, from_=5, to=20, number_of_steps=15,
                                            command=lambda value: update_char_count(value))
    char_slider.grid(row=2, column=0, padx=10, sticky="ew")
    char_slider.set(12)

    char_slider.bind("<ButtonRelease-1>", lambda event: updatePassword())

    # label with value of Slide bar
    char_count_label = customtkinter.CTkLabel(frame2, text="12", width=50)
    char_count_label.grid(row=2, column=1, padx=10)

    # check box 
    check_var1 = customtkinter.StringVar(value="on")
    checkboxOfUpperCase = customtkinter.CTkCheckBox(frame2, text="Letra Maiúscula",
                                            command= updatePassword,
                                            variable=check_var1, onvalue="on", offvalue="off")
    checkboxOfUpperCase.grid(row=3, column=0, padx=10, pady=8, sticky="ew")

    check_var2 = customtkinter.StringVar(value="on")
    checkboxOfNumbers = customtkinter.CTkCheckBox(frame2, text="Números",
                                            command= updatePassword,
                                            variable=check_var2, onvalue="on", offvalue="off")
    checkboxOfNumbers.grid(row=4, column=0, padx=10,  pady=0, sticky="ew")

    check_var3 = customtkinter.StringVar(value="on")
    checkboxOfSymbols = customtkinter.CTkCheckBox(frame2, text="Símbolos",
                                            command= updatePassword,
                                            variable=check_var3, onvalue="on", offvalue="off")
    checkboxOfSymbols.grid(row=5, column=0, padx=10, pady=8, sticky="ew")

    # Copy Btn
    mainButton = customtkinter.CTkButton(app, text="Copiar Senha",
                                         command= clipPasswor)
    mainButton.pack(pady=20)

    updatePassword()
    app.mainloop()
