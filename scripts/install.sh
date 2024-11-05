apt install python redis screen 
pip install celery Django tzdata redis requests
cd ~/WebGK
cp scripts/k.sh ~/
cd scripts
chmod 777 *.sh
cd ..
cd ..
chmod 777 *.sh
cd WebGK
python manage.py makemogrations
python manage.py migrate
echo 'Требуется регестрация поользователей соследующим ролями: Соотрудник IT, Директор Магазина'
echo 'Соотрудник IT:'
python manage.py createsuperuser
echo 'Директор магазина:'
python manage.py createsuperuser
cd ~
