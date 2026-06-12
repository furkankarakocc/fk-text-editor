# 📝 fk-text-editor

> ⚠️ **Beta Sürümü Notu:** Bu proje şu anda **Beta (v0.x)** aşamasındadır. Temel özellikler kararlı bir şekilde çalışsa da geliştirme süreci devam etmektedir. Kullanım sırasında karşılaştığınız hataları (bug) bildirmek veya yeni özellik önerilerinde bulunmak için lütfen [Issues](../../issues) bölümünü kullanın. Geri bildirimleriniz projenin gelişimi için çok değerlidir!

fk-text-editor, Python ve Tkinter kütüphanesi kullanılarak geliştirilmiş, minimalist, kullanıcı dostu ve hafif (lightweight) bir masaüstü metin düzenleyicidir. Günlük notlarınızı tutmak, kod taslakları oluşturmak veya `.fk` uzantılı özel dosyalarınızı yönetmek için ideal bir araçtır.

---

## ✨ Özellikler

* **Gelişmiş Dosya Yönetimi:** Yeni dosya oluşturma, mevcut dosyaları açma, kaydetme, farklı kaydetme ve dosyayı doğrudan sistemden kalıcı olarak silme.
* **🔄 Otomatik Kurtarma Sistemi (Crash Recovery):** Siz yazı yazarken arka planda otomatik olarak geçici yedek alınır. Beklenmedik kapanmalarda programı yeniden açtığınızda verileriniz kaybolmaz, otomatik olarak geri yüklenir.
* **🎨 Tema Desteği:** Göz yorgunluğunu azaltmak için tek tıkla **Karanlık Tema (Dark Mode)** ve **Aydınlık Tema (Light Mode)** arasında geçiş yapabilirsiniz.
* **⚙️ Özelleştirilebilir Font Boyutu:** Okunabilirliği artırmak için Ayarlar menüsünden yazı boyutunu (10px - 26px) değiştirebilirsiniz.
* **⌨️ Kısayol Tuşları Desteği:** Fare kullanmadan, klavyenizdeki fonksiyon tuşları (F1-F5) ile hızlı aksiyonlar alabilirsiniz.
* **🚀 Taşınabilir (.EXE) Sürüm:** Projenin Windows işletim sistemlerinde Python kurulumuna ihtiyaç duymadan, doğrudan çift tıklayarak çalıştırılabilecek hazır bir `.exe` sürümü mevcuttur.

---

## 🚀 Kurulum ve Çalıştırma

Projenizi çalıştırmak için iki farklı alternatifiniz bulunmaktadır:

### Alternatif 1: Hazır Çalıştırılabilir Dosya (Önerilen)
Eğer Windows kullanıyorsanız ve bilgisayarınızda Python yüklü değilse, proje klasöründeki hazır **`.exe`** uzantılı dosyaya çift tıklayarak editörü kurulumsuz ve taşınabilir (portable) olarak anında başlatabilirsiniz.

### Alternatif 2: Kaynak Koddan Çalıştırma (Python)
Sisteminizde **Python 3** yüklüyse, terminal veya komut satırı üzerinden şu adımları takip edebilirsiniz:

1. Bu depoyu bilgisayarınıza klonlayın veya ZIP olarak indirin:
   ```bash
   git clone [https://github.com/kullanici_adiniz/fk-text-editor.git](https://github.com/kullanici_adiniz/fk-text-editor.git)
Proje klasörüne giriş yapın:

Bash
cd fk-text-editor
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
