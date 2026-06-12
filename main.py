#Kütüphaneler
import os
import tempfile
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog, messagebox

#Pencere 
root = tk.Tk()
root.title("Furkan's Text Editor")
root.geometry("800x600") 

#Değişkenler ve Kaydırma Çubuğu
is_recovering = False
active_file = None
temp_file = None
temp_file_path = os.path.join(tempfile.gettempdir(), "furkan_editor_temp.txt")
text_area = tk.Text(root, wrap='word')
scrollbar = tk.Scrollbar(root)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
xscrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL) 
text_area.config(xscrollcommand=xscrollbar.set)      
xscrollbar.config(command=text_area.xview)
text_area.pack(expand=1, fill='both')

#Otomatik Kaydetme 
def auto_save(event=None):
    if is_recovering:
        return
    with open(temp_file_path, "w", encoding="utf-8") as f:
        f.write(text_area.get("1.0", tk.END))
text_area.bind('<KeyRelease>', auto_save)

#Çıkış Onayı 
def confirm_exit():
    if os.path.exists(temp_file_path):
        if messagebox.askyesno("Çıkış", "Kaydedilmemiş değişiklikler var. Kaydederek mi çıkmak istersiniz?"):
            save_file()
    root.destroy()

#Dosya İşlemleri 
def new_file():
    global active_file, temp_file
    if text_area.get("1.0", tk.END).strip():
        if messagebox.askyesno("Save Changes", "Yeni bir dosya açmadan önce değişiklikleri kaydetmek ister misiniz?"):
            save_file()
    text_area.delete("1.0", tk.END)
    active_file = None
    temp_file = None
    root.title("Furkan's Text Editor - Yeni Dosya")

def open_file():
    global active_file, temp_file
    if text_area.get("1.0", tk.END).strip():
        if messagebox.askyesno("Save Changes", "Yeni bir dosya açmadan önce değişiklikleri kaydetmek ister misiniz?"):
            save_file()
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.fk"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                icerik = file.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='windows-1254') as file:
                icerik = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, icerik)
        active_file = file_path
        temp_file = None
        root.title(f"Furkan's Text Editor - {os.path.basename(active_file)}")

def save_file():
    global active_file, temp_file
    if active_file:
        with open(active_file, 'w') as file:
            file.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Dosya Kaydedildi", "Dosya başarıyla kaydedildi.")
    else:
        save_as_file()
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)

def save_as_file():
    global active_file, temp_file
    file_path = filedialog.asksaveasfilename(defaultextension=".fk", filetypes=[("Text Files", "*.fk"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get("1.0", tk.END))
        active_file = file_path
        temp_file = None
        root.title(f"Furkan's Text Editor - {os.path.basename(active_file)}")
        messagebox.showinfo("Dosya Kaydedildi", "Dosya başarıyla kaydedildi.")
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            
def delete_file():
    global active_file, temp_file
    if active_file:
        confirm = messagebox.askyesno("Dosyayı Sil", f"'{os.path.basename(active_file)}' dosyası bilgisayardan KALICI olarak silinecektir.\nEmin misiniz?")
        if confirm: 
            try:
                os.remove(active_file)
                text_area.delete("1.0", tk.END) 
                active_file = None              
                temp_file = None               
                root.title("Furkan's Text Editor") 
                messagebox.showinfo("Başarılı", "Dosya başarıyla silindi.")
            except Exception as e:
                messagebox.showerror("Hata", f"Dosya silinirken bir hata oluştu:\n{e}")
    else:
        messagebox.showwarning("Uyarı", "Silinecek kayıtlı bir dosya bulunamadı. Ekranı temizlemek için 'Yeni Dosya' seçeneğini kullanabilirsiniz.")

#Tema Fonksiyonları ve Font Ayarları
def dark_theme():
    text_area.config(bg="#1e1e1e", fg="#ffffff", insertbackground="white")

def light_theme():
    text_area.config(bg="#ffffff", fg="#000000", insertbackground="black")

def font_size(size):
    current_font = text_area.cget("font").split(" ")[0]
    text_area.config(font=("Arial", size))

#Kısayol Tuşları
root.bind('<F1>', lambda event: open_file())
root.bind('<F2>', lambda event: auto_save())
root.bind('<F3>', lambda event: save_file())
root.bind('<F4>', lambda event: delete_file())
root.bind('<F5>', lambda event: confirm_exit())


#Menü Çubuğu,Tema ve Ayarlar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Dosya", menu=file_menu)
file_menu.add_command(label="Yeni Dosya", command=new_file)
file_menu.add_command(label="Aç", command=open_file)
file_menu.add_command(label="Kaydet", command=save_file)
file_menu.add_command(label="Farklı Kaydet", command=save_as_file)
file_menu.add_command(label="Dosyayı Sil", command=delete_file)
file_menu.add_separator()
file_menu.add_command(label="Çıkış", command=confirm_exit) 
root.config(menu=menu_bar)


theme_menu = tk.Menu(menu_bar, tearoff=0)
theme_menu.add_command(label="Karanlık Tema (Siyah)", command=dark_theme)
theme_menu.add_command(label="Aydınlık Tema (Beyaz)", command=light_theme)
menu_bar.add_cascade(label="Tema", menu=theme_menu)

size_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ayarlar", menu=settings_menu)
size_menu = tk.Menu(settings_menu, tearoff=0)
size_menu.add_command(label="10", command=lambda: font_size(10))
size_menu.add_command(label="14", command=lambda: font_size(14))
size_menu.add_command(label="18", command=lambda: font_size(18))
size_menu.add_command(label="22", command=lambda: font_size(22))
size_menu.add_command(label="26", command=lambda: font_size(26))
settings_menu.add_cascade(label="Font Boyutu", menu=size_menu)

settings_menu.add_command(label="Kısayol Tuşları", command=lambda: messagebox.showinfo("Kısayol Tuşları", "F1: Dosya Aç\nF2: Otomatik Kaydet\nF3: Kaydet\nF4: Dosyayı Sil\nF5: Çıkış"))

#Pencere Kapatma ve Oturum Kurtarma
root.protocol("WM_DELETE_WINDOW", confirm_exit)
if os.path.exists(temp_file_path):
    is_recovering = True 
    with open(temp_file_path, "r", encoding="utf-8") as f:
        recovered_data = f.read()
    if recovered_data.strip():
        text_area.insert("1.0", recovered_data)
        messagebox.showinfo("Kurtarma", "Önceki oturumdan kalan veriler yüklendi.")
    is_recovering = False 
    os.remove(temp_file_path)

root.mainloop()