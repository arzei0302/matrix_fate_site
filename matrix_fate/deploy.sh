#!/bin/bash

# Перемещаемся в папку проекта
cd /opt/matrix_fate

# Сохраняем текущие изменения в файлах config (если они были изменены)
git stash push --keep-index -- "backup config files"

# Обновляем код из репозитория
git pull

# Восстанавливаем изменения в каталоге config
git stash pop

# Обновляем зависимости
pip install -r requirements.txt

# Применяем миграции
python manage.py migrate

# Собираем статику
python manage.py collectstatic --noinput

# Перезапускаем службы
systemctl restart celery
systemctl restart redis-server

# Перезапускаем Nginx (если используется)
systemctl restart nginx

echo "Deploy complete!"
