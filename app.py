from flask import Flask, render_template_string

app = Flask(__name__)

html_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <!-- Здесь должна быть ссылка на картинку -->
    <img src="https://img.freepik.com/premium-psd/3d-mars-planet-isolated-white-background_1314158-4877.jpg?semt=ais_hybrid&w=740" alt="Марсианский пейзаж"/>
    <p>:Это Марс. Круто не так ли?.</p>
</body>
</html>
'''

@app.route('/')
def mission():
    return "Миссия Колонизация Марса"

@app.route('/index')
def slogan():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br>
Человечеству мала одна планета.<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
И начнем с Марса!<br>
Присоединяйся!"""

@app.route('/image_mars')
def image_mars():
    return render_template_string(html_page)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)