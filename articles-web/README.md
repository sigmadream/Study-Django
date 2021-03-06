# Django 초급밥

## 1. VSCode를 설치하자.

VSCode의 `Live Server`와 `Python` 확장 패키지를 설치하자.

## 2. 시작하기

[Materialize](https://materializecss.com/)에서 'Parallax Template'을 다운받고, 기본적인 레이아웃(HTML/CSS/JS)를 구성하자.

## 3. `.gitignore.io`를 활용해서, 불필요한 파일을 미리 정리하자.

`python`,`venv`,`vscode`,`pycharm+all`,`django` 등을 설정하자.

## 4. `Django` 설치

```shell
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install django
(venv) $ django-admin startproject config .
(venv) $ python manage.py runserver        
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 29, 2021 - 14:39:30
Django version 3.1.5, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C. 
```

## 5. App 생성

