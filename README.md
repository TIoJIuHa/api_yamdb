# ГРУППОВОЙ ПРОЕКТ - API_YAMDB
Стек технологий использованный в проекте: Python 3, Django 2.2.16, Django JWT 4.7.2

Разработчики:
- [Елистратова Полина](https://github.com/TIoJIuHa)
- [Саидов Ратмир](https://github.com/RatmirSaidov)
- [Шапченко Дмитрий](https://github.com/dltt1)
## Описание
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории (Genre). Список категорий может быть расширен администратором.

Проект реализован при помощи следующих технологий:

<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"/>
<img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white"/>
<img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"/>
<img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"/>

### Алгоритм регистрации пользователей
  1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.
  2. **YaMDB** отправляет письмо с кодом подтверждения (`confirmation_code`) на адрес  `email`.
  3. Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен).
  4. При желании пользователь отправляет PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполняет поля в своём профайле (описание полей — в документации).

### Пользовательские роли
  - **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
  - **Аутентифицированный пользователь** (`user`) — может, как и **Аноним**, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять **свои** отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
  - **Модератор** (`moderator`) — те же права, что и у **Аутентифицированного пользователя** плюс право удалять **любые** отзывы и комментарии.
  - **Администратор** (`admin`) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям. 
  - **Суперюзер Django** — обладет правами администратора (`admin`)
## Как запустить проект:
Клонировать репозиторий:

```
- git clone https://github.com/TIoJIuHa/api_yamdb.git
- cd api_yamdb
```

Установить и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/Scripts/activate (Windows OS)
source venv/bin/activate (Mac OS)
```
Установить необходимые зависимости requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py makemigrations
python manage.py migrate
```
Создаем суперпользователя:

```
python manage.py createsuperuser
```
Запустить проект:

```
python manage.py runserver
```