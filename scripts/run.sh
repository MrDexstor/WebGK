cd ~/WebGK/
echo 'Загрузка ядра сервера'
screen -wipe
echo 'Удалены устаревшие сессии'
screen -dmS rsgk
echo 'Создан рабочий стол сервера'
screen -S rsgk -X screen scripts/web.sh
screen -S rsgk -X screen scripts/redis.sh
screen -S rsgk -X screen scripts/celery.sh
echo 'Отданы все команды запуска'