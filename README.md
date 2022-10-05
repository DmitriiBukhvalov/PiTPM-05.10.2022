# PiTPM 05.10.2022

Отчет
Бухвалов Дмитрий


Пользователи

1. POST http://127.0.0.1:3005/user
    body:
    {
    
        "name": "Dima",
    
        "surname": "Buhvalov",
        
        "password": "sdfsdf",
    
        "group": "isp-320p"
    
    }

    Принимаемая информация: Пользователь добавлен

2. GET http://127.0.0.1:3005/user
    body:
        
        {
        
            "name": "Dima",
    
            "surname": "Buhvalov",
        
            "password": "sdfsdf",
    
            "group": "isp-320p"
    
        }

    Принимаемая информация: Dima Buhvalov sdfsdf isp-320p


3. PUT http://127.0.0.1:3005/user/0
    body:
        
        {
        
            "name": "Sasha"
    
        }

    Принимаемая информация: Пользователь изменен


4. GET http://127.0.0.1:3005/user
    body:
        
        {
    
        }

    Принимаемая информация: Sasha Buhvalov sdfsdf isp-320p


5. DELETE http://127.0.0.1:3005/user/0
    body:
        
        {
    
        }

    Принимаемая информация: Пользователь удален



Музыка

1. POST http://127.0.0.1:3005/music
    body:
    {
    
        "name": "Dora -  Автопилот",
    
        "data": "2022",
        
        "album": "MISS"
    
    
    }
    
    Принимаемая информация: Музыка добавлена



2. GET http://127.0.0.1:3005/music
    body:
    {
    
        "name": "Dora -  Автопилот",
    
        "data": "2022",
        
        "album": "MISS"
    
    
    }
    
    Принимаемая информация: Dora - Автопилот 2022 MISS


3. PUT http://127.0.0.1:3005/music/0
    body:
    {
    
        "name": "Dora -  Нет тебя"
    
    }
    
    Принимаемая информация: Музыка изменена


4. GET http://127.0.0.1:3005/music/0
    body:
    {
    
    }
    
    Принимаемая информация: Dora - Нет тебя 2022 MISS


5. DELETE http://127.0.0.1:3005/music/0
    body:
    {
    
    }
    
    Принимаемая информация: Музыка удалена
