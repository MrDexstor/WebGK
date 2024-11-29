# Режим работы с тестовым сервером
Develop_Server_Connect = False

# Режим тестирования интерфейса с заготовленными данными
Disight_Mode = False
# TODO: Добавить функционал режима дизайнера

# Включение модуля POS_Scanner в приложении
POS_ScannerAllowed = True

# Ссылка на корень сайта (основной домен)
Root_Url = 'http://127.0.0.2:8097'

# Точка доступа магазина
BO_Urls = 'http://bo-o003.x5.ru:8096'

# Включить загрузку информации о текущем состоянии задач
Cookie_WorkerEnabled = True

# Идентификатор аккаунта сотрулника IT
Service_Account = 1


# Обработчики настроек 
def BO_Url():
    if Develop_Server_Connect:
        return 'http://127.0.0.1:8096'
    else:
        return BO_Urls