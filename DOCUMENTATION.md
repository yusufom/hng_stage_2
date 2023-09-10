# Introduction

This is the solution to backend stage two task for the HNG intership

## Use Cases

The use case for this api is to get, create, update or delete a Person object with name

## UML model
![alt text](https://github.com/yusufom/hng_stage_2/blob/main/uml.png?raw=true)


## Request


```http
GET /api/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | **Required**.  |

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
GET /api/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `Olamilekan` | **Required**.  |

#### Response
```javascript
{
  "id" : 1,
  "name" : "Olamilekan",
}
```

### Create Person

#### Request

```http
POST /api/create/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `Olamilekan` | **Required**.  |

#### Response
```javascript
{
  "id" : 1,
  "name" : "Olamilekan",
}
```

### Update Person

#### Request

```http
PUT /api/update/Olamilekan/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `Adewale` | **Required**.  |

#### Response
```javascript
{
  "id" : 1,
  "name" : "Adewale",
}
```

### Delete Person

#### Request

```http
DELETE /api/delete/Olamilekan/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `Adewale` | **Required**.  |

#### Response
```javascript
{
  "message" : "Olamilekan has been Deleted",
}
```



## Status Codes

Gophish returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

