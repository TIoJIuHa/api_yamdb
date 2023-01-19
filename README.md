# Групповой проект - API_YAMDB

**Разработчики:**
- [Елистратова Полина](https://github.com/TIoJIuHa)
- [Саидов Ратмир](https://github.com/RatmirSaidov)
- [Шапченко Дмитрий](https://github.com/dltt1)

### Стек технологий:

<div>
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"/>
  <img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
</div>


### Описание

Проект выполнен в учебных целяx для курса Яндекс.Практикума. **YaMDb** собирает отзывы пользователей на произведения. Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число). Пользователи могут оставлять комментарии к отзывам.

[Полная документация по API (redoc.yaml)](api_yamdb\static\redoc.yaml)

#### Алгоритм регистрации пользователей

  1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.
  2. **YaMDB** отправляет письмо с кодом подтверждения (`confirmation_code`) на адрес  `email`.
  3. Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен).
  4. При желании пользователь отправляет PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполняет поля в своём профайле (описание полей — в документации).

#### Пользовательские роли

  - **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
  - **Аутентифицированный пользователь** (`user`) — может, как и **Аноним**, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять **свои** отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
  - **Модератор** (`moderator`) — те же права, что и у **Аутентифицированного пользователя** плюс право удалять **любые** отзывы и комментарии.
  - **Администратор** (`admin`) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям. 
  - **Суперюзер Django** — обладет правами администратора (`admin`)

### Как запустить проект

Клонировать репозиторий и перейти в папку с проектом:
```
git clone <project_url>
```
```
cd api_yamdb
```

Установить и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate (Windows OS)
source venv/bin/activate (Mac OS)
```

Установить необходимые зависимости из `requirements.txt`:
```
pip install -r requirements.txt
```

Перейти в папку с файлом `manage.py`:
```
cd api_yamdb
```

Выполнить миграции:
```
python manage.py migrate
```

Создать суперпользователя:
```
python manage.py createsuperuser
```

И запустить проект:
```
python manage.py runserver
```
