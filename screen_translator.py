import pytesseract
import pyautogui
import time
from PIL import Image
from deep_translator import GoogleTranslator
import os
import keyboard
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QTextEdit, QPushButton, QLabel, QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPoint, QRect
from PyQt5.QtGui import QPainter, QColor, QPen
import sys

def analyze_text(text):
    """Metni analiz edip detaylı paragraf cevapları üreten fonksiyon"""
    text = text.lower()
    
    # Teknik konular ve anahtar kelimeler
    teknik_konular = {
        'programlama': ['algoritma', 'kod', 'program', 'yazılım', 'debug', 'test', 'geliştirme', 'dil'],
        'veritabanı': ['sql', 'database', 'veri', 'tablo', 'sorgu', 'index', 'join', 'crud'],
        'web': ['html', 'css', 'javascript', 'api', 'rest', 'frontend', 'backend', 'http'],
        'ağ': ['tcp/ip', 'network', 'protokol', 'router', 'switch', 'ip', 'port', 'server'],
        'güvenlik': ['security', 'şifreleme', 'hash', 'authentication', 'authorization', 'token', 'ssl'],
        'yazılım_mimarisi': ['design pattern', 'solid', 'mvc', 'oop', 'inheritance', 'interface', 'clean code'],
        'devops': ['docker', 'kubernetes', 'ci/cd', 'jenkins', 'git', 'deployment', 'container'],
        'yapay_zeka': ['machine learning', 'ai', 'deep learning', 'neural network', 'model', 'training'],
        'plc': ['ladder', 'scada', 'hmi', 'sensör', 'aktüatör', 'siemens', 'allen bradley', 'otomasyon', 'endüstriyel'],
        'endüstriyel_otomasyon': ['motor', 'sürücü', 'inverter', 'servo', 'encoder', 'fieldbus', 'profinet', 'modbus'],
        'proses_kontrol': ['pid', 'kontrol', 'regülasyon', 'kalibrasyon', 'ölçüm', 'vana', 'basınç', 'sıcaklık'],
        'elektrik': ['pano', 'güç', 'voltaj', 'akım', 'röle', 'kontaktör', 'sigorta', 'ups']
    }

    # Konuyu belirle
    konu = None
    max_eslesen = 0
    for alan, keywords in teknik_konular.items():
        eslesen = sum(1 for keyword in keywords if keyword in text)
        if eslesen > max_eslesen:
            max_eslesen = eslesen
            konu = alan

    # Anahtar kelimeleri çıkar
    words = text.split()
    anahtar_kelimeler = [word for word in words if len(word) > 3]

    # Detaylı cevap oluştur
    if konu in ['plc', 'endüstriyel_otomasyon', 'proses_kontrol', 'elektrik']:
        if 'nasıl' in text:
            return f"""Endüstriyel otomasyon konusunda detaylı bir açıklama yapmak isterim. {' '.join(anahtar_kelimeler[:2]).capitalize() if len(anahtar_kelimeler) >= 2 else konu.capitalize()} sistemlerinin kurulumu ve programlanması, dikkatli bir planlama ve uzmanlık gerektiren bir süreçtir.

İlk olarak, sistem tasarımı ve donanım seçimi çok önemlidir. PLC seçiminde Siemens S7-1200/1500, Allen Bradley CompactLogix gibi endüstri standardı ürünler tercih edilmelidir. Ayrıca, sensörler, aktüatörler ve diğer saha ekipmanlarının doğru seçimi de sistemin güvenilirliği için kritiktir.

Programlama aşamasında, öncelikle sistem gereksinimleri detaylı olarak analiz edilmelidir. Ladder diyagramı, Function Block (FB) veya Structured Text (ST) gibi IEC 61131-3 standardına uygun programlama dillerinden projeye en uygun olanı seçilmelidir. Program yazılırken hata yönetimi, acil durum senaryoları ve güvenlik önlemleri mutlaka düşünülmelidir.

Son olarak, devreye alma ve test süreçleri büyük önem taşır. Sistemin kademeli olarak test edilmesi, tüm güvenlik önlemlerinin doğrulanması ve operatör eğitimlerinin tamamlanması gerekir. Düzenli bakım planları ve yedekleme prosedürleri de oluşturulmalıdır."""

        elif 'neden' in text:
            return f"""Endüstriyel otomasyonun neden önemli olduğunu açıklamak gerekirse, {' '.join(anahtar_kelimeler[:2]).capitalize() if len(anahtar_kelimeler) >= 2 else konu.capitalize()} sistemleri modern üretim tesislerinin vazgeçilmez bir parçasıdır.

Üretim verimliliği açısından bakıldığında, otomasyon sistemleri üretim hızını artırırken hata oranlarını minimize eder. İnsan kaynaklı hataların önlenmesi, tekrarlanabilir kalite ve yüksek hassasiyet sağlanması gibi avantajlar sunar. Örneğin, bir PLC kontrollü üretim hattı, 24 saat kesintisiz ve tutarlı kalitede üretim yapabilir.

Maliyet optimizasyonu konusunda da önemli avantajlar sağlar. İşçilik maliyetlerinin azaltılması, enerji verimliliğinin artırılması ve fire oranlarının düşürülmesi gibi ekonomik faydalar sunar. Ayrıca, üretim verilerinin gerçek zamanlı izlenebilmesi sayesinde, süreç optimizasyonu ve kaynak planlaması daha etkin yapılabilir.

Endüstri 4.0 ve dijital dönüşüm perspektifinden değerlendirdiğimizde, modern otomasyon sistemleri akıllı fabrikaların temelini oluşturur. SCADA sistemleri, HMI'lar ve veri toplama sistemleri sayesinde üretim süreçleri tam anlamıyla dijitalleştirilebilir ve uzaktan izlenebilir."""

        else:
            return f"""{konu.replace('_', ' ').capitalize()} sistemleri hakkında kapsamlı bir değerlendirme yapmak gerekirse, bu teknolojiler modern endüstrinin temel yapı taşlarıdır.

Temel bileşenler açısından, bir otomasyon sistemi PLC'ler, HMI paneller, sensörler, aktüatörler ve haberleşme ağlarından oluşur. PLC'ler sistemin beyni görevi görürken, sensörler ve aktüatörler sistemin duyu organları ve kasları gibi çalışır. SCADA sistemleri ise tüm bu bileşenlerin merkezi kontrolünü ve izlenmesini sağlar.

Haberleşme protokolleri ve ağ yapısı da kritik öneme sahiptir. Profinet, EtherCAT, Modbus TCP gibi endüstriyel haberleşme protokolleri, sistem bileşenleri arasında güvenilir ve hızlı iletişim sağlar. Özellikle gerçek zamanlı kontrol uygulamalarında, bu protokollerin doğru seçimi ve konfigürasyonu büyük önem taşır.

Güvenlik ve yedeklilik konuları da mutlaka düşünülmelidir. Safety PLC'ler, acil stop sistemleri, güvenlik bariyerleri gibi ekipmanlar personel ve makine güvenliği için vazgeçilmezdir. Yedekli (redundant) sistemler ise kritik proseslerde kesintisiz çalışma için tercih edilir."""

    elif konu:
        if 'nasıl' in text:
            return f"""Bu sorunun cevabını detaylı bir şekilde açıklamak isterim. {' '.join(anahtar_kelimeler[:2]).capitalize() if len(anahtar_kelimeler) >= 2 else konu.capitalize()} konusu, modern yazılım geliştirme süreçlerinin önemli bir parçasıdır. Bu alanda başarılı olmak için öncelikle temel prensipleri iyi anlamak gerekiyor.

İlk olarak, planlama aşamasından bahsetmek istiyorum. Her projenin başında detaylı bir analiz ve planlama yapılması çok önemlidir. Bu aşamada gereksinimler belirlenmeli, kullanılacak teknolojiler seçilmeli ve bir yol haritası çıkarılmalıdır. Deneyimlerime göre, bu aşamaya yeterince zaman ayırmayan projelerde ileride ciddi sorunlar yaşanabiliyor.

Uygulama aşamasına geldiğimizde, modern geliştirme pratiklerini kullanmak büyük önem taşıyor. Örneğin, Test-Driven Development (TDD) yaklaşımını benimsemek, kodun kalitesini artırırken hata oranını düşürüyor. Ayrıca, düzenli code review'lar yapmak ve pair programming uygulamak da kod kalitesini artıran önemli faktörler.

Son olarak, sürekli öğrenme ve gelişim konusuna değinmek istiyorum. Teknoloji dünyası çok hızlı değişiyor ve güncel kalmak için sürekli kendimizi geliştirmemiz gerekiyor. Düzenli olarak yeni teknolojileri takip etmek, online kurslara katılmak ve topluluk etkinliklerine katılmak profesyonel gelişim için çok değerli."""

        elif 'neden' in text:
            return f"""Bu soruya kapsamlı bir yanıt vermek gerekirse, {' '.join(anahtar_kelimeler[:2]).capitalize() if len(anahtar_kelimeler) >= 2 else konu.capitalize()} konusunun birçok önemli avantajı bulunmaktadır. Öncelikle teknik perspektiften bakacak olursak, modern yazılım geliştirme süreçlerinde bu yaklaşımın sağladığı faydalar oldukça belirgindir.

Sistem mimarisi açısından değerlendirdiğimizde, bu yaklaşım bize ölçeklenebilirlik ve sürdürülebilirlik konularında büyük avantajlar sağlıyor. Özellikle büyük ölçekli projelerde, sistemin modüler yapısı sayesinde bakım ve geliştirme süreçleri çok daha kolay yönetilebiliyor.

İş süreçleri perspektifinden baktığımızda, verimlilik artışı ve maliyet optimizasyonu konularında önemli kazanımlar elde edildiğini görüyoruz. Projelerimde edindiğim tecrübelere dayanarak söyleyebilirim ki, bu yaklaşımı benimseyen ekipler çok daha hızlı ve etkili sonuçlar elde edebiliyor.

Uzun vadeli başarı için önerilerim ise şunlar: Öncelikle best practice'leri yakından takip etmek ve uygulamak çok önemli. Düzenli code review'lar ve sürekli iyileştirme yaklaşımı, projenin kalitesini sürekli olarak artırıyor. Ayrıca, ekip içi bilgi paylaşımı ve dokümantasyon da sürdürülebilirlik açısından kritik öneme sahip."""

        else:
            return f"""{konu.replace('_', ' ').capitalize()} konusunda size detaylı bir açıklama yapmak isterim. Bu alan, modern teknoloji dünyasının en önemli konularından biridir ve sürekli gelişim göstermektedir.

Öncelikle temel kavramlardan başlayalım. {' '.join(anahtar_kelimeler[:2]).capitalize() if len(anahtar_kelimeler) >= 2 else 'Bu teknoloji'}, günümüz yazılım dünyasında çok önemli bir yere sahiptir. Temel prensipleri ve best practice'leri iyi anlamak, başarılı projeler geliştirmek için kritik öneme sahiptir. Özellikle büyük ölçekli projelerde, bu prensiplere bağlı kalmak projenin başarısını doğrudan etkiliyor.

Pratik uygulamalar konusuna geldiğimizde, endüstri standardı yaklaşımların ve design pattern'ların doğru kullanımı öne çıkıyor. Yıllara dayanan tecrübelerime dayanarak söyleyebilirim ki, bu pattern'ları doğru yerde ve doğru şekilde kullanmak, projenin kalitesini ve sürdürülebilirliğini önemli ölçüde artırıyor.

Gelecek trendleri açısından baktığımızda, bu alanın sürekli evrildiğini ve yeni teknolojilerle zenginleştiğini görüyoruz. Özellikle cloud computing ve mikroservis mimarileri gibi modern yaklaşımlarla birlikte, bu alanın önemi daha da artıyor. Kendimizi sürekli geliştirmek ve yeni teknolojileri takip etmek, profesyonel kariyerimiz için çok önemli."""

    # Genel cevap
    return """Bu soruyu detaylı bir şekilde ele almak gerekirse, öncelikle konunun teorik temellerini iyi anlamak önemlidir. Modern yazılım geliştirme dünyasında, temel prensiplere hakim olmak ve best practice'leri doğru uygulamak, başarılı projeler geliştirmenin anahtarıdır.

Pratik uygulama açısından baktığımızda, gerçek dünya senaryolarından öğrendiğimiz çok şey var. Örneğin, problem çözme yaklaşımları ve optimizasyon teknikleri, projelerin başarısında kritik rol oynuyor. Yıllara dayanan tecrübelerim gösteriyor ki, bu konulara gereken önemi vermek, projelerin başarı şansını önemli ölçüde artırıyor.

Kişisel deneyimlerime dayanarak söyleyebilirim ki, her projede karşılaşılan zorluklar ve bunların çözümleri, bize çok değerli dersler öğretiyor. Özellikle büyük ölçekli projelerde, bu deneyimler daha da önem kazanıyor.

Son olarak, sürekli öğrenme ve gelişimin önemini vurgulamak isterim. Teknoloji dünyası çok hızlı değişiyor ve güncel kalmak için kendimizi sürekli geliştirmemiz gerekiyor. Takım çalışması ve kod kalitesi gibi konular da başarılı projeler için vazgeçilmez unsurlardır."""

