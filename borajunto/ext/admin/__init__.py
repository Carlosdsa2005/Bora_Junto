from flask_admin import Admin
from borajunto.ext.db import db
from borajunto.models.user import User
from borajunto.models.trip import Trip
from borajunto.ext.admin.views import UserAdmin, TripAdmin

admin = Admin(name="BoraJunto Admin")

def init_app(app):
    admin.init_app(app)
    admin.add_view(UserAdmin(User, db.session, name="Usuários"))
    admin.add_view(TripAdmin(Trip, db.session, name="Viagens"))