from flask import Flask,request,jsonify

app = Flask(__name__)


#Пустые массивы 
db_users = []

db_music = []



#Классы для заполнения данных
class User:
    def __init__(self, name, password, surname, group):
        self.name = name
        self.surname = surname
        self.password = password
        self.group = group

class Music:
    def __init__(self, name, album, year):
        self.name = name
        self.album = album
        self.year = year

#Пользователь



@app.route('/user', methods=['POST', 'GET'])
def user():

#Запись пользователя в файлик\объекта
    if request.method == 'POST':
        data = request.get_json()
        if (data == False and []):
            return "Данные не заполнены", 403
        if (data['name'] == ''):
            return "Имя не заполнено", 403

    
        
        name = data['name']
        password = data['password']
        surname = data['surname']
        group = data['group']
        user = User(name, password, surname, group)

        db_users.append(user)

        return "Пользователь добавлен", 200
        return jsonify(data)

#Получение пользователя из файлика\объекта

    if request.method == "GET":
        i = ''
        for u in db_users:
            user = u.name + " " + u.surname + " " + u.password + " " + u.group
            i += user

        return i, 200


        

@app.route('/user/<int:id>', methods=['PUT', "DELETE"])

def user_id(id):

#Удаление из объекта человека

    if request.method == 'DELETE':
        db_users.pop(id)
        return "Пользователь удален", 200

#Редактирование данных

    if request.method == "PUT":
        data = request.get_json();
        if data:
            if 'name' in data:
                db_users[id].name = data['name']
            if 'password' in data:
                db_users[id].password = data['password']
            if 'surname' in data:
                db_users[id].surname = data['surname']
            if 'group' in data:
                db_users[id].group = data['group']

        else:
            return "Нет данных", 403

        return "Пользователь изменен", 200

#Музыка

@app.route('/music', methods=['POST', 'GET'])
def music():

#Запись музыки в файлик\объекта
    if request.method == 'POST':
        data = request.get_json()
        if (data == False and []):
            return "Данные не заполнены", 403
        if (data['name'] == ''):
            return "Имя не заполнено", 403

    
        
        name = data['name']
        year = data['year']
        album = data['album']
        music = Music(name, year, album)

        db_music.append(music)

        return "Музыка добавлена", 200
        return jsonify(data)

#Получение музыки из файлика\объекта

    if request.method == "GET":
        i = ''
        for u in db_music:
            music = u.name + " " + u.album + " " + u.year
            i += music

        return i, 200


@app.route('/music/<int:id>', methods=['PUT', "DELETE"])

def music_id(id):

#Удаление музыки

    if request.method == 'DELETE':
        db_music.pop(id)
        return "Музыка удалена", 200

#Редактирование музыки

    if request.method == "PUT":
        data = request.get_json();
        if data:
            if 'name' in data:
                db_music[id].name = data['name']
            if 'album' in data:
                db_music[id].password = data['album']
            if 'year' in data:
                db_music[id].year = data['year']

        else:
            return "Нет данных", 403

        return "Музыка изменена", 200



if __name__ == "__main__":
    data = request.json()
    app.run(port=3005)