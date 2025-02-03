# Akıllı Ekran Çeviri Sistemi 🌐

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-development-orange)

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/berkayozcelikel0/screen_translator/main/docs/demo.gif" alt="Demo" width="600">
</p>

Ekrandaki İngilizce metinleri gerçek zamanlı olarak Türkçe'ye çeviren ve yapay zeka destekli analiz sunan gelişmiş bir çeviri uygulaması.

## 🚀 Özellikler

- **Gerçek Zamanlı Çeviri**: Ekrandaki metinleri anında tespit edip çevirir
- **Alan Seçimi**: İstediğiniz ekran bölgesini seçerek çeviri yapabilme
- **Yapay Zeka Analizi**: Çevirilen metinlere akıllı yorumlar ve analizler
- **Sesli Okuma**: Hem İngilizce hem Türkçe metinleri sesli okuma
- **Kolay Kullanım**: Kullanıcı dostu arayüz ve pratik kısayol tuşları
- **Teknik Analiz**: PLC, otomasyon ve yazılım konularında uzman yanıtlar

## 📋 Gereksinimler

- Python 3.8 veya üzeri
- Tesseract OCR
- PyQt5
- Diğer gerekli kütüphaneler (requirements.txt dosyasında listelenmiştir)

## 🛠️ Kurulum

1. Tesseract OCR'ı yükleyin:
   - Windows için: [Tesseract-OCR indirme linki](https://github.com/UB-Mannheim/tesseract/wiki)
   - Linux için: `sudo apt-get install tesseract-ocr`

2. Python bağımlılıklarını yükleyin:
```bash
pip install -r requirements.txt
```

3. Programı çalıştırın:
```bash
python screen_translator.py
```

## 💻 Kullanım

### Kısayol Tuşları
| Tuş Kombinasyonu | İşlev |
|-----------------|-------|
| CTRL+SHIFT+A | Tüm ekranı çevir |
| CTRL+SHIFT+S | Alan seç ve çevir |
| ESC | Programı kapat |

### Butonlar
- **Tüm Ekranı Çevir**: Ekrandaki tüm metni çevirir
- **Alan Seç**: İstediğiniz bir alanı seçerek çeviri yapar
- **Temizle**: Tüm metinleri temizler
- **Kopyala**: İlgili metni panoya kopyalar
- **Sesli Oku**: Seçili metni sesli okur

## 🚧 Geliştirme Aşaması

Proje aktif geliştirme aşamasındadır. Planlanan geliştirmeler:

- [ ] OCR doğruluğunun artırılması
- [ ] Daha fazla dil desteği
- [ ] Çeviri geçmişi kaydetme
- [ ] Karanlık mod
- [ ] Özelleştirilebilir kısayol tuşları
- [ ] Daha gelişmiş yapay zeka analizi

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Açıklama'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.

## 👨‍💻 Geliştirici

<div align="center">
  <img src="https://avatars.githubusercontent.com/brkyozclkl" alt="Berkay Özçelikel" width="100" style="border-radius: 50%;">
  
  **Berkay Özçelikel**
  
  [![GitHub](https://img.shields.io/badge/GitHub-Follow-black.svg)](https://github.com/brkyozclkl)
  [![Kocaeli University](https://img.shields.io/badge/Kocaeli%20University-Student-blue.svg)](https://www.kocaeli.edu.tr/)

</div>

---

<div align="center">
  <sub>Built with ❤️ by Berkay Özçelikel</sub>
</div> 