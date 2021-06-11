import threading ,webbrowser
from flask import Flask, render_template, jsonify
import input

app = Flask(__name__)

print('モジュール名：{}'.format(__name__))

# 分割したモジュールを読み込み
app.register_blueprint(input.input_module)

@app.route('/')
def hello():
    app.logger.debug(__name__)
    title = 'indexページ'
    message = 'リストを渡してみる'
    shikoku_list = ['愛媛県', '高知県', '徳島県', '香川県']
    return render_template('index.html', title=title, message=message, shikoku=shikoku_list)
 

if __name__ == "__main__":
    threading.Timer(1.0, lambda: webbrowser.open('http://localhost:8000') ).start()
    app.run(port=8000, debug=True)