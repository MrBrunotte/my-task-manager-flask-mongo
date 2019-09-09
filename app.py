import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World ...again and again'
"""
if __name__ == '__main__':
    # NEVER HAVE DEBUG=TRUE IN PRODUCTION OR WHEN SUBMITTING!!!
    app.run(debug=True)
"""
"""
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='localhost', port=port)
"""

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

