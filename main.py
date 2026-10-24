import tkinter as tk
from tkinter import ttk, messagebox

class YurtUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Başkent OSB MTAL Yurt Bilgileri")
        self.root.geometry("380x600")

        self.bugunun_menusu = ["Mercimek Çorbası", "Köfte", "Pirinç Pilavı", "Ayran"]
        self.favori_yemek = "Köfte"

        # Başlık
        title = tk.Label(root, text="Başkent OSB MTAL Yurt", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Menü Kartı
        self.menu_frame = tk.LabelFrame(root, text="Günün Menüsü (Pansiyon)", padding=10)
        self.menu_frame.pack(fill="x", padx=10, pady=5)

        self.menu_label = tk.Label(self.menu_frame, text="", justify="left", font=("Arial", 11))
        self.menu_label.pack(anchor="w")

        # Favori Yemek Girme
        fav_frame = tk.LabelFrame(root, text="En Sevdiğin Yemek", padding=10)
        fav_frame.pack(fill="x", padx=10, pady=5)

        self.fav_entry = tk.Entry(fav_frame, font=("Arial", 11))
        self.fav_entry.insert(0, self.favori_yemek)
        self.fav_entry.pack(fill="x", pady=5)
        
        btn_kaydet = tk.Button(fav_frame, text="Kaydet ve Kontrol Et", command=self.guncelle)
        btn_kaydet.pack()

        self.guncelle()
        # Etüt ve Yemek Ayarları
        etut_frame = tk.LabelFrame(root, text="Etüt ve Yemek Saatleri", padding=10)
        etut_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(etut_frame, text="Kaç dk önce ses uyarısı gelsin?").pack(anchor="w")
        self.etut_combo = ttk.Combobox(etut_frame, values=["5 dk", "10 dk", "15 dk", "20 dk", "25 dk", "30 dk"])
        self.etut_combo.set("10 dk")
        self.etut_combo.pack(fill="x", pady=2)

        tk.Label(etut_frame, text="Geç kalınca ses uyarısı:").pack(anchor="w")
        self.etut_gec_combo = ttk.Combobox(etut_frame, values=["2 dk sonra", "5 dk sonra", "8 dk sonra"])
        self.etut_gec_combo.set("5 dk sonra")
        self.etut_gec_combo.pack(fill="x", pady=2)

        # Okul Saatleri
        okul_frame = tk.LabelFrame(root, text="Okul Saati Ayarları", padding=10)
        okul_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(okul_frame, text="Okuldan önce ses gelsin:").pack(anchor="w")
        self.okul_combo = ttk.Combobox(okul_frame, values=["5 dk", "10 dk", "15 dk", "20 dk", "25 dk", "35 dk", "40 dk"])
        self.okul_combo.set("15 dk")
        self.okul_combo.pack(fill="x", pady=2)

        tk.Label(okul_frame, text="Geç kalınca ses uyarısı:").pack(anchor="w")
        self.okul_gec_combo = ttk.Combobox(okul_frame, values=["2 dk sonra", "5 dk sonra", "10 dk sonra", "15 dk sonra"])
        self.okul_gec_combo.set("5 dk sonra")
        self.okul_gec_combo.pack(fill="x", pady=2)

    def guncelle(self):
        yazilan = self.fav_entry.get().strip()
        metin = "\n".join([f"• {y}" for y in self.bugunun_menusu])
        
        if yazilan and any(yazilan.lower() in y.lower() for y in self.bugunun_menusu):
            metin += f"\n\n🔊 BİLDİRİM: Bugün sevdiğin {yazilan} var!"
            
        self.menu_label.config(text=metin)

if __name__ == "__main__":
    root = tk.Tk()
    app = YurtUygulamasi(root)
    root.mainloop()
