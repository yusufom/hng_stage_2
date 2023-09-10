# Introduction

This is the solution to backend stage two task for the HNG intership.
This guide is based on the assumption that you already have python 3.10 and venv installed on your machine

## Clone the repo

```bash
git clone https://github.com/yusufom/hng_stage_2.git
```

## Test script

```bash
cd ./scripts
```
```python
python create_person.py
python get_person.py
python update_person.py
python delete_person.py
```

## Create virtualenv

```bash
virtualenv env
```

## Activate virtualenv

```bash
source env/bin/activate
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Run server

```bash
python manage.py runserver
```