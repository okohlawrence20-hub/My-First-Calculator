import customtkinter as ctk

calculator = ctk.CTk()

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

calculator.title ("My_first_calculate")

calculator.geometry("400x500")

button_entry = ctk.CTkLabel(calculator, text="", )
button_entry.pack(pady=40)

cal_frame = ctk.CTkFrame(calculator, corner_radius=5)
cal_frame.pack(pady=10, padx=5)

for i in range (5):
        cal_frame.rowconfigure(i, weight = 1 )
        
for g in range (5):
        cal_frame.columnconfigure(g, weight = 1)
def delete():
        current = button_entry.cget("text")
        new_num = current[:-1]
        button_entry.configure(text=new_num)

def button_clicked(num):
               current = button_entry.cget("text")
               button_entry.configure(text=current + str(num), font=("Arial", 20))

def clear():
        button_entry.configure(text="")
      
def calculate():
        try:
            see_num = button_entry.cget("text")

            num1= ""
            result = 0

            operation = "+"

            for i in see_num:
                    if i.isdigit() or i == ".":
                            num1 += i

                    else:
                        if num1:
                            if operation == "+":
                                result += float(num1)
                            elif operation == "−":
                                    result -= float(num1)  
                            elif operation == "×":
                                        result *= float(num1)

                            elif operation == "÷":
                                    result  /= float(num1)
                            elif operation == "%":
                                result  = float (num1) / 100
                   
                        num1 = ""
                        operation = i

            if num1:
                    if operation == "+":
                            result += float(num1)
                    elif operation == "−":
                            result -= float(num1)

                    elif operation == "×":
                            result *= float(num1)

                    elif operation == "÷":
                            result  /= float(num1)
                    
                    elif operation == "%":
                            result  = float (num1) /100
                    button_entry.configure(text=str(result))
        except:
               button_entry.configure(text="Error")

            
del_button = ctk.CTkButton(cal_frame, text="⌫", height=60, width=60, corner_radius=30, command=delete,  fg_color="#000000")
del_button.grid(pady=5, padx=5, row=0, column=0, sticky="nsew")

clear_button = ctk.CTkButton(cal_frame, text="AC", height=60, width=60, corner_radius=30,  fg_color="#000000", command= clear )
clear_button.grid(pady=5, padx=5, row=0, column=1, sticky="nsew")

divide_button= ctk.CTkButton(cal_frame, text="÷", height=60, width=60, corner_radius=30, command= lambda: button_clicked("÷"))
divide_button.grid(pady=5, padx=5, row=0, column=2, sticky="nsew")


button_7 = ctk.CTkButton(cal_frame, text="7", height=60, width=60, corner_radius=30,command= lambda: button_clicked(7), fg_color="#000000")
button_7.grid(pady=5, padx=5, row=1, column=0, sticky="nsew")

button_8 = ctk.CTkButton(cal_frame, text="8", height=60, width=60, corner_radius=30, command =lambda: button_clicked(8),  fg_color="#000000")
button_8.grid(pady=5, padx=5, row=1, column=1, sticky="nsew")

button_9 = ctk.CTkButton(cal_frame, text="9", height=60, width=60, corner_radius=30,command= lambda: button_clicked(9),  fg_color="#000000")
button_9.grid(pady=5, padx=5, row=1, column=2, sticky="nsew")

multiply_button = ctk.CTkButton(cal_frame, text="×", height=60, width=60, corner_radius=30, command =lambda: button_clicked("×"))
multiply_button.grid(pady=5, padx=5, row=1, column=3, sticky="nsew")

button_4 = ctk.CTkButton(cal_frame, text="4", height=60, width=60, corner_radius=30, command =lambda: button_clicked(4),  fg_color="#000000")
button_4.grid(pady=5, padx=5, row=2, column=0, sticky="nsew")

button_5 = ctk.CTkButton(cal_frame, text="5", height=60, width=60, corner_radius=30, command =lambda: button_clicked(5),  fg_color="#000000")
button_5.grid(pady=5, padx=5, row=2, column=1, sticky="nsew")

button_6 = ctk.CTkButton(cal_frame, text="6", height=60, width=60, corner_radius=30,  command =lambda: button_clicked(6),  fg_color="#000000")
button_6.grid(pady=5, padx=5, row=2, column=2, sticky="nsew")

minus_button = ctk.CTkButton(cal_frame, text="−", height=60, width=60, corner_radius=30, command =lambda: button_clicked("−"))
minus_button.grid(pady=5, padx=5, row=2, column=3, sticky="nsew")

button_1 = ctk.CTkButton(cal_frame, text="1", height=60, width=60, corner_radius=30, command =lambda: button_clicked(1),  fg_color="#000000")
button_1.grid(pady=5, padx=5, row=3, column=0, sticky="nsew")

button_2 = ctk.CTkButton(cal_frame, text="2", height=60, width=60, corner_radius=30, command =lambda: button_clicked(2),  fg_color="#000000")
button_2.grid(pady=5, padx=5, row=3, column=1, sticky="nsew")

button_3 = ctk.CTkButton(cal_frame, text="3", height=60, width=60, corner_radius=30 , command =lambda: button_clicked(3),  fg_color="#000000")
button_3.grid(pady=5, padx=3, row=3, column=2, sticky="nsew")

add_button = ctk.CTkButton(cal_frame, text="+", height=60, width=60, corner_radius=30, command =lambda: button_clicked("+") )
add_button.grid(pady=5, padx=5, row=3, column=3, sticky="nsew")

button_c = ctk.CTkButton(cal_frame, text="%", height=60, width=60, corner_radius=30, fg_color="#000000", command= lambda: button_clicked("%"))
button_c.grid(pady=5, padx=5, row=4, column=0, sticky="nsew")

button_0 = ctk.CTkButton(cal_frame, text="0", height=60, width=60, corner_radius=30, command =lambda: button_clicked(0),  fg_color="#000000")
button_0.grid(pady=5, padx=5, row=4, column=1, sticky="nsew")

decimal_button = ctk.CTkButton(cal_frame, text=".", height=60, width=60, corner_radius=30,command =lambda: button_clicked("."),  fg_color="#000000")
decimal_button.grid(pady=5, padx=5, row=4, column=2, sticky="nsew")

equal_button = ctk.CTkButton(cal_frame, text="=", height=60, width=60, corner_radius=30, command = calculate)
equal_button.grid(pady=(5,10), padx=5, row=4, column=3, sticky="nsew")

calculator.mainloop()

