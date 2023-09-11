# het
Финансовый ассистент для ведения семейного бюджета

# Запуск
```bash
cd het
source venv/Scripts/activate
cd het
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Перейти на `http://127.0.0.1:8000/expenses/expenses/`

# Получение изменений
```bash
git checkout dev
git pull
git checkout front
git merge dev
git push
```

# Комиит
Из корневой папки .../dev/het/
```bash
git add .
git commit -m "Назване коммита"
git push
```

# Новое изменение
Из ветки front
```bash
git checkout -b "feature-..."
git commit -m "Название коммита"
git push
```
В ветке `"feature-..."` закомитить все изменения!

# Слияние с веткой front
```bash
git checkout front
git merge "feature-..."
git push
```