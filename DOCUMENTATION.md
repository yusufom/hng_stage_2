# Introduction

This document provides information on how to use the API endpoints, standard request and response formats, sample usage, and instructions for setting up and deploying the API.

### Base URL

```
https://person-nsnx.onrender.com/api/
```
## Use Cases

The use case for this api is to get, create, update or delete a Person object with name


## Request


```http
GET https://person-nsnx.onrender.com/api/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | **Required**.  |

```http
POST https://person-nsnx.onrender.com/api/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | **Required**.  |


```http
PUT https://person-nsnx.onrender.com/api/:name/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | **Required**.  |

```http
DELETE https://person-nsnx.onrender.com/api/:name/
```

## Responses

The api endpoint returns a JSON representation of the resource created or edit.

```javascript
{
  "id" : int,
  "name" : string,
}
```
The `id` attribute is the primary unique key automatically assigned to the created resource upon creation.

The `name` attribute is the name field of the resource.

However, if an invalid request is submitted, or some other error occurs, the api returns a JSON response in the following format:

```javascript
{
  "message" : string,
}
```

The delete endpoint also returns a response similar to other error responses with a message.

```javascript
{
  "message" : string,
}
```

The `message` attribute contains a message commonly used to indicate errors or, in the case of deleting a resource, success that the resource was properly deleted.

## Example request and responses

### Get Person

#### Request

```http
GET https://person-nsnx.onrender.com/api/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `Olamilekan` | **Required**.  |

```json
{
  "name": "Olamilekan",
}
```

#### Response

- **Success Response (HTTP Status Code: 200 OK):**

```json
{
  "id" : 1,
  "name" : "Olamilekan",
}
```
- **Error Response (HTTP Status Code: 404 Not Found):**
```json
{
  "message" : "Not found",
}
```

### Create Person

#### Request

```http
POST https://person-nsnx.onrender.com/api/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `Olamilekan` | **Required**.  |
```json
{
  "name": "Olamilekan",
}
```

#### Response
- **Success Response (HTTP Status Code: 200 OK):**
```json
{
  "id" : 1,
  "name" : "Olamilekan",
}
```
- **Error Response (HTTP Status Code: 400 Bad Request):**
```json
{
  "message" : "Olamilekan already exist",
}
```

### Update Person

#### Request

```http
PUT https://person-nsnx.onrender.com/api/Olamilekan/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `Adewale` | **Required**.  |

```json
{
  "name": "Adewale",
}
```

#### Response
- **Success Response (HTTP Status Code: 200 OK):**
```javascript
{
  "id" : 1,
  "name" : "Adewale",
}
```
- **Error Response (HTTP Status Code: 404 Bad Request):**
```json
{
  "message" : "Not found",
}
```
### Delete Person

#### Request

```http
PUT https://person-nsnx.onrender.com/api/Olamilekan/
```

#### Response
- **Success Response (HTTP Status Code: 200 OK):**
```json
{
  "message" : "Olamilekan has been Deleted",
}
```
- **Error Response (HTTP Status Code: 404 Not Found):**
```json
{
  "message" : "Not found",
}
```



## Status Codes

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

