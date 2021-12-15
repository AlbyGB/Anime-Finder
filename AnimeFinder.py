import requests
import tkinter as tk
from tkinter import filedialog as fd
import threading

#create another thread to avoid blocking the GUI
def selec_file_thread():
  threading.Thread(target=selec_file).start()

def selec_file():
  immagine = fd.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

  if not immagine:
    return

  request = requests.post("https://api.trace.moe/search",
    data=open(immagine, "rb").read(),
    headers={"Content-Type": "image/jpeg"}
  ).json()
  
  T.config(state=tk.NORMAL)
  T.delete(1.0, tk.END)
  for key, value in request["result"][0].items():
    T.insert(tk.END, f"{key}: {value}\n\n")

  T.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Anime Finder")
root.geometry("500x500")
root.resizable(False, False)
root.iconbitmap(r"C:\Users\Drako\Desktop\Anime.ico")
bottone = tk.Button(root, text="Select file", command=selec_file_thread, bg="#4860cb", fg="white", activebackground="#263887", activeforeground="white", highlightthickness=0, bd=0, relief = tk.SUNKEN)
bottone.pack(fill=tk.X)

T = tk.Text(root, height=250, width=500, bg="#363940", fg="white", font=("Arial", 12))
T.config(state=tk.DISABLED)
T.pack()

root.mainloop()