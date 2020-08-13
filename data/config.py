import os
from flask_appbuilder.security.manager import (
    AUTH_OID,
    AUTH_REMOTE_USER,
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
)

basedir = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

# The SQLAlchemy connection string.
#SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
# SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
SQLALCHEMY_DATABASE_URI = 'postgresql://kore-number-mngnt-db:user-number-mngnt@172.30.33.41/kore-number-mngnt-db'

# Flask-WTF flag for CSRF
#CSRF_ENABLED = True

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
# Uncomment to setup Your App name
APP_NAME = "Optus NUMs"

# Uncomment to setup Setup an App icon
#APP_ICON = "/static/ico.png"
APP_ICON = "data:image/png;base64,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"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_DB

# Uncomment to setup Full admin role name
# AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
# AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
# AUTH_USER_REGISTRATION = True

# The default user self registration role
# AUTH_USER_REGISTRATION_ROLE = "Public"

# When using LDAP Auth, setup the ldap server
# AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
# OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = "en"
# Your application default translation path
BABEL_DEFAULT_FOLDER = "translations"
# The allowed translation for you app
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
#    "pt": {"flag": "pt", "name": "Portuguese"},
#    "pt_BR": {"flag": "br", "name": "Pt Brazil"},
#    "es": {"flag": "es", "name": "Spanish"},
#    "de": {"flag": "de", "name": "German"},
#    "zh": {"flag": "cn", "name": "Chinese"},
#    "ru": {"flag": "ru", "name": "Russian"},
#    "pl": {"flag": "pl", "name": "Polish"},
}
# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload url, when using models with images
IMG_UPLOAD_URL = "/static/uploads/"
# Setup image size default is (300, 200, True)
# IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
# APP_THEME = "bootstrap-theme.css"  # default bootstrap
# APP_THEME = "cerulean.css"         # COOL
#APP_THEME = "amelia.css"            #Optus style
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"           # COOL
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
APP_THEME = "slate.css"              # COOL
# APP_THEME = "spacelab.css"         # NICE
# APP_THEME = "united.css"
# APP_THEME = "yeti.css"