# Tesseract yolunu kontrol et ve ayarla
tesseract_paths = [
    r'C:\Program Files\Tesseract-OCR\tesseract.exe',
    r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
    r'C:\Tesseract-OCR\tesseract.exe'
]

for path in tesseract_paths:
    if os.path.exists(path):
        pytesseract.pytesseract.tesseract_cmd = path
        break
else:
    print("HATA: Tesseract bulunamadı! Lütfen Tesseract OCR'ı yükleyin:")
    print("https://github.com/UB-Mannheim/tesseract/wiki")
    exit(1)

def preprocess_image(image):
    """Görüntüyü OCR için optimize et"""
    # Görüntüyü 2 kat büyüt
    width, height = image.size
    new_width = width * 2
    new_height = height * 2
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

class ScreenSelector(QWidget):
    area_selected = pyqtSignal(tuple)
    
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(QApplication.desktop().geometry())
        
        self.begin = QPoint()
        self.end = QPoint()
        self.is_drawing = False
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Yarı saydam siyah arka plan
        painter.setBrush(QColor(0, 0, 0, 100))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())
        
        if self.is_drawing:
            # Seçili alanı çiz
            rect = QRect(self.begin, self.end)
            # Seçili alanın içini temizle (şeffaf yap)
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.drawRect(rect)
            
            # Seçili alanın çerçevesini çiz
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
            painter.setPen(QPen(QColor(255, 255, 255), 2))
            painter.setBrush(Qt.NoBrush)
            painter.drawRect(rect)
            
            # Boyutları göster
            size_text = f"{abs(rect.width())}x{abs(rect.height())}"
            painter.setPen(QPen(QColor(255, 255, 255)))
            painter.drawText(rect.center(), size_text)
    
    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.is_drawing = True
        self.update()
    
    def mouseMoveEvent(self, event):
        if self.is_drawing:
            self.end = event.pos()
            self.update()
    
    def mouseReleaseEvent(self, event):
        if self.is_drawing:
            x1, y1 = self.begin.x(), self.begin.y()
            x2, y2 = self.end.x(), self.end.y()
            
            # Koordinatları düzenle (sol üst ve sağ alt köşe olacak şekilde)
            left = min(x1, x2)
            top = min(y1, y2)
            right = max(x1, x2)
            bottom = max(y1, y2)
            
            self.area_selected.emit((left, top, right, bottom))
            self.close()
    
    def keyPressEvent(self, event):
        # ESC tuşuna basılırsa seçimi iptal et
        if event.key() == Qt.Key_Escape:
            self.close()

