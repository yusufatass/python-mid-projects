# 🐍 Python Mid-Level Projects (Orta Seviye Python Projeleri)

Merhaba! 👋 Başlangıç seviyesindeki temel yapıları (değişkenler, döngüler, if-else) kavradıktan sonra, artık işleri bir adım ileri taşıma vakti. Bu depo (repository), Python'da fonksiyonları modüler kullanmayı, dış dosyalarla çalışmayı ve daha karmaşık algoritmalar kurmayı öğreten "Orta Seviye" projeler içermektedir.

Buradaki kodları inceleyerek **dosya okuma/yazma (File Handling), iki boyutlu listeler (Matrisler), obje yönetimi, modüller (`time`, `turtle`, `random`) ve gelişmiş oyun mantıkları** hakkında pratik yapabilirsiniz.

---

## 📂 Depo İçeriği ve Projeler

Bu repoda algoritmik düşünce becerinizi geliştirecek 5 farklı proje bulunmaktadır:

### 1. 📝 Madlibs Hikaye Oluşturucu (`madlibs_generator.py` & `story.txt`)
Dışarıdan bir metin dosyası (`story.txt`) okunarak içindeki eksik kelimelerin (sıfat, isim, fiil vb.) kullanıcıya sorulduğu ve verilen cevaplarla eğlenceli/saçma bir hikayenin oluşturulduğu kelime oyunudur.
* **Ne Öğretir?** Harici dosya okuma işlemleri (`with open`), string manipülasyonu (`.replace()`, `.find()`), listeler ve metin içi veri ayıklama işlemleri.

### 2. 🧮 Matematik Meydan Okuması (`math_challenge.py`)
Kullanıcıya rastgele matematik işlemleri (toplama, çıkarma, çarpma vb.) soran ve bu soruların tamamını ne kadar sürede çözdüğünü hesaplayan zaman karşı yarış oyunudur.
* **Ne Öğretir?** `time` modülü ile başlangıç/bitiş süresi hesaplama, döngü içinde rastgele problem üretme ve sayısal değerlerin kontrolü.

### 3. 🎲 Pig Zar Oyunu (`pig.py`)
İki veya daha fazla oyuncunun sırayla zar atarak 50 (veya 100) puana ulaşmaya çalıştığı klasik masa oyunudur. Oyuncu istediği kadar zar atabilir ancak "1" atarsa o el topladığı tüm puanı kaybeder ve sıra diğerine geçer.
* **Ne Öğretir?** Çok oyunculu (multiplayer) oyun döngüleri, sıra yönetimi, iç içe geçmiş (nested) `while` döngüleri ve kümülatif skor hesaplama mantığı.

### 4. 🎰 Slot Makinesi Oyunu (`slot_machine.py`)
Kullanıcının sanal bir bakiye yatırarak satırlar (lines) üzerinden bahis yaptığı, çarkların döndüğü ve kazanan satırların hesaplandığı kapsamlı bir casino simülasyonudur.
* **Ne Öğretir?** İki boyutlu veri yapıları (Matrisler/Sütun ve Satır mantığı), ileri seviye `if/else` koşul kurguları, "Sabit" (Constant) değişken kullanımı ve hata fırlatmayan (`try-except` veya `.isdigit()`) güvenli kullanıcı girişi alma.

### 5. 🐢 Kaplumbağa Yarışı (`turtle-race-tutorial.py`)
Kullanıcının belirlediği sayıda kaplumbağanın ekrana çizildiği, her birinin rastgele hızlarda bitiş çizgisine doğru ilerlediği görsel ve animasyonlu bir yarış simülasyonudur.
* **Ne Öğretir?** `turtle` kütüphanesi ile ekrana obje çizdirme ve hareket ettirme, koordinat sistemi (X ve Y eksenleri), listeden tekrarsız rastgele eleman seçme (`random.sample()`) ve yazılımdaki nesne (Object) mantığının temelleri.

### 6. 🔐 Kriptografik Şifre Yöneticisi (`password_manager.py`)
Kullanıcının hesap adlarını ve şifrelerini düz metin (plaintext) yerine, modern kriptografi standartlarında şifreleyerek yerel bir dosyada güvenle saklayan gelişmiş bir parola yöneticisidir. Sisteme giriş, tıpkı profesyonel uygulamalardaki gibi tek bir "Master Password" (Ana Parola) ile korunur. Yanlış ana parola girildiğinde sistemdeki hiçbir veriye ulaşılamaz.

* **Ne Öğretir?** * **Siber Güvenlik Temelleri:** Düz metinleri kırılamaz verilere dönüştüren Simetrik Şifreleme (Symmetric Encryption) mantığı.
  * **KDF ve Tuzlama (Salting):** Kullanıcının girdiği basit bir parolayı, `PBKDF2HMAC` algoritması ve rastgele üretilen bir "Salt" (Tuz) dosyası ile birleştirerek 32-byte'lık güvenli bir kriptografik anahtara dönüştürme.
  * **Dış Kütüphane Kullanımı:** Python'un güçlü `cryptography` kütüphanesinin (özellikle `Fernet` modülünün) entegrasyonu.
  * **Nesne Yönelimli Programlama (OOP):** `PasswordManager` adında bir sınıf (class) oluşturarak değişkenleri ve fonksiyonları (metotları) tek bir çatı altında düzenli bir şekilde yönetme.
  * **Kimlik Doğrulama (Authentication):** Programın ana döngüsü başlamadan önce, dosyadaki verileri arka planda çözmeyi deneyerek kullanıcının yetkisini doğrulama akışı.

 ### 6. 💱 Gerçek Zamanlı Döviz Çevirici (`currency_converter.py`)
İnternet üzerinden gerçek zamanlı bir API servisine bağlanarak güncel döviz kurlarını çeken, listeleyen ve iki para birimi arasında anlık tutar hesaplaması yapan gelişmiş bir konsol uygulamasıdır.
* **Ne Öğretir?** REST API'ler ile iletişim kurma (`urllib.request`), internetten gelen JSON formatındaki verileri sözlük (dictionary) ve listelere çevirerek işleme (`json.loads`), API anahtarı gibi hassas bilgileri `.env` (Environment Variables) dosyası ile kodun dışında güvenle saklama ve ağ hatalarını/yanlış kullanıcı girişlerini `try-except` bloklarıyla yönetme.
---
