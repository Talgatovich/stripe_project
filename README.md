# Stripe project


### Локальный запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Talgatovich/stripe_project.git
```

```
cd  stripe_project/

```
### 1. Через Dockerfile

#### Перейти в папку с Докерфайлом

```
cd payment/
```
#### Создать образ
```
docker build -t payment .
```
#### Создать и запустить контейнер
```
docker run --name payment_container -it -p 8000:8000 payment 
```
#### Введите в адресную строку браузера localhost:8000: приложение запущено и работает!

### 2. Не используя Dockerfile:

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Перейти в директорию с файлом manage.py:

```
cd payment/
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Перейти по адресу http://127.0.0.1:8000/

### Проект временно доступен по [ссылке](http://84.201.142.213:8000)

