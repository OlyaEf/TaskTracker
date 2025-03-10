TaskTrackerTest
Django REST Framework Python

📌 Описание проекта
TaskTracker — это минималистичный API на Django REST Framework для управления задачами.

🔹 Функции API:

Получение списка задач (GET /tasks/)
Создание новой задачи (POST /tasks/)
Валидация поля title (не может быть пустым)

🚀 Установка и запуск
1. Клонирование репозитория
git clone git@github.com:OlyaEf/TaskTrackerTest.git
cd DjangoProject
2. Установка зависимостей
Убедитесь, что у вас установлен Poetry:

poetry install
3. Настройка переменных окружения
Создайте файл .env в корне проекта и добавьте:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
4. Применение миграций
python manage.py makemigrations
python manage.py migrate
5. Запуск сервера
python manage.py runserver

📍 API будет доступен по адресу: http://127.0.0.1:8000/tasks/

📡 Использование API
1. Получение списка задач
Метод: GET
URL: /tasks/
Пример ответа:
[
    {
        "id": 1,
        "title": "Купить продукты",
        "is_completed": false
    }
]
2. Создание новой задачи
Метод: POST
URL: /tasks/
Тело запроса (JSON):
{
    "title": "Новая задача"
}
Пример ответа:
{
    "id": 2,
    "title": "Новая задача",
    "is_completed": false
}

📂 Структура проекта
TaskTrackerTest/
DjangoProject/
│── tasks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│── DjangoProject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── manage.py
│── poetry.lock
│── pyproject.toml
│── .gitignore
│── README.md
⚙️ Технологии
Python 3.12
Django 5.1
Django REST Framework 3.15.2
Poetry (управление зависимостями)

🎯 Автор
📌 OlyaEf
📧 efimovskikh@gmail.com

📜 Лицензия
Проект распространяется под лицензией MIT. Используйте на своё усмотрение! 🚀
