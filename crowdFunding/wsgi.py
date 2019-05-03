"""
<<<<<<< HEAD
WSGI config for crowdFunding08 project.
=======
WSGI config for crowdFunding project.
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crowdFunding08.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crowdFunding.settings')
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d

application = get_wsgi_application()
