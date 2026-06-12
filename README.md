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
* **📦 Çoklu Platform ve Taşınabilir (Portable) Sürümler:** Proje hem Windows (.exe) hem de Linux/Ubuntu (.bin) için kurulumsuz çalışacak şekilde derlenmiştir. Ayrıca izole çalıştırma için Docker desteği mevcuttur.

---

## 🚀 Kurulum ve Çalıştırma Seçenekleri

Projenizi çalıştırmak için işletim sisteminize ve tercihinize göre 4 farklı alternatif bulunmaktadır:

### 1. Windows Taşınabilir Sürüm (.EXE)
Eğer Windows kullanıyorsanız ve bilgisayarınızda Python yüklü değilse, proje klasöründeki hazır **`.exe`** uzantılı dosyaya çift tıklayarak editörü kurulumsuz olarak anında başlatabilirsiniz.

### 2. Linux (Ubuntu / Debian / Mint) Taşınabilir Sürüm
Ubuntu veya Debian tabanlı bir Linux dağıtımı kullanıyorsanız, Python kurulumu gerekmeden doğrudan derlenmiş sürümü çalıştırabilirsiniz:
1. `fk-text-editor-linux` dosyasına sağ tıklayıp **Özellikler -> İzinler** sekmesinden *"Dosyayı bir program gibi çalıştırmaya izin ver"* seçeneğini aktif edin.
2. Ya da terminalden şu komutları çalıştırın:
   ```bash
   chmod +x fk-text-editor-linux
   ./fk-text-editor-linux

Bash
cd fk-text-editor
Scripti çalıştırın:

Bash
python main.py
(Not: Dosya adınız farklıysa main.py yerine kendi .py dosyanızın adını yazın.)

🛠️ Kullanılan Teknolojiler
Dil: Python 3
Arayüz (GUI): Tkinter
Derleme Araçları: PyInstaller (Windows & Linux için bağımsız binary üretimi)
Konteynerleştirme: Docker (X11 GUI Forwarding)


Dosya ve Sistem Yönetimi: os, tempfile

📜 Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Özgürce değiştirebilir, geliştirebilir ve kendi projelerinizde kullanabilirsiniz.
