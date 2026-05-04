from flask import Flask
from flask_cors import CORS
from config import Config
from routes.auth_routes import auth_bp
from models.db import mysql
from routes.protected_routes import protected_bp
from routes.project_routes import project_bp
from routes.task_routes import task_bp


app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
mysql.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')

# Register Blueprints
app.register_blueprint(protected_bp, url_prefix='/api')

# Register other blueprints
app.register_blueprint(project_bp, url_prefix='/api')
app.register_blueprint(task_bp, url_prefix='/api')

@app.route('/')
def home():
    return {"message": "Team Task Manager API Running 🚀"}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)