from re import A
import tkinter as tk

root = tk.Tk()
root.title("Need Help?")
root.geometry('540x200')

A_ = tk.Label(root, text=r'The Following Directions Will Convert CA Certificates into .PEM Files:', font= ('Arial 10 underline'))
A_.pack()

B_ = tk.Label(root, text=r'')
B_.pack()

A = tk.Label(root, text=r'1. Click the CA Certificate you have')
A.pack()

B = tk.Label(root, text=r'2. Right-Click the CA Certificate you have on your computer')
B.pack()

B2 = tk.Label(root, text=r'3. Copy the Path ex: "C:\Users\name\Desktop\user.crt"')
B2.pack()

C = tk.Label(root, text=r'4. Paste the Path into the Text Box and click "Enter Path"')
C.pack()

D = tk.Label(root, text=r'5. Click "Run Command Prompt')
D.pack()

E = tk.Label(root, text=r'6. The .PEM Certificate will be created to the same path as the initial CA')
E.pack()

root.mainloop()