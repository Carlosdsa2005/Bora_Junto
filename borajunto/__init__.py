from flask import Flask

def create_app(config_name=None):
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    if config_name == "testing":
        import os
        os.environ["FLASK_ENV"] = "testing"

    from borajunto.ext.config import init_app as init_config
    init_config(app)

    from borajunto.ext.db import init_app as init_db
    init_db(app)

    from borajunto.ext.login import init_app as init_login
    init_login(app)

    from borajunto.ext.wtf import init_app as init_wtf
    init_wtf(app)

    # ---> ADICIONE O CÓDIGO DO ADMIN AQUI <---
    from borajunto.ext.admin import init_app as init_admin
    init_admin(app)

    from borajunto.views import init_app as init_views
    init_views(app)

    from borajunto import cli
    cli.init_app(app)

    return app