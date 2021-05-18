# Overview
This repository contains an example that demonstrates a flask application using mod_wsgi.
The example is a adapted from the [flask-restful library](https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example) and provides CRUD operations on users.
## Deployment
- From the ICP Catalog, select `Infineon Python` Builder image and provide a path to the repository.
## Testing
Following `GET` endpoints are available
- `/`: Shows a message
- `/users`: Displays a list of users

For other endpoints, have a look in the [wsgi.py](wsgi.py) file.