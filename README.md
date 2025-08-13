# Sprint 5 UI Автотесты

Автотесты на Selenium + Pytest для учебного сервиса «Доска».

## 📦 Установка

```bash
pip install -r requirements.txt
```

## 🚀 Запуск тестов

```bash
pytest -v --tb=short
```

## 📂 Структура

```
Sprint_5/
│
├── locators/ — локаторы элементов
│   ├── __init__.py
│   ├── auth_page_locators.py
│   ├── main_page_locators.py
│   ├── ad_page_locators.py
│
├── tests/ — тестовые сценарии
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_create_ad.py
│
├── utils/ — вспомогательные функции
│   ├── __init__.py
│   └── helpers.py
│
├── conftest.py
├── README.md
├── .gitignore
├── requirements.txt
```

locators/ — локаторы элементов

tests/ — тестовые сценарии

utils/ — генерация email и ожидания

conftest.py — фикстура драйвера