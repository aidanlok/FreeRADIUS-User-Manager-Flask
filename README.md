# FreeRADIUS-User-Manager-Flask
This repository contains the files required to run the FreeRADIUS user manager Flask server as described in my YouTube video.

**Note: you must run this Flask server with sudo to allow the server to change the FreeRADIUS configuration, as the server needs elevated permissions to access the configuration file.**

# Files

1. [app.py](./app.py)

This file is the Flask server that reads the configuration, allows you to edit the configuration, and save the configuration to disk.

2. [templates/index.html](./templates/index.html)

This file provides the HTML that the Flask server renders as the web GUI.

3. [freeradius_flask_manager.service](./freeradius_flask_manager.service)

This file is used if you want to set up a systemctl service for the Flask server.
