from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mission():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lines = (
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!",
    )

    return "<br>".join(lines)


@app.route('/image_mars')
def image_mars():
    return f"<b>Жди нас, Марс!</b><br>" \
           f"<img src={url_for('static', filename='img/MARS.png')}>" \
           f"<p>Вот она какая, красная планета</p>"


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                     <link rel="stylesheet"
                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                     crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}" />
                    <title>Пример загрузки файла</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1><br>
                    <img src={url_for('static', filename='img/MARS.png')}>
                    <p class="alert alert-secondary">Человечество вырастает из детства.</p>
                    <p class="alert alert-success">Человечеству мала одна планета.</p>
                    <p class="alert alert-dark">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class="alert alert-warning">И начнем с Марса!</p>
                    <p class="alert alert-danger">Присоединяйся!</p>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
