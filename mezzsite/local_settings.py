# -*- coding: utf-8 -*-
# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = False

# Make these unique, and don't share it with anybody.
SECRET_KEY = "qas*601g+p#*h*-bv85dyu%$iu1@#&36i3a#t6%o95zds&-514"
NEVERCACHE_KEY = "p%&ozyzi#ryth779hu_k-naqc@d4%bvm6^nz)gq*g$@kg1i5u2"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        #"django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "mysite",
        # Not used with sqlite3.
        "USER": "mezzanine",
        # Not used with sqlite3.
        "PASSWORD": "mezzanine",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "115.28.242.182",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "3306",
    }
}

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
# ALLOWED_HOSTS = [""]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }
