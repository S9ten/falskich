from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/index')
def index():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route('/')
def main():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/promotion')
def promotion():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Рекламная компания</title>
                  </head>
                  <body>
                    <h1>Человечество вырастает из детства.</h1>
                    <h1>Человечеству мала одна планета.</h1>
                    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                    <h1>И начнем с Марса!</h1>
                    <h1>Присоединяйся!</h1>
                  </body>
                </html>"""


@app.route('/image_sample')
def image():
    return f'''	<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                   </head>
                    <body>
                        <link rel="stylesheet" type="text/css"
                         href="{url_for('static',
                                        filename='css/style.css')}" />
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" 
                               alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
