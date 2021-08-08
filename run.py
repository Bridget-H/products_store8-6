from app.models import User
from app import app, db
#CART^^

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
    }