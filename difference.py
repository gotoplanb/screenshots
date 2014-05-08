import os
import subprocess
import selenium.webdriver as webdriver
import contextlib
import base64

with open("new/desktop/desktop changing.png", "rb") as image_file:
    new_encoded_string = base64.b64encode(image_file.read())

with open("old/desktop/desktop changing.png", "rb") as image_file:
    old_encoded_string = base64.b64encode(image_file.read())

if (new_encoded_string == old_encoded_string):
	print('Same.')
else:
	print('Different.')