from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class UserAdmin(SecureModelView):
    column_list = ["id", "name", "email", "is_active"]
    form_excluded_columns = ["password_hash", "created_at"]

class TripAdmin(SecureModelView):
    column_list = ["id", "title", "destination", "start_date"]