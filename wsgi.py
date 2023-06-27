import sys, site

sys.path.insert(0,'/home/michael/flaskapp')

python_home = '/home/michael/flaskapp/env'

# Calculate path to site-packages directory.
python_version = '.'.join(map(str, sys.version_info[:2]))
site_packages = python_home + '/lib/python%s/site-packages' % python_version

# Add the site-packages directory.
site.addsitedir(site_packages)

from website import create_app

application = create_app()

if __name__ == "__main__":
    application.run()

