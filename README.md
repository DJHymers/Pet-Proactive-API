Challenge A: Python API Challenge

We want you to create a Flask API which listens for a JSON message on a public facing URI
( web address ). You should write the API using Flask and it should listen to POST requests.
The JSON in the POST request should be formatted like this.

{“command”: “greeting”, “name”: “alex”}

The ‘command’ parameter should always be ‘greeting’ but the ‘name’ parameter value can
be changed to any name. If the JSON is correct, the API will respond with the following
where ‘alex’ is replaced with the ‘name’ parameter value from the request.

{“response”: “hello alex”}

If the JSON request is not correct the response should be a 403 Forbidden error.
You may enhance the API to respond to other commands, and you may make any
assumptions you wish.

https://europe-west2-python-api-challenge-399713.cloudfunctions.net/flask-api
