import os
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class PasswordManager:
    def __init__(self, master_password: str, salt_filename: str = "salt.key", pwd_filename: str = "password.txt"):
        self.salt_filename = salt_filename
        self.pwd_filename = pwd_filename

        self.key = self._generate_key_from_password(master_password)
        self.fernet = Fernet(self.key)

        # Sınıf başlatıldığında parolayı test et ve sonucu bir değişkende tut
        self.is_authenticated = self._verify_password()

    def _generate_key_from_password(self, password: str) -> bytes:
        if not os.path.exists(self.salt_filename):
            print("[BİLGİ] Yeni güvenlik tuzu (salt) oluşturuluyor...")
            salt = os.urandom(16)
            with open(self.salt_filename, "wb") as file:
                file.write(salt)
        else:
            with open(self.salt_filename, "rb") as file:
                salt = file.read()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def _verify_password(self) -> bool:
        """
        Dosyadaki kayıtlı ilk şifreyi çözmeyi deneyerek
        girilen Master Password'ün doğru olup olmadığını test eder.
        """
        # Eğer dosya hiç yoksa, kullanıcı programı ilk kez çalıştırıyordur. Parola geçerli kabul edilir.
        if not os.path.exists(self.pwd_filename):
            return True

        with open(self.pwd_filename, "r", encoding="utf-8") as file:
            for line in file.readlines():
                data = line.strip()
                if "|" in data:
                    _, encrypted_pass = data.split("|", 1)
                    try:
                        # Sadece şifreyi çözmeyi deniyoruz, ekrana yazdırmıyoruz
                        self.fernet.decrypt(encrypted_pass.encode())
                        return True  # Çözüldüyse parola doğru!
                    except InvalidToken:
                        return False  # Çözülemediyse parola kesinlikle yanlış!

        # Dosya var ama içi boşsa yine kabul et
        return True

    def add_password(self, account_name: str, password: str) -> None:
        encrypted_pass = self.fernet.encrypt(password.encode()).decode()
        with open(self.pwd_filename, "a", encoding="utf-8") as file:
            file.write(f"{account_name}|{encrypted_pass}\n")
        print(f"✅ '{account_name}' için şifre başarıyla eklendi!")

    def view_passwords(self) -> None:
        if not os.path.exists(self.pwd_filename):
            print("📭 Henüz kaydedilmiş bir şifre bulunmuyor.")
            return

        print("\n--- Kayıtlı Şifreleriniz ---")
        with open(self.pwd_filename, "r", encoding="utf-8") as file:
            for line in file.readlines():
                data = line.strip()
                if "|" not in data:
                    continue

                account, encrypted_pass = data.split("|", 1)

                try:
                    decrypted_pass = self.fernet.decrypt(encrypted_pass.encode()).decode()
                    print(f"🔹 Hesap: {account:<15} | Şifre: {decrypted_pass}")
                except InvalidToken:
                    print(f"❌ [HATA] Veri bozuk veya yetkisiz erişim!")
        print("-" * 28)


# ==========================================
# ANA UYGULAMA DÖNGÜSÜ
# ==========================================

def main():
    print("🔐 Güvenli Password Manager'a Hoş Geldiniz! 🔐\n")

    m_pwd = input("Lütfen Master Password'ünüzü girin: ").strip()

    pm = PasswordManager(master_password=m_pwd)

    # KAPIDA KONTROL: Eğer parola doğrulamadan geçemediyse programı anında kapat!
    if not pm.is_authenticated:
        print("\n❌ GİRİŞ BAŞARISIZ! Yanlış Master Password girdiniz.")
        print("Güvenlik nedeniyle program sonlandırılıyor...")
        return  # return diyerek main() fonksiyonunu bitirir ve programı kapatırız.

    print("\n✅ Giriş Başarılı! Kasanın kilidi açıldı.")

    while True:
        mode = input("\nİşlem (add / view / q): ").strip().lower()

        if mode in ['q', 'çıkış']:
            print("Kasa kilitlendi. Görüşmek üzere! 👋")
            break
        elif mode == 'view':
            pm.view_passwords()
        elif mode == 'add':
            name = input("Hesap Adı: ").strip()
            pwd = input("Şifre: ").strip()
            if name and pwd:
                pm.add_password(name, pwd)
            else:
                print("❌ Hesap adı veya şifre boş bırakılamaz!")
        else:
            print("❌ Geçersiz seçim.")


if __name__ == "__main__":
    main()