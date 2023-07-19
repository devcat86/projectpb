from random import *
from time import *
from turtle import *
import base64
import pelmen_fun
import requests
import string
devcount = 0 
def get_weather(city):
            api_key = '9f847b92b31f51a681d9792e18973c03'
            base_url = 'https://api.openweathermap.org/data/2.5/weather'
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric'
            }
            response = requests.get(base_url, params=params)
            weather_data = response.json()
            if weather_data['cod'] == 200:
                temperature = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']
                return f"Температура в городе {city}: {temperature}°C, {description}"
            else:
                return "Не удалось получить данные о погоде"
def devmode(devcount):
    if devcount == 1:
        print("<<<Dev Mode>>>")
        print("Тут я тестирую разное что добавляю ;)")
        print("Доступны: ультра быстрый таймер")
        per2 = int(input("Что выбираете?"))
        if per2 == 1:
            timer1 = int(input("УЛЬТРА Таймер обратного отсчета. Введите секунды."))
        for i in range(timer1, -1, -1):
            print(i)
    if devcount != 1:
        print("Blocked!!")
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choice(characters) for _ in range(length))
    return password
def main():
    length = int(input("Введите длину пароля: "))
    password = generate_password(length)
    print("Сгенерированный пароль:", password)
print("Привет! Это Project PelmenBot! Мои функции: \n1-заказ еды \n2-погода(ненастоящая) \n3-розыгрыш \n4-о чатботе \n5-что нового? \n6-погода \n7-секудомер \n8-таймер обратного отсчета \n9-генератор цифр \n10-шифратор паролей в base64 \n11-проверка длинны пароля \n12-игра КНБ \n13-тест\nВыбирай цифру!")
ipt = int(input("Что вы хотите сделать?(введите 0 для выхода):"))
while ipt != 0:
    if ipt == 1:
        pelmen_fun.eda()
    elif ipt == 2:
        pelmen_fun.pogod()
    elif ipt == 3:
        print("Угадайте число от 1 до 100!")
        count = randint(1,100)
        price = int(input("Введите число: "))
        while price != count:
            if price > 101:
                print("Сказали же, ДО 100 xD")
            elif price > count:
                print("Число меньше!")
            elif price < count:
                print("Число больше!")
            else:
                break
            price = int(input("Введите число: "))
        if price == count:
                print("Вы угадали!")
        if price != count:
            print("Повезет в другой раз!")
    elif ipt == 4:
        print("Чатбот projectpb(Пельмень). Версия 1.5.0 от 19.07.23. Все права съедены шлепой. 6,10 пункты взяты из интернета, я не писал их сам.")
    elif ipt == 5:
        pelmen_fun.info()
    elif ipt == 999:
        if devcount == 0:
            devcount += 1
            print("ok!")
            per2 = int(input("Войти в режим разработчика? 1 or 0"))
            if per2 == 1:
                devmode(devcount)
        if devcount != 1:
            print("Blocked!!")
    elif ipt == 6:
        city = input("Введите название города: ")
        weather = get_weather(city)
        print(weather)
    elif ipt == 7:
        sec_start = int(input("1 - запустить таймер, 0 - выйти"))
        if sec_start == 1:
            start = time()
            sec_end = int(input("0 - стоп"))
            end = time()
            total_time = (end - start)
            print("Время -",round(total_time, 3))
    elif ipt == 8:
        timer1 = int(input("Таймер обратного отсчета. Введите секунды."))
        for i in range(timer1, -1, -1):
            print(i)
            sleep(1)
    elif ipt == 9:
        passw = "0"
        gen_ipt = int(input("Введите длинну пароля:"))
        for i in range(gen_ipt):
            passw += str(randint(0,9))
        print("Ваш пароль:", passw)
    elif ipt == 10:
        q = input("Введите пароль: ")
        b = q.encode("UTF-8")
        e = base64.b64encode(b)
        s1 = e.decode("UTF-8")
        print(s1)
    elif ipt == 11:
        per3 = input("Введите пароль: ")
        print("Длинна пароля:", len(per3))
        if len(per3) < 8:
            print("Слишком короткий пароль! Рекомендую заменить на более надежный!")
    elif ipt == 12:
            pelmen_fun.knb() 
    elif ipt == 13:
        hideturtle()
        def fun1():
            color("blue")
            pensize(2)
            speed(15)
            for i in range(36):
                color("blue")
                bebra()
                left(10)
                color("green")
                bebra()
                left(10)
        def bebra():
            for i in range(1):
                forward(100)
                left(120)
        fun1()
    else: 
        print("Прости, я тебя не понял:(")
    ipt = int(input("Что вы хотите сделать?(введите 0 для выхода):"))
print("Пока ;)")