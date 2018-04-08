# Pushit

Quick demo to demonstrate the use of firebase web push notifications with the use of `javascript` on frontend, `django` on backend and push notifications via `fcm-django` pypi package for django.

## Quick start

### prerequisites
- in `pushit`:
  - create virtual environment with `python -m virtualenv env` (or `python -m venv env` in Python 3)
  - activate virtual environment with `. env/bin/activate`
  - install necessary Python packages with `pip install -r mysite/requirements.txt`

### frontend
- in `pushit/frontend`:
  - run server with `python -m http.server 8001`

### backend
- in `pushit/mysite`:
  - run database migrations with `python manage.py migrate`
  - create Django administrator with `python manage.py createsuperuser`
  - collect static files with `python manage.py collectstatic`
  - run server with `python manage.py runserver 0.0.0.0:8000`.

### how to use
- open http://localhost:8001 in your browser of choice
- request token and allow firebase to send notifications to your browser (device)
- you should now be seeing your instance id token on the aforementioned URL
- if you go to django admin, http://localhost:8000/admin/fcm_django/fcmdevice/, you should be seeing a FCMDevice instance for your browser
- send yourself a test notification with django admin actions
  - shell example (run `python manage.py shell` from `pushit/mysite`):
    ```python
	   from fcm_django.models import FCMDevice
	   device = FCMDevice.objects.all().first()
	   device.send_message(title='title', body='message')
    ```
- Enjoy! :)

### optional HTTPS support
- *why would you want to do this?* because service workers will not work on http, unless you are running them on localhost
- generate certificate and key with `openssl req -nodes -new -x509 -keyout key.pem -out cert.pem` in `pushit`
- in `pushit/frontend`:
  - update URL protocol to `https` and `localhost` to your server's IP address in [index.html](https://github.com/xtrinch/pushit/blob/b8d552830de2b5d82e2d3f787e98d160160c0844/frontend/index.html#L194)
  - run frontend server with `python server.py` 
- in `pushit/mysite`:
  - add your server's IP address to allowed hosts in project settings (shell example: `echo "ALLOWED_HOSTS = ['172.20.1.10']" > mysite/local_settings.py`)
  - run backend server with `python manage.py runsslserver --certificate ../cert.pem --key ../key.pem 0.0.0.0:8000`
- testing this demo in Chrome may require to run it with `--ignore-certificate-errors` flag to avoid SSL certificate fetch errors
- during the testing allow untrusted connections to the demo servers on browser prompt

### fcm-django DRF API URL docs demo

- available via `coreapi` and `djangorestframework` pypi packages, can be accessed at http://localhost:8000/docs
