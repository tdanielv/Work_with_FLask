
from flask import Flask, render_template


app = Flask(__name__)
# @app.route('/albums/1')
# def hello_world():
#     return 'Hello, Flask'
#
#
# @app.route('/albums/<int:album_number>')
# def albums(album_number):
#     return 'The {} album.'.format(album_number)
#
#
# @app.route('/albums/<int:album_number>/<song_number>')
# def album(album_number, song_number):
#     return 'The {} album and {} musician performer.'.format(album_number, song_number)

# @app.route('/')
# def calc():
#     return render_template('index.html')

# @app.route('/<int:numb>/')
# def index(numb):
#     return render_template('index.html', number = numb*2, text = 'Ваше число {}, умноженное на 2: {}'.format(numb, numb*2))

template = '''
    {%if symbol == '+'%}
        {{first+second}}
    {%elif symbol == '-'%}
        {{first-second}}
    {%elif symbol == '**'%}
        {{first**second}}
    {%elif symbol ==':'%}
        {% if second != 0.0%}
            {{first/second}}
        {% else %}
            {{Ошибка}}
        {%endif%}
    {%elif symbol == '*'%}
        {{first*second}}
    {%else%}
        {{Ошибка}}
    {%endif%}
'''
@app.route('/<float:first>/<string:symbol>/<float:second>/')
def index(first, symbol, second):
    return render_template('index.html',  first=first, second=second, symbol=symbol)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
