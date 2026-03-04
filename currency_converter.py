import urllib.request
import json
import os
from pprint import PrettyPrinter
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri (API anahtarı vb.) programa yüklüyoruz
load_dotenv()

BASE_URL = "https://api.freecurrencyapi.com/v1/"
# API anahtarını artık doğrudan koda yazmak yerine yüklü olan ortamlardan çekiyoruz
# Bu sayede kodumuzu GitHub'a yüklediğimizde anahtarımız gizli kalacak
API_KEY = os.getenv("API_KEY")

printer = PrettyPrinter()

def get_currencies():
    # API'den kullanılabilir para birimi listesini çeker
    
    # API'ye istek atmak için URL oluşturulur
    url = f"{BASE_URL}currencies?apikey={API_KEY}"
    try:
        # Sunucunun bizi bot sanıp engellemesini (403 Forbidden) önlemek için kimlik (User-Agent) eklenir
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        response = urllib.request.urlopen(req)
        # Gelen veriler okunur ve JSON formatına çevrilir
        data = json.loads(response.read())['data']
        
        # Sözlük (dictionary) yapısındaki veriler listeye çevrilir ve harf sırasına göre dizilir
        currencies_list = list(data.items())
        currencies_list.sort()
        return currencies_list
    except Exception as e:
        print("API hatası:", e)
        return []

def print_currencies(currencies):
    # Parametre olarak gelen para birimlerini ekrana yazdırır
    for code, currency in currencies:
        name = currency.get('name', '')
        symbol = currency.get('symbol', '')
        print(f"{code} - {name} - {symbol}")


def exchange_rate(currency1, currency2):
    # İki para birimi arasındaki güncel kur değerini hesaplar
    url = f"{BASE_URL}latest?apikey={API_KEY}&base_currency={currency1}&currencies={currency2}"
    try:
        # Güvenlik engeline takılmamak için tekrar kimlik (User-Agent) ekliyoruz
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        
        # İsteği atıp, gelen JSON cevabı içindeki 'data' bölümünü alıyoruz
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        rates = data.get('data', {})
        
        # Eğer veri gelmediyse hatalı kur işlemi yapılmış demektir
        if not rates:
            print('Invalid currencies.')
            return None
        
        # İlk sıradaki hedef kur oranını seçip ekrana yazdırırız
        rate = list(rates.values())[0]
        print(f"{currency1} -> {currency2} = {rate}")
        return rate
    except urllib.error.HTTPError:
        # Eğer API bir HTTP hatası döndürürse hatalı kur veya geçersiz istek var demektir
        print('Invalid currencies.')
        return None
    except Exception as e:
        print('Bir hata oluştu:', e)
        return None


def convert(currency1, currency2, amount):
    # Belirli bir miktar parayı hedef para birimine çevirir
    
    # Öncelikle girdiğimiz kurların kur değeri hesaplanır
    rate = exchange_rate(currency1, currency2)
    # Eğer hesaplama sonucu None is (hata olmuşsa) işlem iptal edilir
    if rate is None:
        return

    # Girilen miktar sayıya (float - ondalık sayı türüne) dönüştürülür
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    # Miktar kur ile çarpılarak çeviri işlemi tamamlanır
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    # Ana program döngüsü
    currencies = get_currencies()
    # Kur kısaltmalarını kontrol edebilmek için "Geçerli Kodlar" listesi oluşturulur.
    valid_codes = {c[0]: c[1] for c in currencies} if currencies else {}

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    # Program bizden çıkış yapmak istemediğimiz sürece dönmeye devam eder
    while True:
        # .lower() sayesinde büyük/küçük harf duyarlılığı engellenir
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            # q yazılırsa döngü kırılır ve program kapanır
            break
        elif command == "list":
            # list yazılırsa kurlar ekrana yazdırılır
            print_currencies(currencies)
        elif command == "convert":
            # Çeviri yapmak istendiğinde önce baz alınacak (elimizdeki) para sorulur
            while True:
                currency1 = input("Enter a base currency: ").lower()
                # Eğer girilen kur geçerli listemizde varsa bir sonraki adıma geçeriz
                if currency1.upper() in valid_codes:
                    break
                print("Invalid currency. Please enter a valid currency.")
                
            # Çevrilmek istenen miktar sorulur ve doğru bir sayı girildiği doğrulanır
            while True:
                amount_str = input(f"Enter an amount in {currency1}: ")
                try:
                    amount = float(amount_str)
                    break
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")

            # Hangi para birimine çevrileceğimiz sorulur ve kontrol edilir
            while True:
                currency2 = input("Enter a currency to convert to: ").lower()
                if currency2.upper() in valid_codes:
                    break
                print("Invalid currency. Please enter a valid currency.")

            # API büyük harf kabul ettiği için seçtiğimiz kurlar .upper() ile büyütülerek fonksiyona yollanır
            convert(currency1.upper(), currency2.upper(), amount)

        elif command == "rate":
            # Sadece kuru öğrenmek istediğinde çalışacak işlemler
            while True:
                currency1 = input("Enter a base currency: ").lower()
                if currency1.upper() in valid_codes:
                    break
                print("Invalid currency. Please enter a valid currency.")

            while True:
                currency2 = input("Enter a currency to convert to: ").lower()
                if currency2.upper() in valid_codes:
                    break
                print("Invalid currency. Please enter a valid currency.")

            exchange_rate(currency1.upper(), currency2.upper())
        else:
            print("Unrecognized command!")

if __name__ == "__main__":
    main()