# Folder for the flask server that will run on the Raspberry Pi

To start the server, navigate to the flask-server folder and execute `flask run`. This should start the app server locally in flask.

Next, run `ngrok http --domain=randomly-verified-jaguar.ngrok-free.app 5000`. This will connect the flask server to a publicly available endpoint, which will allow the Alexa to poll it.
