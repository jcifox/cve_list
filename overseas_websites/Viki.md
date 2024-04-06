# About Viki Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie:_cfuvid=hbeB.2xgQOS26X0B6BLFKGZPOAwQCxTNQNCay79EDvU-1712127143589-0.0.1.1-604800000; path=/; domain=.vimeo.com; HttpOnly; Secure; SameSite=None
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: username.

> Request method: GET, information can be obtained by traversing user id,such as "6056115u","18105409u"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params |
|---------|---|-----------|
|Yizhimuzhu666|https://api.viki.io/v4/contributors/6056115u/count.json|6056115u|



### Leaked packet cases 
``` 
{
    "user_id": "6056115u",
    "username": "*******",
    "subtitles_count": 72285,
    "segments_count": 29,
    "ratings_count": 27,
    "suggestions_count": 37
}
```