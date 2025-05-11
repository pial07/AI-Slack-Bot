import os
import ssl
from celery import Celery

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pialhome.settings")

# Create the Celery app
app = Celery('pialhome')

# Configure Celery using Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Explicitly set the broker_use_ssl with the correct SSL options
# This is a backup in case the settings aren't being properly loaded
app.conf.update(
    broker_use_ssl={
        'ssl_cert_reqs': ssl.CERT_NONE,
        'ssl_check_hostname': False
    }
)

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()


# import os

# from celery import Celery

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pialhome.settings")

# app = Celery('pialhome') # celery -A cfehome
# app.config_from_object("django.conf:settings", namespace="CELERY")
# app.autodiscover_tasks()

