from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route('/')
def hello_world():
      return 'Hey its Python Flask application on Azure!'

'''
def index():
    return render_template(
        'indexh.html',**locals())
'''
if __name__ == '__main__':
  app.run()
