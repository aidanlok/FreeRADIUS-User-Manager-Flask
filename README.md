# FreeRADIUS-User-Manager-Flask
This Flask server provides an interface for managing the users allowed to authenticate through a FreeRADIUS server. This server provides a web GUI, which you can use to add and delete users. When finished editing, click the "Save Changes" button to write the configuration to disk.

**Note: you must run this Flask server with sudo to allow the server to change the FreeRADIUS configuration, as the server needs elevated permissions to access the configuration file.**

# Files

1. [app.py](./app.py)

This file is the Flask server that reads the configuration, allows you to edit the configuration, and save the configuration to disk.

2. [templates/index.html](./templates/index.html)

This file provides the HTML that the Flask server renders as the web GUI.

3. [freeradius_flask_manager.service](./freeradius_flask_manager.service)

This file is used if you want to set up a systemctl service for the Flask server.
