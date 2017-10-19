from os.path import dirname, join

APP_PATH = dirname(__file__)
ROOT_PATH = dirname(APP_PATH)

SETTINGS = dict(
    template_path=join(ROOT_PATH, 'templates'),
    static_path=join(ROOT_PATH, 'static'),
)
