import sys, os

# Add this project to python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

app.debug = app.config['DEBUG']

if __name__ == "__main__":
    app.run()