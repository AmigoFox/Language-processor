import csv
name_city_txt = '''
https://rp5.ru/Погода_в_мире
https://rp5.ru/Погода_в_мире
https://rp5.ru/Погода_в_Беларуси
https://rp5.ru/Погода_в_Литве
https://rp5.ru/Погода_в_России
https://rp5.ru/Погода_в_Украине
https://rp5.ru/Погода_в_мире
https://rp5.ru/Погода_в_мире
https://rp5.ru/Погода_в_России
https://rp5.ru/Погода_в_Москве
https://rp5.ru/Погода_в_Москве_(ВДНХ)
https://rp5.ru/Погода_в_Республике_Саха_(Якутии)
https://rp5.ru/Погода_в_Республике_Саха_(Якутии)
https://rp5.ru/Погода_в_Республике_Саха_(Якутии)
https://rp5.ru/Погода_в_Красноярском_крае
https://rp5.ru/Погода_в_Адыгее
https://rp5.ru/Погода_в_Майкопе
https://rp5.ru/Погода_в_Адыгее
https://rp5.ru/Погода_в_Алтайском_крае
https://rp5.ru/Погода_в_Барнауле,_Алтайский_край
https://rp5.ru/Погода_в_Алтайском_крае
https://rp5.ru/Погода_в_Амурской_области
https://rp5.ru/Погода_в_Благовещенске,_Амурская_область
https://rp5.ru/Погода_в_Амурской_области
https://rp5.ru/Погода_в_Архангельске,_Архангельская_область
https://rp5.ru/Погода_в_Северодвинске
https://rp5.ru/Погода_в_Архангельской_области
https://rp5.ru/Погода_в_Астрахани,_Астраханская_область
https://rp5.ru/Погода_в_Знаменске,_Астраханская_область
https://rp5.ru/Погода_в_Астраханской_области
https://rp5.ru/Погода_в_Башкортостане,_регион
https://rp5.ru/Погода_в_Уфе
https://rp5.ru/Погода_в_Башкортостане,_регион
https://rp5.ru/Погода_в_Белгороде,_Белгородская_область
https://rp5.ru/Погода_в_Старом_Осколе
https://rp5.ru/Погода_в_Белгородской_области
https://rp5.ru/Погода_в_Брянске,_Брянская_область
https://rp5.ru/Погода_в_Клинцах,_Брянская_область
https://rp5.ru/Погода_в_Брянской_области
https://rp5.ru/Погода_в_Бурятии
https://rp5.ru/Погода_в_Улан-Удэ
https://rp5.ru/Погода_в_Бурятии
https://rp5.ru/Погода_во_Владимире,_Владимирская_область
https://rp5.ru/Погода_в_Коврове
https://rp5.ru/Погода_во_Владимирской_области
https://rp5.ru/Погода_в_Волгограде
https://rp5.ru/Погода_в_Волжском,_Волгоградская_область
https://rp5.ru/Погода_в_Волгоградской_области
https://rp5.ru/Погода_в_Вологде
https://rp5.ru/Погода_в_Череповце
https://rp5.ru/Погода_в_Вологодской_области
https://rp5.ru/Погода_в_Воронеже,_Воронежская_область
https://rp5.ru/Погода_в_Россоши,_Воронежская_область
https://rp5.ru/Погода_в_Воронежской_области
https://rp5.ru/Погода_в_Дагестане
https://rp5.ru/Погода_в_Махачкале
https://rp5.ru/Погода_в_Дагестане
https://rp5.ru/Погода_в_Донецке,_Донецкая_Народная_Республика
https://rp5.ru/Погода_в_Горловке,_Донецкая_Народная_Республика
https://rp5.ru/Погода_в_Донецкой_Народной_Республике
https://rp5.ru/Погода_в_Еврейской_АО
https://rp5.ru/Погода_в_Биробиджане
https://rp5.ru/Погода_в_Еврейской_АО
https://rp5.ru/Погода_в_Забайкальском_крае
https://rp5.ru/Погода_в_Чите,_Забайкальский_край
https://rp5.ru/Погода_в_Забайкальском_крае
https://rp5.ru/Погода_в_Запорожье,_Запорожье
https://rp5.ru/Погода_в_Бердянске
https://rp5.ru/Погода_в_Запорожской_области
https://rp5.ru/Погода_в_Иваново,_Ивановский_район
https://rp5.ru/Погода_в_Кинешме
https://rp5.ru/Погода_в_Ивановской_области
https://rp5.ru/Погода_в_Ингушетии
https://rp5.ru/Погода_в_Магасе
https://rp5.ru/Погода_в_Ингушетии
https://rp5.ru/Погода_в_Иркутске
https://rp5.ru/Погода_в_Ангарске
https://rp5.ru/Погода_в_Иркутской_области
https://rp5.ru/Погода_в_Кабардино-Балкарии
https://rp5.ru/Погода_в_Нальчике_(аэропорт)
https://rp5.ru/Погода_в_Кабардино-Балкарии
https://rp5.ru/Погода_в_Калининграде
https://rp5.ru/Погода_в_Черняховске
https://rp5.ru/Погода_в_Калининградской_области
https://rp5.ru/Погода_в_Калмыкии
https://rp5.ru/Погода_в_Элисте
https://rp5.ru/Погода_в_Калмыкии
https://rp5.ru/Погода_в_Калуге,_Калужская_область
https://rp5.ru/Погода_в_Обнинске
https://rp5.ru/Погода_в_Калужской_области
https://rp5.ru/Погода_на_Камчатке
https://rp5.ru/Погода_в_Петропавловске-Камчатском
https://rp5.ru/Погода_на_Камчатке
https://rp5.ru/Погода_в_Карачаево-Черкесии
https://rp5.ru/Погода_в_Черкесске
https://rp5.ru/Погода_в_Карачаево-Черкесии
https://rp5.ru/Погода_в_Карелии
https://rp5.ru/Погода_в_Петрозаводске
https://rp5.ru/Погода_в_Карелии
https://rp5.ru/Погода_в_Кирове,_Кировская_область
https://rp5.ru/Погода_в_Кирово-Чепецке
https://rp5.ru/Погода_в_Кировской_области
https://rp5.ru/Погода_в_Коми
https://rp5.ru/Погода_в_Сыктывкаре
https://rp5.ru/Погода_в_Коми
https://rp5.ru/Погода_в_Костроме,_Костромская_область
https://rp5.ru/Погода_в_Буе,_Костромская_область
https://rp5.ru/Погода_в_Костромской_области
https://rp5.ru/Погода_в_Краснодаре,_Краснодарский_край
https://rp5.ru/Погода_в_Сочи
https://rp5.ru/Погода_в_Краснодарском_крае
https://rp5.ru/Погода_в_Красноярске,_Красноярский_край
https://rp5.ru/Погода_в_Дудинке,_Красноярский_край
https://rp5.ru/Погода_в_Красноярском_крае
https://rp5.ru/Погода_в_Крыму
https://rp5.ru/Погода_в_Симферополе
https://rp5.ru/Погода_в_Крыму
https://rp5.ru/Погода_в_Кемеровской_области
https://rp5.ru/Погода_в_Новокузнецке
https://rp5.ru/Погода_в_Кемеровской_области
https://rp5.ru/Погода_в_Кургане,_Курганская_область
https://rp5.ru/Погода_в_Шадринске
https://rp5.ru/Погода_в_Курганской_области
https://rp5.ru/Погода_в_Курске,_Курская_область
https://rp5.ru/Погода_в_Железногорске,_Курская_область
https://rp5.ru/Погода_в_Курской_области
https://rp5.ru/Погода_в_Ленинградской_области
https://rp5.ru/Погода_в_Киришах,_Киришский_район
https://rp5.ru/Погода_в_Ленинградской_области
https://rp5.ru/Погода_в_Липецке
https://rp5.ru/Погода_в_Ельце,_Липецкая_область
https://rp5.ru/Погода_в_Липецкой_области
https://rp5.ru/Погода_в_Луганске,_Луганская_Народная_Республика
https://rp5.ru/Погода_в_Старобельске
https://rp5.ru/Погода_в_Луганской_Народной_Республике
https://rp5.ru/Погода_в_Магадане
https://rp5.ru/Погода_в_Оле,_Россия
https://rp5.ru/Погода_в_Магаданской_области
https://rp5.ru/Погода_в_Марий_Эл
https://rp5.ru/Погода_в_Йошкар-Оле
https://rp5.ru/Погода_в_Марий_Эл
https://rp5.ru/Погода_в_Мордовии
https://rp5.ru/Погода_в_Саранске,_Мордовия
https://rp5.ru/Погода_в_Мордовии
https://rp5.ru/Погода_в_Москве_(ВДНХ)
https://rp5.ru/Погода_в_Шереметьево,_им._А._С._Пушкина_(аэропорт)
https://rp5.ru/Погода_в_Москве
https://rp5.ru/Погода_в_Московской_области
https://rp5.ru/Погода_в_Подольске,_Московская_область
https://rp5.ru/Погода_в_Московской_области
https://rp5.ru/Погода_в_Мурманске
https://rp5.ru/Погода_в_Североморске
https://rp5.ru/Погода_в_Мурманской_области
https://rp5.ru/Погода_в_Нижнем_Новгороде
https://rp5.ru/Погода_в_Дзержинске,_Нижегородская_область
https://rp5.ru/Погода_в_Нижегородской_области
https://rp5.ru/Погода_в_Новгородской_области
https://rp5.ru/Погода_в_Великом_Новгороде
https://rp5.ru/Погода_в_Новгородской_области
https://rp5.ru/Погода_в_Новосибирске
https://rp5.ru/Погода_в_Бердске
https://rp5.ru/Погода_в_Новосибирской_области
https://rp5.ru/Погода_в_Омске
https://rp5.ru/Погода_в_Таре,_Омская_область
https://rp5.ru/Погода_в_Омской_области
https://rp5.ru/Погода_в_Орле,_Орловская_область
https://rp5.ru/Погода_в_Ливнах,_Орловская_область
https://rp5.ru/Погода_в_Орловской_области
https://rp5.ru/Погода_в_Оренбурге
https://rp5.ru/Погода_в_Орске,_Оренбургская_область
https://rp5.ru/Погода_в_Оренбургской_области
https://rp5.ru/Погода_в_Пензе,_Пензенская_область
https://rp5.ru/Погода_в_Кузнецке
https://rp5.ru/Погода_в_Пензенской_области
https://rp5.ru/Погода_в_Перми
https://rp5.ru/Погода_в_Кудымкаре
https://rp5.ru/Погода_в_Пермском_крае
https://rp5.ru/Погода_в_Приморье
https://rp5.ru/Погода_во_Владивостоке
https://rp5.ru/Погода_в_Приморье
https://rp5.ru/Погода_в_Пскове
https://rp5.ru/Погода_в_Великих_Луках,_Россия
https://rp5.ru/Погода_в_Псковской_области
https://rp5.ru/Погода_в_Алтае
https://rp5.ru/Погода_в_Горно-Алтайске
https://rp5.ru/Погода_в_Алтае
https://rp5.ru/Погода_в_Республике_Саха_(Якутии)
https://rp5.ru/Погода_в_Якутске
https://rp5.ru/Погода_в_Республике_Саха_(Якутии)
https://rp5.ru/Погода_в_Ростове-на-Дону
https://rp5.ru/Погода_в_Таганроге
https://rp5.ru/Погода_в_Ростовской_области
https://rp5.ru/Погода_в_Рязани,_Рязанская_область
https://rp5.ru/Погода_в_Касимове
https://rp5.ru/Погода_в_Рязанской_области
https://rp5.ru/Погода_в_Самаре,_Самарская_область
https://rp5.ru/Погода_в_Тольятти
https://rp5.ru/Погода_в_Самарской_области
https://rp5.ru/Погода_в_Санкт-Петербурге
https://rp5.ru/Погода_в_Колпино,_Санкт-Петербург
https://rp5.ru/Погода_в_Санкт-Петербурге,_регион
https://rp5.ru/Погода_в_Саратове
https://rp5.ru/Погода_в_Энгельсе,_Саратовская_область
https://rp5.ru/Погода_в_Саратовской_области
https://rp5.ru/Погода_на_Сахалине
https://rp5.ru/Погода_в_Южно-Сахалинске
https://rp5.ru/Погода_на_Сахалине
https://rp5.ru/Погода_в_Свердловской_области
https://rp5.ru/Погода_в_Екатеринбурге
https://rp5.ru/Погода_в_Свердловской_области
https://rp5.ru/Погода_в_Севастополе,_Севастополь
https://rp5.ru/Погода_в_Севастополе
https://rp5.ru/Погода_в_Северной_Осетии-Алании
https://rp5.ru/Погода_во_Владикавказе
https://rp5.ru/Погода_в_Северной_Осетии-Алании
https://rp5.ru/Погода_в_Смоленске
https://rp5.ru/Погода_в_Вязьме,_Смоленская_область
https://rp5.ru/Погода_в_Смоленской_области
https://rp5.ru/Погода_в_Ставрополе
https://rp5.ru/Погода_в_Пятигорске,_Россия
https://rp5.ru/Погода_в_Ставропольском_крае
https://rp5.ru/Погода_в_Тамбове
https://rp5.ru/Погода_в_Мичуринске,_Тамбовская_область
https://rp5.ru/Погода_в_Тамбовской_области
https://rp5.ru/Погода_в_Татарстане,_регион
https://rp5.ru/Погода_в_Казани,_Татарстан
https://rp5.ru/Погода_в_Татарстане,_регион
https://rp5.ru/Погода_в_Твери
https://rp5.ru/Погода_в_Ржеве
https://rp5.ru/Погода_в_Тверской_области
https://rp5.ru/Погода_в_Томске
https://rp5.ru/Погода_в_Северске,_Томская_область
https://rp5.ru/Погода_в_Томской_области
https://rp5.ru/Погода_в_Туле,_Тульская_область
https://rp5.ru/Погода_в_Новомосковске,_Россия
https://rp5.ru/Погода_в_Тульской_области
https://rp5.ru/Погода_в_Тыве,_регион
https://rp5.ru/Погода_в_Кызыле,_Россия
https://rp5.ru/Погода_в_Тыве,_регион
https://rp5.ru/Погода_в_Тюмени,_Тюменская_область
https://rp5.ru/Погода_в_Тобольске
https://rp5.ru/Погода_в_Тюменской_области
https://rp5.ru/Погода_в_Удмуртии
https://rp5.ru/Погода_в_Ижевске
https://rp5.ru/Погода_в_Удмуртии
https://rp5.ru/Погода_в_Ульяновске
https://rp5.ru/Погода_в_Димитровграде,_Россия
https://rp5.ru/Погода_в_Ульяновской_области
https://rp5.ru/Погода_в_Хабаровске
https://rp5.ru/Погода_в_Комсомольске-на-Амуре
https://rp5.ru/Погода_в_Хабаровском_крае
https://rp5.ru/Погода_в_Хакасии
https://rp5.ru/Погода_в_Абакане
https://rp5.ru/Погода_в_Хакасии
https://rp5.ru/Погода_в_Ханты-Мансийске
https://rp5.ru/Погода_в_Ханты-Мансийском_автономном_округе_—_Югре
https://rp5.ru/Погода_в_Херсоне
https://rp5.ru/Погода_в_Каховке,_Херсонская_область
https://rp5.ru/Погода_в_Херсонской_области
https://rp5.ru/Погода_в_Челябинске
https://rp5.ru/Погода_в_Магнитогорске
https://rp5.ru/Погода_в_Челябинской_области
https://rp5.ru/Погода_в_Чечне
https://rp5.ru/Погода_в_Грозном,_Чечня
https://rp5.ru/Погода_в_Чечне
https://rp5.ru/Погода_в_Чувашии
https://rp5.ru/Погода_в_Чебоксарах,_Чувашия
https://rp5.ru/Погода_в_Чувашии
https://rp5.ru/Погода_в_Чукотском_АО
https://rp5.ru/Погода_в_Анадыре
https://rp5.ru/Погода_в_Чукотском_АО
https://rp5.ru/Погода_в_Ямало-Ненецком_автономном_округе
https://rp5.ru/Погода_в_Ямало-Ненецком_автономном_округе
https://rp5.ru/Погода_в_Ярославле,_Ярославская_область
https://rp5.ru/Погода_в_Рыбинске,_Ярославская_область
https://rp5.ru/Погода_в_Ярославской_области
https://rp5.ru/Погода_в_Долгопрудном
https://rp5.ru/Погода_в_Мытищах,_Московская_область
https://rp5.ru/Погода_в_Химках
https://rp5.ru/Погода_в_Реутове,_Московская_область
https://rp5.ru/Погода_в_Москве_(центр,_Балчуг)
https://rp5.ru/Погода_в_Москве_(юг)
https://rp5.ru/Погода_в_Москве_(юго-запад,_МГУ)
https://rp5.ru/Погода_в_Шереметьево,_им._А._С._Пушкина_(аэропорт)
http://rp5.ru/Погода_в_Санкт-Петербурге
'''
cities = name_city_txt.strip().split('\n')

# Открываем файл для записи в формате CSV
with open('A:/Language-processor/links_city.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Записываем заголовок
    writer.writerow(['Ссылки'])

    # Записываем каждый город в новую строку
    writer.writerows([[city] for city in cities])

print("Данные записаны в 'links_city.csv'")