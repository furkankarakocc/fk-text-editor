# fk-text-editor

Furkan's Text Editor, Python ve Tkinter kütüphanesi kullanılarak geliştirilmiş, minimalist, kullanıcı dostu ve hafif (lightweight) bir masaüstü metin düzenleyicidir. Günlük notlarınızı tutmak, kod taslakları oluşturmak veya `.fk` uzantılı özel dosyalarınızı yönetmek için ideal bir araçtır.

---

## ✨ Özellikler

* **Gelişmiş Dosya Yönetimi:** Yeni dosya oluşturma, mevcut dosyaları açma, kaydetme, farklı kaydetme ve dosyayı doğrudan sistemden kalıcı olarak silme.
* **🔄 Otokarşılaşma ve Oturum Kurtarma (Crash Recovery):** Siz yazı yazarken arka planda otomatik olarak geçici yedek alınır. Beklenmedik kapanmalarda programı yeniden açtığınızda verileriniz kaybolmaz, otomatik olarak geri yüklenir.
* **🎨 Tema Desteği:** Göz yorgunluğunu azaltmak için tek tıkla **Karanlık Tema (Dark Mode)** ve **Aydınlık Tema (Light Mode)** arasında geçiş yapabilirsiniz.
* **⚙️ Özelleştirilebilir Font Boyutu:** Okunabilirliği artırmak için Ayarlar menüsünden yazı boyutunu (10px - 26px) değiştirebilirsiniz.
* **⌨️ Kısayol Tuşları Desteği:** Fare kullanmadan, klavyenizdeki fonksiyon tuşları (F1-F5) ile hızlı aksiyonlar alabilirsiniz.

---

## ⌨️ Kısayol Tuşları

Editör içinde işlemlerinizi hızlandıracak işlevsel kısayollar tanımlanmıştır:

| Kısayol | İşlev |
| :---: | :--- |
| **`F1`** | Dosya Aç |
| **`F2`** | Manuel Otomatik Kaydetme Tetikleyicisi |
| **`F3`** | Dosyayı Kaydet |
| **`F4`** | Aktif Dosyayı Kalıcı Olarak Sil |
| **`F5`**| Güvenli Çıkış (Kaydedilmemiş değişiklikleri sorar) |

---

## 🚀 Kurulum ve Çalıştırma

Projenin bilgisayarınızda çalışması için sisteminizde **Python 3** yüklü olması yeterlidir. Ekstra bir dış kütüphane kurulumuna (pip) gerek yoktur.

1. Bu depoyu bilgisayarınıza klonlayın veya ZIP olarak indirin:
   ```bash
   git clone [https://github.com/kullanici_adiniz/fk-text-editor.git](https://github.com/kullanici_adiniz/furkans-text-editor.git)
Proje klasörüne giriş yapın:

Bash
cd furkans-text-editor
Scripti çalıştırın:

Bash
python main.py
(Not: Dosya adınız farklıysa main.py yerine kendi .py dosyanızın adını yazın.)

🛠️ Kullanılan Teknolojiler
Dil: Python 3

Arayüz (GUI): Tkinter

Dosya ve Sistem Yönetimi: os, tempfile

📜 Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Özgürce değiştirebilir, geliştirebilir ve kendi projelerinizde kullanabilirsiniz.
