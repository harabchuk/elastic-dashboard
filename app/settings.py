from os import path

APP_PATH = path.dirname(path.dirname(__file__))

SETTINGS = dict(
    template_path=path.join(APP_PATH, 'templates'),
    static_path=path.join(APP_PATH, 'static'),
)
