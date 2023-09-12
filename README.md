# Person API Introduction

This is the solution to backend stage two task for the HNG intership.
This guide is based on the assumption that you already have python 3.10 and venv installed on your machine

## UML model
![alt text](https://github.com/yusufom/hng_stage_2/blob/main/uml.png?raw=true)
## Getting Started

Before you begin, make sure you have the following prerequisites:

- Python version 3.10 and venv installed on your machine.

## Installation
1. Clone the repo

```bash
git clone https://github.com/yusufom/hng_stage_2.git
```

2. Create virtualenv

```bash
virtualenv env
```

3. Activate virtualenv

```bash
source env/bin/activate
```

4. Install Requirements

```bash
pip install -r requirements.txt
```

5. Make database migrations

```bash
python manage.py makemgrations
```

6. Migrate database
```bash
python manage.py migrate
```

7. Run server

```bash
python manage.py runserver
```

### Test script

```bash
cd ./scripts
```
1. Create Person
```python
python create_person.py
python get_person.py
python update_person.py
python delete_person.py
```
2. Get Person
```python
python get_person.py
```

3 Delete Person
```python
python delete_person.py
```

4. Update Person
```python
python update_person.py
```

## Endpoints

### Create a Person

- **Endpoint**: `POST /api/`
- **Description**: Create a new person with a name
- **Request Body**:

```json
{
  "name": "John Doe",
}
```

- **Response**:

```json
{
  "id": 1,
  "name": "John Doe",
}
```

### Get a Person by Name

- **Endpoint**: `POST /api/:id`
- **Description**: get a person by their ID
- **Request Body**:


- **Response**:

```json
{
  "id": 1,
  "name": "John Doe",
}
```

### Update a Person by Name

- **Endpoint**: `PUT /api/:id`
- **Description**: Update a person's id by a new name
- **Request Body**:

```json
{
  "name": "Updated Name",
}
```

- **Response**:

```json
{
  "id": 1,
  "name": "Updated Name",
}
```

### Delete a Person by Name

- **Endpoint**: `DELETE /api/:id`
- **Description**: Delete a person by their ID.
- **Response**:

```json
{
  "message": "{name} has been deleted successfully",
}
```

## Error Handling

- If the provided ID does not exist, you will receive a `404 Not Found` response.
- If the request body does not contain valid name and value fields, you will receive a `400 Bad Request` response.
- If you navigate to an invalid page, you will receive a `500 Internal Server Error` response.