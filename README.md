# business_system

# Business Management System (Django)

## Опис
Інформаційна система для керування бізнес-процесами малого підприємства. Реалізовано функціонал обліку товарів, керування замовленнями, контролю залишків та базової адміністрації.

## Можливості
- Додавання та редагування товарів
- Категоризація продукції
- Створення вхідних та вихідних замовлень
- Зв’язки між товарами і замовленнями
- Зменшення/збільшення залишків товару на складі
- Адмін-панель для керування всіма сутностями

## Використані технології
- Python 3.13
- Django 5.2
- PostgreSQL
- Django Admin

## Встановлення

1. Клонувати репозиторій:
```bash
git clone https://github.com/your-username/business-system.git
cd business_system
```

2. Створити та активувати віртуальне середовище:
```bash
python -m venv .venv
source .venv/bin/activate   # або .venv\Scripts\activate для Windows
```

3. Встановити залежності: 
```bash
pip install -r requirements.txt
```

4. Налаштувати .env або settings.py з параметрами БД.

5. Застосувати міграції:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Створити адміністратора:
```bash
python manage.py createsuperuser
```

7. Запустити сервер:
```bash
python manage.py runserver
```

Доступ до адмінки
Перейдіть за посиланням: http://127.0.0.1:8000/admin/
Увійдіть під логіном/паролем створеного суперкористувача.

## Модульна структура
- inventory: товари, категорії, склад
- orders: замовлення та позиції замовлень
- users: користувачі системи





























