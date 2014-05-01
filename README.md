screenshots
===========

Automated screenshots for a list of URLs at various device widths.

## Requirements

Install setuptools, pip and brew the NPR News Apps way:
http://blog.apps.npr.org/2013/06/06/how-to-setup-a-developers-environment.html

Create a virtual environment to isolation your packages:

`mkvirtualenv screenshots`

## Install necessary python packages:

1. `brew install imagemagick`
1. `pip install selenium`
1. `ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install imgdiff`

## Clone the project and modify settings

1. `cd path/to/project/`
1. `git clone git@github.com:gotoplanb/screenshots.git`
1. `cp settings-example.py settings.py`
1. Edit `screenshot.py` to comment out the login section if you don't need authentication stuff
1. Edit `bootstrap.py` to comment out the login section if you don't need authentication stuff
1. Edit `settings.py` and add as many URLs as you want to screenshot
1. Run `python bootstrap.py` to create the first batch of images. You just have to do this once.

## Get new screenshots

`python screenshot.py`