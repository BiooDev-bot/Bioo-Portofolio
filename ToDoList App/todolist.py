import tkinter as tk
from tkinter import messagebox, ttk
import json

def simpan_tugas():
    with open("tugas.json", "w") as file:
        json.dump(tugas_list, file)

def muat_tugas():
    global tugas_list
    try:
        with open("tugas.json", "r") as file:
            tugas_list = json.load(file)
            tugas_list.sort()
            tugas.delete(0, tk.END)
            for t in tugas_list:
                tugas.insert(tk.END, f"{t[0]} - {t[1]}")
    except FileNotFoundError:
        tugas_list = []

def pindah_ke_aktivitas(event):
    entry_aktivitas.focus_set()

def tambah_tugas(event=None):
    waktu = entry_waktu.get()
    aktivitas = entry_aktivitas.get()
    if waktu and aktivitas:
        tugas_list.append((waktu, aktivitas))
        tugas_list.sort()
        tugas.delete(0, tk.END)
        for t in tugas_list:
            tugas.insert(tk.END, f"{t[0]} - {t[1]}")
        entry_waktu.delete(0, tk.END)
        entry_aktivitas.delete(0, tk.END)
        entry_waktu.focus_set()
        simpan_tugas()
    else:
        messagebox.showwarning("Peringatan", "Mohon isi waktu dan aktivitas")

def hapus_tugas(event=None):
    try:
        selected_index = tugas.curselection()[0]
        del tugas_list[selected_index]
        tugas.delete(selected_index)
        simpan_tugas()
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus")

def keluar(event=None):
    simpan_tugas()
    root.quit()

def pindah_ke_atas(event):
    index = tugas.curselection()
    if index and index[0] > 0:
        tugas.selection_clear(0, tk.END)
        tugas.selection_set(index[0] - 1)
        tugas.activate(index[0] - 1)

def pindah_ke_bawah(event):
    index = tugas.curselection()
    if index and index[0] < tugas.size() - 1:
        tugas.selection_clear(0, tk.END)
        tugas.selection_set(index[0] + 1)
        tugas.activate(index[0] + 1)

root = tk.Tk()
root.title("ToDoList App")
root.geometry("400x500+400+90")
root.config(bg="#E3F2FD")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)

ttk.Label(root, text="ToDoList App", font=("Arial", 18, "bold"), background="#E3F2FD", foreground="#01579B").pack(pady=10)

frame_input = ttk.Frame(root)
frame_input.pack(pady=10)

ttk.Label(frame_input, text="Waktu:").grid(row=0, column=0, padx=5, pady=5)
entry_waktu = ttk.Entry(frame_input)
entry_waktu.grid(row=0, column=1, padx=5, pady=5)
entry_waktu.bind('<Return>', pindah_ke_aktivitas)

ttk.Label(frame_input, text="Aktivitas:").grid(row=1, column=0, padx=5, pady=5)
entry_aktivitas = ttk.Entry(frame_input)
entry_aktivitas.grid(row=1, column=1, padx=5, pady=5)

ttk.Button(root, text="Tambah", command=tambah_tugas).pack(pady=5)

frame_list = ttk.Frame(root)
frame_list.pack(pady=10)

tugas = tk.Listbox(frame_list, width=40, height=10, bg="#FFFFFF", font=("Arial", 10))
tugas.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = ttk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tugas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tugas.yview)

muat_tugas()

ttk.Button(root, text="Hapus", command=hapus_tugas).pack(pady=5)

ttk.Button(root, text="Keluar", command=keluar).pack(pady=5)

root.bind('<Return>', tambah_tugas)
root.bind('<Delete>', hapus_tugas)
root.bind('<Escape>', keluar)
root.bind('<Prior>', pindah_ke_atas)
root.bind('<Next>', pindah_ke_bawah)

root.mainloop()