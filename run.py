from flask import Flask
from app.routes import register_routes
from app.config import Config

def create_app():
    app = Flask(__name__, template_folder='app/views/templates')
    app.config.from_object(Config)
    register_routes(app)
    return app


app = create_app()

if __name__ == '__main__':
    print(f"Running in {app.config['ENVIRONMENT']} mode")
    app.run(host="0.0.0.0", port=5001, debug=app.config["DEBUG"])