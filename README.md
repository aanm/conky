Conky
=====
This repository provides a public copy of my conky config.

conky_config
-----
To make it your own, you have to change lines 72, 76, 156 from conky_config.
72: Put the mount directory of your external HDD or Pen Drive. If you don't use
external HDD and/or Pen Drives, please delete this line and lines 100-102.
76: Change $USER to your user name and put the repository's files inside
/home/$USER/.conky/ directory.
156: If you use a 3G bundle you can try and see if the signal.sh script gives
any value for the 3G bundle signal.

If you use Nvidia Drivers (oficial drivers) uncomment lines 107-110.

weather_update.py
-----
This is a small python script to download weather data from openweathermap.org
It's necessary to register in order to get a API ID
see more info here: http://openweathermap.org/appid

You can find your city's ID by searching in:
http://openweathermap.org/find?q=

You need to change lines 35 and 36 in order for this script work.

Dependencies: https://pypi.python.org/pypi/python-dateutil

fonts/
-----
I can't remember from where I have downloaded these fonts. I didn't create any of
them and unfortunatelly don't know who the author is. They are fundamental
for conky output to be pretty.