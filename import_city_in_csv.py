import csv
name_city_txt = '''
мире
мире
Беларуси
Литве
России
Украине
мире
мире
России
Москве
Москве (ВДНХ)
Архангельской области
Архангельской области
Республике Саха (Якутии)
Краснодарском крае
Краснодарском крае
Карелии
Адыгее
Майкопе
Адыгее
Алтайском крае
Барнауле, Алтайский край
Алтайском крае
Амурской области
Благовещенске, Амурская область
Амурской области
Архангельске, Архангельская область
Северодвинске
Архангельской области
Астрахани, Астраханская область
Знаменске, Астраханская область
Астраханской области
Башкортостане, регион
Уфе
Башкортостане, регион
Белгороде, Белгородская область
Старом Осколе
Белгородской области
Брянске, Брянская область
Клинцах, Брянская область
Брянской области
Бурятии
Улан-Удэ
Бурятии
Владимире, Владимирская область
Коврове
Владимирской области
Волгограде
Волжском, Волгоградская область
Волгоградской области
Вологде
Череповце
Вологодской области
Воронеже, Воронежская область
Россоши, Воронежская область
Воронежской области
Дагестане
Махачкале
Дагестане
Донецке, Донецкая Народная Республика
Горловке, Донецкая Народная Республика
Донецкой Народной Республике
Еврейской АО
Биробиджане
Еврейской АО
Забайкальском крае
Чите, Забайкальский край
Забайкальском крае
Запорожье, Запорожье
Бердянске
Запорожской области
Иваново, Ивановский район
Кинешме
Ивановской области
Ингушетии
Магасе
Ингушетии
Иркутске
Ангарске
Иркутской области
Кабардино-Балкарии
Нальчике (аэропорт)
Кабардино-Балкарии
Калининграде
Черняховске
Калининградской области
Калмыкии
Элисте
Калмыкии
Калуге, Калужская область
Обнинске
Калужской области
Камчатке
Петропавловске-Камчатском
Камчатке
Карачаево-Черкесии
Черкесске
Карачаево-Черкесии
Карелии
Петрозаводске
Карелии
Кирове, Кировская область
Кирово-Чепецке
Кировской области
Коми
Сыктывкаре
Коми
Костроме, Костромская область
Буе, Костромская область
Костромской области
Краснодаре, Краснодарский край
Сочи
Краснодарском крае
Красноярске, Красноярский край
Дудинке, Красноярский край
Красноярском крае
Крыму
Симферополе
Крыму
Кемеровской области
Новокузнецке
Кемеровской области
Кургане, Курганская область
Шадринске
Курганской области
Курске, Курская область
Железногорске, Курская область
Курской области
Ленинградской области
Киришах, Киришский район
Ленинградской области
Липецке
Ельце, Липецкая область
Липецкой области
Луганске, Луганская Народная Республика
Старобельске
Луганской Народной Республике
Магадане
Оле, Россия
Магаданской области
Марий Эл
Йошкар-Оле
Марий Эл
Мордовии
Саранске, Мордовия
Мордовии
Москве (ВДНХ)
Шереметьево, им. А. С. Пушкина (аэропорт)
Москве
Московской области
Подольске, Московская область
Московской области
Мурманске
Североморске
Мурманской области
Нижнем Новгороде
Дзержинске, Нижегородская область
Нижегородской области
Новгородской области
Великом Новгороде
Новгородской области
Новосибирске
Бердске
Новосибирской области
Омске
Таре, Омская область
Омской области
Орле, Орловская область
Ливнах, Орловская область
Орловской области
Оренбурге
Орске, Оренбургская область
Оренбургской области
Пензе, Пензенская область
Кузнецке
Пензенской области
Перми
Кудымкаре
Пермском крае
Приморье
Владивостоке
Приморье
Пскове
Великих Луках, Россия
Псковской области
Алтае
Горно-Алтайске
Алтае
Республике Саха (Якутии)
Якутске
Республике Саха (Якутии)
Ростове-на-Дону
Таганроге
Ростовской области
Рязани, Рязанская область
Касимове
Рязанской области
Самаре, Самарская область
Тольятти
Самарской области
Санкт-Петербурге
Колпино, Санкт-Петербург
Санкт-Петербурге, регион
Саратове
Энгельсе, Саратовская область
Саратовской области
Сахалине
Южно-Сахалинске
Сахалине
Свердловской области
Екатеринбурге
Свердловской области
Севастополе, Севастополь
Севастополе
Северной Осетии-Алании
Владикавказе
Северной Осетии-Алании
Смоленске
Вязьме, Смоленская область
Смоленской области
Ставрополе
Пятигорске, Россия
Ставропольском крае
Тамбове
Мичуринске, Тамбовская область
Тамбовской области
Татарстане, регион
Казани, Татарстан
Татарстане, регион
Твери
Ржеве
Тверской области
Томске
Северске, Томская область
Томской области
Туле, Тульская область
Новомосковске, Россия
Тульской области
Тыве, регион
Кызыле, Россия
Тыве, регион
Тюмени, Тюменская область
Тобольске
Тюменской области
Удмуртии
Ижевске
Удмуртии
Ульяновске
Димитровграде, Россия
Ульяновской области
Хабаровске
Комсомольске-на-Амуре
Хабаровском крае
Хакасии
Абакане
Хакасии
Ханты-Мансийске
Ханты-Мансийском автономном округе — Югре
Херсоне
Каховке, Херсонская область
Херсонской области
Челябинске
Магнитогорске
Челябинской области
Чечне
Грозном, Чечня
Чечне
Чувашии
Чебоксарах, Чувашия
Чувашии
Чукотском АО
Анадыре
Чукотском АО
Ямало-Ненецком автономном округе
Ямало-Ненецком автономном округе
Ярославле, Ярославская область
Рыбинске, Ярославская область
Ярославской области
Долгопрудном
Мытищах, Московская область
Химках
Реутове, Московская область
Москве (центр, Балчуг)
Москве (юг)
Москве (юго-запад, МГУ)
Шереметьево, им. А. С. Пушкина (аэропорт)
Абаза
Абакан
Абдулино
Абинск
Агидель
Агрыз
Адыгейск
Азнакаево
Азов
Ак-Довурак
Аксай
Алагир
Алапаевск
Алатырь
Алдан
Алейск
Александров
Александровск
Александровск-Сахалинский
Алексеевка
Алексин
Алзамай
Алупкане призн.
Алуштане призн.
Альметьевск
Амурск
Анадырь
Анапа
Ангарск
Андреаполь
Анжеро-Судженск
Анива
Апатиты
Апрелевка
Апшеронск
Арамиль
Аргун
Ардатов
Ардон
Арзамас
Аркадак
Армавир
Армянскне призн.
Арсеньев
Арск
Артём
Артёмовск
Артёмовский
Архангельск
Асбест
Асино
Астрахань
Аткарск
Ахтубинск
Ачинск
Ачхой-Мартан
Аша
Бабаево
Бабушкин
Бавлы
Багратионовск
Байкальск
Баймак
Бакал
Баксан
Балабаново
Балаково
Балахна
Балашиха
Балашов
Балей
Балтийск
Барабинск
Барнаул
Барыш
Батайск
Бахчисарайне призн.
Бежецк
Белая Калитва
Белая Холуница
Белгород
Белебей
Белёв
Белинский
Белово
Белогорск
Белогорскне призн.
Белозерск
Белокуриха
Беломорск
Белоозёрский
Белорецк
Белореченск
Белоусово
Белоярский
Белый
Бердск
Березники
Берёзовский
Берёзовский
Беслан
Бийск
Бикин
Билибино
Биробиджан
Бирск
Бирюсинск
Бирюч
Благовещенск
Благовещенск
Благодарный
Бобров
Богданович
Богородицк
Богородск
Боготол
Богучар
Бодайбо
Бокситогорск
Болгар
Бологое
Болотное
Болохово
Болхов
Большой Камень
Бор
Борзя
Борисоглебск
Боровичи
Боровск
Бородино
Братск
Бронницы
Брянск
Бугры
Бугульма
Бугуруслан
Будённовск
Бузулук
Буинск
Буй
Буйнакск
Бутурлиновка
Валдай
Валуйки
Велиж
Великие Луки
Великий Новгород
Великий Устюг
Вельск
Венёв
Верещагино
Верея
Верхнеуральск
Верхний Тагил
Верхний Уфалей
Верхняя Пышма
Верхняя Салда
Верхняя Тура
Верхотурье
Верхоянск
Весьегонск
Ветлуга
Видное
Вилюйск
Вилючинск
Вихоревка
Вичуга
Владивосток
Владикавказ
Владимир
Волгоград
Волгодонск
Волгореченск
Волжск
Волжский
Вологда
Володарск
Волоколамск
Волосово
Волхов
Волчанск
Вольск
Воркута
Воронеж
Ворсма
Воскресенск
Воткинск
Всеволожск
Вуктыл
Выборг
Выкса
Высоковск
Высоцк
Вытегра
Вышний Волочёк
Вяземский
Вязники
Вязьма
Вятские Поляны
Гаврилов Посад
Гаврилов-Ям
Гагарин
Гаджиево
Гай
Галич
Гатчина
Гвардейск
Гдов
Геленджик
Георгиевск
Глазов
Голицыно
Горбатов
Горно-Алтайск
Горнозаводск
Горняк
Городец
Городище
Городовиковск
Гороховец
Горячий Ключ
Грайворон
Гремячинск
Грозный
Грязи
Грязовец
Губаха
Губкин
Губкинский
Гудермес
Гуково
Гулькевичи
Гурьевск
Гурьевск
Гусев
Гусиноозёрск
Гусь-Хрустальный
Давлеканово
Дагестанские Огни
Далматово
Дальнегорск
Дальнереченск
Данилов
Данков
Дегтярск
Дедовск
Демидов
Дербент
Десногорск
Джанкойне призн.
Дзержинск
Дзержинский
Дивногорск
Дигора
Димитровград
Дмитриев
Дмитров
Дмитровск
Дно
Добрянка
Долгопрудный
Долинск
Домодедово
Донецк
Донской
Дорогобуж
Дрезна
Дубна
Дубовка
Дудинка
Духовщина
Дюртюли
Дятьково
Евпаторияне призн.
Егорьевск
Ейск
Екатеринбург
Елабуга
Елец
Елизово
Ельня
Еманжелинск
Емва
Енисейск
Ермолино
Ершов
Ессентуки
Ефремов
Железноводск
Железногорск
Железногорск
Железногорск-Илимский
Жердевка
Жигулёвск
Жиздра
Жирновск
Жуков
Жуковка
Жуковский
Завитинск
Заводоуковск
Заволжск
Заволжье
Задонск
Заинск
Закаменск
Заозёрный
Заозёрск
Западная Двина
Заполярный
Зарайск
Заречный
Заречный
Заринск
Звенигово
Звенигород
Зверево
Зеленогорск
Зеленоградск
Зеленодольск
Зеленокумск
Зерноград
Зея
Зима
Златоуст
Злынка
Змеиногорск
Знаменск
Зубцов
Зуевка
Ивангород
Иваново
Ивантеевка
Ивдель
Игарка
Ижевск
Избербаш
Изобильный
Иланский
Инза
Иннополис
Инсар
Инта
Ипатово
Ирбит
Иркутск
Исилькуль
Искитим
Истра
Ишим
Ишимбай
Йошкар-Ола
Кадников
Казань
Калач
Калач-на-Дону
Калачинск
Калининград
Калининск
Калтан
Калуга
Калязин
Камбарка
Каменка
Каменногорск
Каменск-Уральский
Каменск-Шахтинский
Камень-на-Оби
Камешково
Камызяк
Камышин
Камышлов
Канаш
Кандалакша
Канск
Карабаново
Карабаш
Карабулак
Карасук
Карачаевск
Карачев
Каргат
Каргополь
Карпинск
Карталы
Касимов
Касли
Каспийск
Катав-Ивановск
Катайск
Качканар
Кашин
Кашира
Кедровый
Кемерово
Кемь
Керчьне призн.
Кизел
Кизилюрт
Кизляр
Кимовск
Кимры
Кингисепп
Кинель
Кинешма
Киреевск
Киренск
Киржач
Кириллов
Кириши
Киров
Киров
Кировград
Кирово-Чепецк
Кировск
Кировск
Кирс
Кирсанов
Киселёвск
Кисловодск
Клин
Клинцы
Княгинино
Ковдор
Ковров
Ковылкино
Когалым
Кодинск
Козельск
Козловка
Козьмодемьянск
Кола
Кологрив
Коломна
Колпашево
Колтуши
Кольчугино
Коммунар
Комсомольск
Комсомольск-на-Амуре
Конаково
Кондопога
Кондрово
Константиновск
Копейск
Кораблино
Кореновск
Коркино
Королёв
Короча
Корсаков
Коряжма
Костерёво
Костомукша
Кострома
Котельники
Котельниково
Котельнич
Котлас
Котово
Котовск
Кохма
Красавино
Красноармейск
Красноармейск
Красновишерск
Красногорск
Краснодар
Краснозаводск
Краснознаменск
Краснознаменск
Краснокаменск
Краснокамск
Красноперекопскне призн.
Краснослободск
Краснослободск
Краснотурьинск
Красноуральск
Красноуфимск
Красноярск
Красный Кут
Красный Сулин
Красный Холм
Кремёнки
Кропоткин
Крымск
Кстово
Кубинка
Кувандык
Кувшиново
Кудрово
Кудымкар
Кузнецк
Куйбышев
Кукмор
Кулебаки
Кумертау
Кунгур
Купино
Курган
Курганинск
Курильск
Курлово
Куровское
Курск
Куртамыш
Курчалой
Курчатов
Куса
Кушва
Кызыл
Кыштым
Кяхта
Лабинск
Лабытнанги
Лагань
Ладушкин
Лаишево
Лакинск
Лангепас
Лахденпохья
Лебедянь
Лениногорск
Ленинск
Ленинск-Кузнецкий
Ленск
Лермонтов
Лесной
Лесозаводск
Лесосибирск
Ливны
Ликино-Дулёво
Липецк
Липки
Лиски
Лихославль
Лобня
Лодейное Поле
Лосино-Петровский
Луга
Луза
Лукоянов
Луховицы
Лысково
Лысьва
Лыткарино
Льгов
Любань
Люберцы
Любим
Людиново
Лянтор
Магадан
Магас
Магнитогорск
Майкоп
Майский
Макаров
Макарьев
Макушино
Малая Вишера
Малгобек
Малмыж
Малоархангельск
Малоярославец
Мамадыш
Мамоново
Мантурово
Мариинск
Мариинский Посад
Маркс
Махачкала
Мглин
Мегион
Медвежьегорск
Медногорск
Медынь
Межгорье
Междуреченск
Мезень
Меленки
Мелеуз
Менделеевск
Мензелинск
Мещовск
Миасс
Микунь
Миллерово
Минеральные Воды
Минусинск
Миньяр
Мирный
Мирный
Михайлов
Михайловка
Михайловск
Михайловск
Мичуринск
Могоча
Можайск
Можга
Моздок
Мончегорск
Морозовск
Моршанск
Мосальск
Москва
Муравленко
Мураши
Мурино
Мурманск
Муром
Мценск
Мыски
Мытищи
Мышкин
Набережные Челны
Навашино
Наволоки
Надым
Назарово
Назрань
Называевск
Нальчик
Нариманов
Наро-Фоминск
Нарткала
Нарьян-Мар
Наурская
Находка
Невель
Невельск
Невинномысск
Невьянск
Нелидово
Неман
Нерехта
Нерчинск
Нерюнгри
Нестеров
Нефтегорск
Нефтекамск
Нефтекумск
Нефтеюганск
Нея
Нижневартовск
Нижнекамск
Нижнеудинск
Нижние Серги
Нижний Ломов
Нижний Новгород
Нижний Тагил
Нижняя Салда
Нижняя Тура
Николаевск
Николаевск-на-Амуре
Никольск
Никольск
Никольское
Новая Ладога
Новая Ляля
Новоалександровск
Новоалтайск
Новоаннинский
Нововоронеж
Новодвинск
Новозыбков
Новокубанск
Новокузнецк
Новокуйбышевск
Новомичуринск
Новомосковск
Новопавловск
Новоржев
Новороссийск
Новосибирск
Новосиль
Новосокольники
Новотроицк
Новоузенск
Новоульяновск
Новоуральск
Новохопёрск
Новочебоксарск
Новочеркасск
Новошахтинск
Новый Оскол
Новый Уренгой
Ногинск
Нолинск
Норильск
Ноябрьск
Нурлат
Нытва
Нюрба
Нягань
Нязепетровск
Няндома
Облучье
Обнинск
Обоянь
Обь
Одинцово
Озёрск
Озёрск
Озёры
Ойсхара
Октябрьск
Октябрьский
Окуловка
Олёкминск
Оленегорск
Олонец
Омск
Омутнинск
Онега
Опочка
Орёл
Оренбург
Орехово-Зуево
Орлов
Орск
Оса
Осинники
Осташков
Остров
Островной
Острогожск
Отрадное
Отрадный
Оха
Оханск
Очёр
Павлово
Павловск
Павловский Посад
Палласовка
Партизанск
Певек
Пенза
Первомайск
Первоуральск
Перевоз
Пересвет
Переславль-Залесский
Пермь
Пестово
Петров Вал
Петровск
Петровск-Забайкальский
Петрозаводск
Петропавловск-Камчатский
Петухово
Петушки
Печора
Печоры
Пикалёво
Пионерский
Питкяранта
Плавск
Пласт
Плёс
Поворино
Подольск
Подпорожье
Покачи
Покров
Покровск
Полевской
Полесск
Полысаево
Полярные Зори
Полярный
Поронайск
Порхов
Похвистнево
Почеп
Починок
Пошехонье
Правдинск
Приволжск
Приморск
Приморск
Приморско-Ахтарск
Приозерск
Прокопьевск
Пролетарск
Протвино
Прохладный
Псков
Пугачёв
Пудож
Пустошка
Пучеж
Пушкино
Пущино
Пыталово
Пыть-Ях
Пятигорск
Радужный
Радужный
Райчихинск
Раменское
Рассказово
Ревда
Реж
Реутов
Ржев
Родники
Рославль
Россошь
Ростов-на-Дону
Ростов
Рошаль
Ртищево
Рубцовск
Рудня
Руза
Рузаевка
Рыбинск
Рыбное
Рыльск
Ряжск
Рязань
Сакине призн.
Салават
Салаир
Салехард
Сальск
Самара
Санкт-Петербург
Саранск
Сарапул
Саратов
Саров
Сасово
Сатка
Сафоново
Саяногорск
Саянск
Светлогорск
Светлоград
Светлый
Светогорск
Свирск
Свободный
Себеж
Севастопольне призн.
Северо-Курильск
Северобайкальск
Северодвинск
Североморск
Североуральск
Северск
Севск
Сегежа
Сельцо
Семёнов
Семикаракорск
Семилуки
Сенгилей
Серафимович
Сергач
Сергиев Посад
Сердобск
Серноводское
Серов
Серпухов
Сертолово
Сибай
Сим
Симферопольне призн.
Сковородино
Скопин
Славгород
Славск
Славянск-на-Кубани
Сланцы
Слободской
Слюдянка
Смоленск
Снежинск
Снежногорск
Собинка
Советск
Советск
Советск
Советская Гавань
Советский
Сокол
Солигалич
Соликамск
Солнечногорск
Соль-Илецк
Сольвычегодск
Сольцы
Сорочинск
Сорск
Сортавала
Сосенский
Сосновка
Сосновоборск
Сосновый Бор
Сосногорск
Сочи
Спас-Деменск
Спас-Клепики
Спасск
Спасск-Дальний
Спасск-Рязанский
Среднеколымск
Среднеуральск
Сретенск
Ставрополь
Старая Купавна
Старая Русса
Старица
Стародуб
Старый Крымне призн.
Старый Оскол
Стерлитамак
Стрежевой
Строитель
Струнино
Ступино
Суворов
Судакне призн.
Суджа
Судогда
Суздаль
Сунжа
Суоярви
Сураж
Сургут
Суровикино
Сурск
Сусуман
Сухиничи
Сухой Лог
Сызрань
Сыктывкар
Сысерть
Сычёвка
Сясьстрой
Тавда
Таганрог
Тайга
Тайшет
Талдом
Талица
Тамбов
Тара
Тарко-Сале
Таруса
Татарск
Таштагол
Тверь
Теберда
Тейково
Тельмана
Темников
Темрюк
Терек
Тетюши
Тимашёвск
Тихвин
Тихорецк
Тобольск
Тогучин
Тольятти
Томари
Томмот
Томск
Топки
Торжок
Торопец
Тосно
Тотьма
Трёхгорный
Троицк
Трубчевск
Туапсе
Туймазы
Тула
Тулун
Туран
Туринск
Тутаев
Тында
Тырныауз
Тюкалинск
Тюмень
Уварово
Углегорск
Углич
Удачный
Удомля
Ужур
Узловая
Улан-Удэ
Ульяновск
Унеча
Урай
Урень
Уржум
Урус-Мартан
Урюпинск
Усинск
Усмань
Усолье-Сибирское
Усолье
Уссурийск
Усть-Джегута
Усть-Илимск
Усть-Катав
Усть-Кут
Усть-Лабинск
Устюжна
Уфа
Ухта
Учалы
Уяр
Фатеж
Феодосияне призн.
Фокино
Фокино
Фролово
Фрязино
Фурманов
Хабаровск
Хадыженск
Ханты-Мансийск
Харабали
Харовск
Хасавюрт
Хвалынск
Хилок
Химки
Холм
Холмск
Хотьково
Цивильск
Цимлянск
Циолковский
Чадан
Чайковский
Чапаевск
Чаплыгин
Чебаркуль
Чебоксары
Чегем
Чекалин
Челябинск
Чердынь
Черемхово
Черепаново
Череповец
Черкесск
Чёрмоз
Черноголовка
Черногорск
Чернушка
Черняховск
Чехов
Чистополь
Чита
Чкаловск
Чудово
Чулым
Чусовой
Чухлома
Шагонар
Шадринск
Шали
Шарыпово
Шарья
Шатура
Шахты
Шахунья
Шацк
Шебекино
Шелехов
Шелковская
Шенкурск
Шилка
Шимановск
Шиханы
Шлиссельбург
Шумерля
Шумиха
Шуя
Щёкино
Щёлкиноне призн.
Щёлково
Щигры
Щучье
Электрогорск
Электросталь
Электроугли
Элиста
Энгельс
Эртиль
Югорск
Южа
Южно-Сахалинск
Южно-Сухокумск
Южноуральск
Юрга
Юрьев-Польский
Юрьевец
Юрюзань
Юхнов
Ядрин
Якутск
Ялтане призн.
Ялуторовск
Янаул
Яранск
Яровое
Ярославль
Ярцево
Ясногорск
Ясный
Яхрома
'''
cities = name_city_txt.strip().split('\n')

# Открываем файл для записи в формате CSV
with open('A:/Language-processor/name_city_extended.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Записываем заголовок
    writer.writerow(['city'])

    # Записываем каждый город в новую строку
    writer.writerows([[city] for city in cities])

print("Данные записаны в 'name_city_extended.csv'")