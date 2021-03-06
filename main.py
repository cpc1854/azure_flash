import urllib
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

def get_webpage(url):
    #html = myHtml.get_webpage(url)
    req = urllib.request.Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req).read()



@app.route('/')
def hello_world():
      return 'Hey its Python Flask application on Azure!'

'''
def index():
    return render_template(
        'indexh.html',**locals())
'''

@app.route('/rss')
def rss():
    url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    xml = get_webpage(url)
    return xml


if __name__ == '__main__':
  app.run()
