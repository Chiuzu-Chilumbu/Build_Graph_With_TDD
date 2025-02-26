from flask import Flask
from app.routes import register_routes
from app.config import config

def create_app():
    app = Flask(__name__, template_folder='app/views/templates')
    app.config.from_object(config)
    register_routes(app)
    return app

# ✅ Move this line outside the `if __name__ == '__main__'` block
app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5001, debug=True)