from tkinter import *
import customtkinter
import socket

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

root_tk = customtkinter.CTk()
root_tk.geometry("400x480")
root_tk.title("Whats my TCP/IP Info?")

# Widgets
frame_1 = customtkinter.CTkFrame(master=root_tk, corner_radius=15)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

my_text = Text(frame_1, height=16, width=22)
my_text.configure(font =("Courier", 14))
my_text.place(relx=.06, rely=.15)

# Widget Functions
def clear_all():
    my_text.config(state='normal')
    my_text.delete("1.0","end")
    my_text.config(state=DISABLED)


def get_ip_info():
    my_text.config(state='normal')
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    total_text = f'Your Computer Name:\n{hostname}\n\nYour IP Address:\n{IPAddr}'
    my_text.insert(END, total_text)
    my_text.config(state=DISABLED)

# More widgets
button_1 = customtkinter.CTkButton(master=frame_1,command=get_ip_info, text= 'Run')
button_1.grid(pady=20, padx=10, column=0, row=0)

clear_button = customtkinter.CTkButton(master=frame_1, 
                                        command=clear_all, 
                                        fg_color='#ba1f1c', 
                                        hover_color='#d62824', 
                                        text='Clear')

clear_button.grid(pady=20, padx=10, column=1, row=0)


root_tk.mainloop()