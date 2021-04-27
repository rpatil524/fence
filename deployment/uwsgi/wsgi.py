import os

from fence import app_init, app

app_init(app)
application = app

application.debug = os.environ.get("GEN3_DEBUG") == "True"
