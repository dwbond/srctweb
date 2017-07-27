from flask import Flask
from flask.ext.gravatar import Gravatar
from flask_frozen import Freezer

website = Flask(__name__)
freezer = Freezer(website)

from website import views

# initialize gravatar defaults
gravatar = Gravatar(website,
                    size = 80,
                    rating='g',
                    default='mm',
                    force_default=False,
                    use_ssl=True,
                    base_url=None)
