from flask import Blueprint, render_template, request
 
input_module = Blueprint("input", __name__)

print('モジュール名：{}'.format(__name__))

@input_module.route('/input', methods=['GET'])
def input():
  return render_template('input.html', title='入力ページ')

@input_module.route('/input', methods=['POST'])
def output():
  name = request.form['name']
  age = request.form['age']
  return render_template('output.html', name=name, age=age, title='出力ページ')
