## API для продуктов и работа с фронтендом


### Клонируем репозиторий

```
    git clone https://github.com/molodcovnik/test_catalog_products.git
```


### Инструкция по запуску приложения

```
    cd test_catalog_products
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt
    python app/manage.py runserver
```

### Запуск тестов

```
    python app/manage.py test catalog
```