class TranslatorThread(QThread):
    finished = pyqtSignal(str, str, str, str)

    def __init__(self, area=None):
        super().__init__()
        self.area = area

    def run(self):
        try:
            if self.area:
                # Belirli bir alanın ekran görüntüsünü al
                left, top, right, bottom = self.area
                width = right - left
                height = bottom - top
                
                # Seçilen alanı biraz genişlet
                padding = 15
                left = max(0, left - padding)
                top = max(0, top - padding)
                width = width + (padding * 2)
                height = height + (padding * 2)
                
                # Ekran görüntüsünü al
                screenshot = pyautogui.screenshot(region=(left, top, width, height))
                
                # Görüntüyü büyüt
                width, height = screenshot.size
                large_img = screenshot.resize((width * 3, height * 3), Image.Resampling.LANCZOS)
                
                # Farklı OCR ayarlarıyla dene
                configs = [
                    r'--psm 6 --oem 3',  # Tek blok metin
                    r'--psm 3 --oem 3',  # Otomatik sayfa segmentasyonu
                    r'--psm 4 --oem 3',  # Tek sütun metin
                ]
                
                texts = []
                for config in configs:
                    # Büyütülmüş görüntüde dene
                    text = pytesseract.image_to_string(
                        large_img,
                        lang='eng',
                        config=config
                    ).strip()
                    if text:
                        texts.append(text)
                
                # En iyi sonucu seç
                if texts:
                    # En uzun ve anlamlı metni seç
                    text = max(texts, key=lambda x: len(x.split()))
                else:
                    text = ""
            else:
                # Tüm ekranın görüntüsünü al
                screenshot = pyautogui.screenshot()
                text = pytesseract.image_to_string(
                    screenshot,
                    lang='eng',
                    config='--psm 3 --oem 3'
                ).strip()
            
            # Metni temizle ve düzenle
            if text:
                # Gereksiz satır sonlarını ve boşlukları temizle
                lines = [line.strip() for line in text.splitlines() if line.strip()]
                text = ' '.join(lines)
                
                try:
                    translator = GoogleTranslator(source='auto', target='tr')
                    translation = translator.translate(text)
                except Exception as e:
                    translation = f"Çeviri hatası: {str(e)}"
                
                # AI yanıtı oluştur
                ai_response = analyze_text(translation)
                
                self.finished.emit(text, translation, time.strftime("%H:%M:%S"), ai_response)
            else:
                self.finished.emit("Metin algılanamadı", "Metin algılanamadı", time.strftime("%H:%M:%S"), "")
        except Exception as e:
            print(f"Hata oluştu: {str(e)}")
            self.finished.emit("Hata oluştu", str(e), time.strftime("%H:%M:%S"), "")

class TranslatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.translator_thread = None
        self.screen_selector = None
        self.shortcuts = []
        
    def initUI(self):
        self.setWindowTitle('Ekran Çeviri Sistemi')
        self.setGeometry(100, 100, 800, 600)
        
        # Ana widget ve layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Kısayol bilgisi
        shortcut_label = QLabel('CTRL+SHIFT+A: Tüm ekranı çevir\nCTRL+SHIFT+S: Alan seç ve çevir\nESC: Programı kapat')
        shortcut_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(shortcut_label)
        
        # Buton layout'u
        button_layout = QHBoxLayout()
        
        # Tüm ekranı çevir butonu
        full_screen_button = QPushButton('Tüm Ekranı Çevir')
        full_screen_button.clicked.connect(self.start_full_translation)
        button_layout.addWidget(full_screen_button)
        
        # Alan seç butonu
        select_area_button = QPushButton('Alan Seç')
        select_area_button.clicked.connect(self.start_area_selection)
        button_layout.addWidget(select_area_button)
        
        # Temizle butonu
        clear_button = QPushButton('Temizle')
        clear_button.clicked.connect(self.clear_texts)
        button_layout.addWidget(clear_button)
        
        layout.addLayout(button_layout)
        
        # Orijinal metin
        layout.addWidget(QLabel('Algılanan Metin:'))
        self.original_text = QTextEdit()
        self.original_text.setReadOnly(False)  # Düzenlenebilir yap
        layout.addWidget(self.original_text)
        
        # Orijinal metin butonları
        original_buttons = QHBoxLayout()
        
        # Kopyala butonu
        copy_original_button = QPushButton('Kopyala')
        copy_original_button.clicked.connect(lambda: self.copy_text(self.original_text))
        original_buttons.addWidget(copy_original_button)
        
        # Sesli oku butonu
        speak_original_button = QPushButton('Sesli Oku (EN)')
        speak_original_button.clicked.connect(lambda: self.speak_text(self.original_text.toPlainText(), 'en'))
        original_buttons.addWidget(speak_original_button)
        
        layout.addLayout(original_buttons)
        
        # Çeviri
        layout.addWidget(QLabel('Türkçe Çeviri:'))
        self.translated_text = QTextEdit()
        self.translated_text.setReadOnly(False)  # Düzenlenebilir yap
        layout.addWidget(self.translated_text)
        
        # Çeviri butonları
        translation_buttons = QHBoxLayout()
        
        # Kopyala butonu
        copy_translation_button = QPushButton('Kopyala')
        copy_translation_button.clicked.connect(lambda: self.copy_text(self.translated_text))
        translation_buttons.addWidget(copy_translation_button)
        
        # Sesli oku butonu
        speak_translation_button = QPushButton('Sesli Oku (TR)')
        speak_translation_button.clicked.connect(lambda: self.speak_text(self.translated_text.toPlainText(), 'tr'))
        translation_buttons.addWidget(speak_translation_button)
        
        layout.addLayout(translation_buttons)
        
        # AI Yanıtı için yeni metin alanı
        layout.addWidget(QLabel('Yapay Zeka Yanıtı:'))
        self.ai_response_text = QTextEdit()
        self.ai_response_text.setReadOnly(False)
        layout.addWidget(self.ai_response_text)
        
        # AI yanıtı için butonlar
        ai_buttons = QHBoxLayout()
        
        # Kopyala butonu
        copy_ai_button = QPushButton('Kopyala')
        copy_ai_button.clicked.connect(lambda: self.copy_text(self.ai_response_text))
        ai_buttons.addWidget(copy_ai_button)
        
        # Sesli oku butonu
        speak_ai_button = QPushButton('Sesli Oku (TR)')
        speak_ai_button.clicked.connect(lambda: self.speak_text(self.ai_response_text.toPlainText(), 'tr'))
        ai_buttons.addWidget(speak_ai_button)
        
        layout.addLayout(ai_buttons)
        
        # Kısayol tuşlarını ayarla
        self.setup_shortcuts()
        
        self.show()
    
    def setup_shortcuts(self):
        """Kısayol tuşlarını ayarla"""
        try:
            # Önceki tüm kısayolları temizle
            keyboard.unhook_all()
            
            # Global kısayolları tanımla
            keyboard.add_hotkey('ctrl+shift+a', lambda: QApplication.postEvent(
                self, 
                QApplication.postEvent(self, type('_', (), {'type': lambda _: 'shortcut_full'})())
            ))
            keyboard.add_hotkey('ctrl+shift+s', lambda: QApplication.postEvent(
                self, 
                QApplication.postEvent(self, type('_', (), {'type': lambda _: 'shortcut_area'})())
            ))
            keyboard.add_hotkey('esc', lambda: QApplication.postEvent(
                self, 
                QApplication.postEvent(self, type('_', (), {'type': lambda _: 'shortcut_close'})())
            ))
        except Exception as e:
            print(f"Kısayol tuşları ayarlanırken hata oluştu: {e}")

    def event(self, event):
        """Özel olayları işle"""
        if hasattr(event, 'type'):
            event_type = event.type()
            if event_type == 'shortcut_full':
                self.start_full_translation()
                return True
            elif event_type == 'shortcut_area':
                self.start_area_selection()
                return True
            elif event_type == 'shortcut_close':
                self.close()
                return True
        return super().event(event)

    def start_full_translation(self):
        """Tam ekran çeviriyi başlat"""
        if not self.isHidden() and (self.translator_thread is None or not self.translator_thread.isRunning()):
            self.translator_thread = TranslatorThread()
            self.translator_thread.finished.connect(self.update_texts)
            self.translator_thread.start()

    def start_area_selection(self):
        """Alan seçimini başlat"""
        if not self.isHidden():
            self.hide()  # Ana pencereyi gizle
            time.sleep(0.2)  # Pencerenin kaybolması için kısa bir bekleme
            
            self.screen_selector = ScreenSelector()
            self.screen_selector.area_selected.connect(self.on_area_selected)
            self.screen_selector.show()

    def on_area_selected(self, area):
        self.show()  # Ana pencereyi tekrar göster
        if self.translator_thread is None or not self.translator_thread.isRunning():
            self.translator_thread = TranslatorThread(area)
            self.translator_thread.finished.connect(self.update_texts)
            self.translator_thread.start()
    
    def update_texts(self, original, translation, timestamp, ai_response):
        current_original = self.original_text.toPlainText()
        current_translated = self.translated_text.toPlainText()
        current_ai = self.ai_response_text.toPlainText()
        
        # Yeni metinleri ekle
        new_original = f"[{timestamp}]\n{original}\n\n{current_original}"
        new_translated = f"[{timestamp}]\n{translation}\n\n{current_translated}"
        new_ai = f"[{timestamp}]\n{ai_response}\n\n{current_ai}"
        
        self.original_text.setText(new_original)
        self.translated_text.setText(new_translated)
        self.ai_response_text.setText(new_ai)
    
    def clear_texts(self):
        self.original_text.clear()
        self.translated_text.clear()
        self.ai_response_text.clear()
    
    def closeEvent(self, event):
        """Pencere kapatılırken tüm kaynakları temizle"""
        try:
            # Kısayolları temizle
            keyboard.unhook_all()
            
            # Thread'leri temizle
            if self.translator_thread and self.translator_thread.isRunning():
                self.translator_thread.terminate()
                self.translator_thread.wait()
            
            # Screen selector'ı temizle
            if self.screen_selector:
                self.screen_selector.close()
        except Exception:
            pass
        
        event.accept()
    
    def copy_text(self, text_edit):
        """Metni panoya kopyala"""
        clipboard = QApplication.clipboard()
        clipboard.setText(text_edit.toPlainText())
    
    def speak_text(self, text, lang):
        """Metni sesli oku"""
        try:
            if lang == 'tr':
                # Türkçe metin için Google TTS kullan
                from gtts import gTTS
                import pygame
                import tempfile
                import os
                
                # Pygame mixer'ı başlat
                pygame.mixer.init()
                
                # Geçici ses dosyası oluştur
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                    temp_filename = fp.name
                
                try:
                    # Metni sese çevir
                    tts = gTTS(text=text, lang='tr')
                    tts.save(temp_filename)
                    
                    # Sesi çal
                    pygame.mixer.music.load(temp_filename)
                    pygame.mixer.music.play()
                    
                    # Ses bitene kadar bekle
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
                    
                    # Mixer'ı kapat
                    pygame.mixer.quit()
                finally:
                    # Geçici dosyayı sil
                    try:
                        os.unlink(temp_filename)
                    except:
                        pass
            else:
                # İngilizce metin için pyttsx3 kullan
                import pyttsx3
                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
        except Exception as e:
            print(f"Sesli okuma hatası: {str(e)}")
            QMessageBox.warning(self, "Hata", "Sesli okuma sırasında bir hata oluştu!")

def main():
    app = QApplication(sys.argv)
    ex = TranslatorWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 