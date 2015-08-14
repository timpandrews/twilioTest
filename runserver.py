from os import environ
from application import app

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
