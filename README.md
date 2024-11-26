# Maverick - the extensible reddit bot

Maverick is a reddit bot that you can easily add new functionality to.
Just write a new function in `instances.py` and add it to the
`functions` list in `main.py`.

Note: Maverick is written purely in Python 3 (>=3.5), it *may* run
on Python 2 but we do not recommend or support it.

## How to run

*These instructions are meant to set you up quickly with a development
environment, production config would be different.*

Clone the repository and cd into it.

    $ git clone https://github.com/sahkanishk01/Maverick_A Reddit Bot
    $ cd Maverick

Create config file by running the following command:

    $ cp config.sample.py config.py

Fill out the username and password of the bot in the config file.

Create a new reddit app by going [here](https://www.reddit.com/prefs/apps/).
The app should be of type `script for personal use`.

Fill out the `CLIENT_ID` and `CLIENT_SECRET` fields of config.py now from
the app created.

Ideally we recommend using [venv](https://docs.python.org/3/tutorial/venv.html) for
dev purposes, so create a virtualenv and install all dependencies.

    $ sudo apt install python3-venv # for ubuntu
    $ python3 -m venv .
    $ source bin/activate
    $ pip install -r requirements.txt

Get an access token by running the following command and fill the field in
`config.py` with it.

    $ python get_token.py

Everything should be set up now.

    $ python main.py

In order to deactivate the virtual environment, just run `deactivate`.

## License Notice

```
Maverick - the extensible reddit bot

Copyright (C) 2017 Rashi Sah
Copyright (C) 2017 Param Singh

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
```
