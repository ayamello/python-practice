# Python Practice - Leads

Registration, listing, updating and removal of Leads. 

<blockquote> 
  Leads these are people who may be interested in some type of product or service. 
</blockquote>

### Objective

Practice crud with python

### Deploy

https://e15-leads-ayana.herokuapp.com/

### Techs
	
- Python
- Flask
- Postgresql
- SQLAlchemy
- Flask-Migrate
- Flask-SQLAlchemy
- Psycopg2
- Heroku 
- Gunicorn

### Routes

#### Create a lead

`POST /leads - Request format`
```json
{
  "name": "Pythian",   
  "email": "pythian@mail.com",
  "phone": "(XX)XXXXX-XXXX"
}
```

#### List all leads

`GET /leads - Response format - STATUS 200`
```json
[
 {
  "creation_date": "Thu, 12 Nov 2021 02:24:42 GMT",
  "email": "pythian@mail.com",
  "last_visit": "Thu, 12 Nov 2021 02:24:42 GMT",
  "name": "Pythian",
  "phone": "(55)99789-2341",
  "visits": 1
 }
]
```

#### Update number of visits for a lead 

`PATCH /leads - Request format`
```json
{
 "email": "pythian@mail.com",
}
```

`PATCH /leads - Response format - STATUS 200`
```json
{
 "creation_date": "Thu, 12 Nov 2021 02:24:42 GMT",
 "email": "pythian@mail.com",
 "last_visit": "Thu, 20 Dez 2021 12:41:43 GMT",
 "name": "Pythian",
 "phone": "(55)99789-2341",
 "visits": 2
}
```

#### Delete one lead

`DELETE /leads - Request format`
```json
{
 "email": "pythian@mail.com",
}
```
