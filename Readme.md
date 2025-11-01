# ЭлектроЦепь 

Онлайн платформа-торговой сети электроники: веб-приложение с API-интерфейсом и админ-панелью, в которой реализованы:
1. CRUD-операции
2. Миграции с БД(Субд: Postgresql)
3. Создана Авто-документация с помощью: swagger и redoc
4. Проект покрыт тестами на 87%

# Инструкция по установке и использованию разработанного функционала приложения
1. Клонируйте репозиторий:
```
git clone https://github.com/4usnok/electro_chain.git
```
2. Установите зависимости:
```
poetry install
```
3. Активировать окружение
```
poetry shell
```
# Содержание проекта  
## Приложение `network`  
1. `models.py`:  
ContactsFactory -> Модель для контактов  
ProductsFactory -> Модель для продукта  
Network -> Модель для сети  

2. `serializers.py`  
NetworkSerializer -> Сериализатор для модели Network  

3. `views.py`:  
NetworkList -> Просмотр списка сетей  
NetworkDetail -> Просмотр одной сети  
NetworkCreate -> Создание новой сети  
NetworkUpdate -> Редактирование сети  
NetworkDelete -> Удаление сети  

4. `urls.py`:  
`network_list/` -> маршрут для NetworkList  
`new_network/` -> маршрут для NetworkCreate  
`<int:pk>/detail_network/` -> маршрут для detail_network  
`<int:pk>/delete_network/` -> маршрут для delete_network  
`<int:pk>/update_network/` -> маршрут для update_network  
`swagger/` -> авто-документация swagger  
`redoc/` -> авто-документация redoc  

## Прочие файлы  
1. `Readme.md` -> Описание проекта  
2. `.env.sample` -> Шаблон для переменных окружения, которые заполняются в новом `.env` в первую очередь  
3. `gitignore` -> текстовый файл, который сообщает, какие файлы и папки следует игнорировать  
и не отслеживать в репозитории  
4. `pyproject.toml` -> файл конфигурации для проекта  

# Работа с программой  
1. запуск приложения: `python manage.py runserver`  

# Полезные команды  
* Запуск сервера: `python manage.py runserver`,  
* Создание суперюзера(админка): `python manage.py createsuperuser`,  
* Создание миграций: `python manage.py makemigrations`,  
* Сохранение миграций: `python manage.py migrate`,  
* Откат всех миграций: `python manage.py migrate name_migration`, где `name_migration` -> название миграции.  
* Создание фикстуры для модели пользователей `User`: `python -Xutf8 manage.py dumpdata users.User --output users_fixture.json --indent 4`  
* Создание фикстуры для модели платежей `Payments`: `python -Xutf8 manage.py dumpdata users.Payments --output payments_fixture.json --indent 4`  
* Создания файла с покрытием `.coverage`: `coverage run --source='.' manage.py test`  
* Посмотреть покрытие unit-тестами: `coverage report`  