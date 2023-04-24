# Lab-10
Лабораторная работа №10

Голосовой ассистент.

**Задание**

1. Используя библиотеки ```requests```, ```pyttsx3```, ```pyaudio``` и ```Vosk``` (или сходную по функционалу), реализовать голосового ассистента, умеющего распознавать не менее четырех разных команд. Название команд и их назначение остаётся на усмотрение студента, указанные в варианте примеры команд приводятся для ориентира. Может быть предложена своя тема голосового ассистента. Язык может быть как русским, так и английским.

Обработка ошибок: не распознана команда, ошибка в запросе.

**Варианты**

1. Сайт https://dog.ceo/api/breeds/image/random Примеры команд: "показать", "сохранить" (сохранение как файл), "следующая" (обновление картинки), "назвать породу" (есть в тексте ссылки), "разрешение" (сказать разрешение в пикселях).  
2. Сайт https://date.nager.at/api/v2/publicholidays/2020/GB Примеры команд: "перечислить" (только названия), "сохранить" (файл с названиями), "даты" (файл с датами и названиями), "ближайший" (сказать ближайший к дате праздник), "количество". Страну и год можно поменять.  
3. Сайт https://rickandmortyapi.com/api/character/108 Примеры команд: "случайный" (сказать имя случайного персонажа), "сохранить" (сохраняет картинку), "эпизод" (назвать эпизод первого появления), "показать" (вывести картинку), "разрешение" (назвать разрешение в пикселях).  
4. Сайт https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/rub.json Примеры команд "доллар" (курс к доллару), "евро" (курс к евро), "сохранить" (сохранить в виде списка в файл), "количество", "случайный" (сказать курс к случайной валюте).  
5. Сайт https://randomuser.me/api/ Примеры команд: "создать" (создаёт пользователя), "имя" (сказать имя), "страна" (назвать страну), "анкета" (сформировать анкету в свободной форме с основными данными), "сохранить" (сохраняет фотографию).  
6. Сайт https://www.boredapi.com/api/activity Примеры команд: "случайный" (показать занятие), "название" (сказать название), "участники" (сказать, сколько нужно человек), "следующая" (сгенерировать следующее занятие), "сохранить" (создать файл).  
7. Сайт https://v2.jokeapi.dev/joke/Any?safe-mode Примеры команд: "создать" (генерация новой шутки), "тип" (высказывание или диалог), "прочесть", "категория" (сказать категорию), "записать" (дописать шутку в конец заранее созданного файла).  
8. Сайт https://go-apod.herokuapp.com/apod Примеры команд: "создать", "описание" (прочесть описание), "вывести" (вывод изображения), "сохранить" (сохранить изображение как файл), "заголовок" (прочесть заголовок).  
9. Сайт https://wttr.in/Saint-Petersburg?format=2 Примеры команд: "погода", "ветер", "направление", "записать", "прогулка" (ответ "не рекомендуется" при погоде холоднее +5 или силе ветра больше 15 км/ч, значение можно взять свои).  
10. Сайт http://numbersapi.com/random/math Примеры команд: "факт", "следующий" (сгенерировать новый), "прочитать" (прочесть факт), "записать" (записать в конец созданного файла), "удалить" (стереть последний записанный факт из файла).  

**Дополнительное задание**

Сайт https://api.dictionaryapi.dev/api/v2/entries/en/<слово (англ.)> Ввести команду на поиск информации по сказанному слову. Примеры команд: "сохранить", "значение" (сказать значение), "ссылка" (открыть ссылку в браузере), "пример" (сказать пример). Выполняется **вместо** основного задания.

**Полезные ссылки**

Голосовая модель VOSK для русского языка (компактная): https://disk.yandex.ru/d/BB6pZZSfqLsW4Q  
О создании голосовых ассистентов: https://temofeev.ru/info/articles/sozdanie-golosovogo-assistenta-na-python-chast-1/
