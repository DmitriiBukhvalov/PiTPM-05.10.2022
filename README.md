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
![image](https://user-images.githubusercontent.com/101401186/206916741-407f89d5-e28e-4bf8-9bba-e99e1dfc209b.png)

    Принимаемая информация: Пользователь добавлен

2. GET http://127.0.0.1:3005/user
    body:
        
        {
        
            "name": "Dima",
    
            "surname": "Buhvalov",
        
            "password": "sdfsdf",
    
            "group": "isp-320p"
    
        }
![image](https://user-images.githubusercontent.com/101401186/206916751-df7343c0-6cb2-4a64-828c-680a3b5e0315.png)

    Принимаемая информация: Dima Buhvalov sdfsdf isp-320p


3. PUT http://127.0.0.1:3005/user/0
    body:
        
        {
        
            "name": "Sasha"
    
        }
![image](https://user-images.githubusercontent.com/101401186/206916761-e5cb9584-b588-47d6-af65-a46a6bdd56f7.png)
    Принимаемая информация: Пользователь изменен



4. GET http://127.0.0.1:3005/user
    body:
        
        {
    
        }

![image](https://user-images.githubusercontent.com/101401186/206916876-5e0d72a2-fb97-401b-9547-d9e04184420c.png)

    Принимаемая информация: Sasha Buhvalov sdfsdf isp-320p


5. DELETE http://127.0.0.1:3005/user/0
    body:
        
        {
    
        }
![image](https://user-images.githubusercontent.com/101401186/206916886-d0888163-97bd-48ef-a39d-50edeaa368f4.png)

    Принимаемая информация: Пользователь удален



Музыка

1. POST http://127.0.0.1:3005/music
    body:
    {
    
        "name": "Dora -  Автопилот",
    
        "data": "2022",
        
        "album": "MISS"
    
    
    }

![image](https://user-images.githubusercontent.com/101401186/206917057-119b38ee-7a8b-4777-a948-e82496989332.png)

    Принимаемая информация: Музыка добавлена



2. GET http://127.0.0.1:3005/music
    body:
    {
    
        "name": "Dora -  Автопилот",
    
        "data": "2022",
        
        "album": "MISS"
    
    
    }
    ![image](https://user-images.githubusercontent.com/101401186/206917052-3e7c9c78-8f5e-42cf-b838-ebecf114fe49.png)

    Принимаемая информация: Dora - Автопилот 2022 MISS


3. PUT http://127.0.0.1:3005/music/0
    body:
    {
    
        "name": "Dora -  Нет тебя"
    
    }
    ![image](https://user-images.githubusercontent.com/101401186/206917062-8659b7f0-b2ca-4a85-9be5-cc67ab567fa9.png)

    Принимаемая информация: Музыка изменена


4. GET http://127.0.0.1:3005/music/0
    body:
    {
    
    }
    ![image](https://user-images.githubusercontent.com/101401186/206917085-f76d8b9c-ede9-4df9-813b-ac2104d72621.png)

    Принимаемая информация: Dora - Нет тебя 2022 MISS


5. DELETE http://127.0.0.1:3005/music/0
    body:
    {
    
    }
    ![image](https://user-images.githubusercontent.com/101401186/206917091-9e138ba6-b98f-41d7-a82d-58ede7939fbc.png)

    Принимаемая информация: Музыка удалена
