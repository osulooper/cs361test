from flask import Flask, render_template, request, redirect
import webbrowser
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/my-link/', methods=['GET', 'POST'])
def my_link():
  url = request.args.get('url')
  suffix = request.args.get('suffix')
  target = request.args.get('languages')
  return redirect('https://www-' + url + '-' + suffix + '.translate.goog/?_x_tr_sl=en&_x_tr_tl='+ target + '&_x_tr_hl=en&_x_tr_pto=wapp')

if __name__ == '__main__':
  app.run(debug=True)