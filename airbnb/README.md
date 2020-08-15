# Airbnb clone

## 준비사항

* django
* tailwind
* postgresql
* etc...

## 개발환경

```
$ python -m venv venv  
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## 실행

```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py {seed_user, seed_amenities,  seed_facilities, seed_roomtype, seed_rooms, send_reservations, seed_reviews}
```
