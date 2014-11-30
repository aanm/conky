#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a small python script to download weather data from openweathermap.org
It's necessary to register in order to get a API ID
see more info here: http://openweathermap.org/appid

You can find your city ID by searching in:
http://openweathermap.org/find?q=
"""

import xml.etree.ElementTree as ET
import os.path, time
import urllib
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from collections import defaultdict
from decimal import Decimal

__author__ = "André Martins"
__copyright__ = "Copyright 2014"
__credits__ = "André Martins"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "André Martins"
__email__ = "aanm90@gmail.com"
__status__ = "Stable"

now = datetime.now()

######################
#  Changeable stuff  #
######################
yourAPIID = ""
yourCITYID = ""
yourUNITS = "metric"

update = now - relativedelta(minutes=+30)
first = now + relativedelta(hours=+8)
second = now + relativedelta(days=+1, hour=12, minutes=0)
third = now + relativedelta(days=+2, hour=12, minutes=0)
conkyfile = '/tmp/conky_results'

#######################
# Non-changable stuff #
#######################
currentweather = '/tmp/conky_current.xml'
forecast = '/tmp/conky_forecast.xml'

# Checking the last time an update was made
update_file = True
if os.path.isfile(currentweather) and os.path.isfile(forecast):
 last_update = parse(time.ctime(os.path.getmtime(currentweather)))
 update_file = update >= last_update

if update_file:
 urllib.urlretrieve("http://api.openweathermap.org/data/2.5/weather?id=" + yourCITYID + "&APPID=" + yourAPIID + "&mode=xml&units=" + yourUNITS + "", currentweather)
 urllib.urlretrieve("http://api.openweathermap.org/data/2.5/forecast/city?id=" + yourCITYID + "&APPID=" + yourAPIID + "&mode=xml&units=" + yourUNITS + "", forecast)
 urllib.urlcleanup()

#Hack to reuse inside the same list for the current and next moments
#next_moment_index_data = current_moment_index_data = value
time = last_current_update = 0
day = 1
hour = cur_temp = 2
max_temp = wind_speed = 3
min_temp = wind_dir = 4
icon = 5
prec = 6

moments = defaultdict(list)
moments[0] = [now, None, None, None, None, '-', None]
moments[1] = [first, None, None, None, None, '-', None]
moments[2] = [second, None, None, None, None, '-', None]
moments[3] = [third, None, None, None, None, '-', None]

weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temp_units = {'celsius':'ºC', 'imperial':'ºF'}

####
# Table made accordingly with http://openweathermap.org/weather-conditions
# icons[ID] = [Day, Night, Description]
####
icons = defaultdict(list)
icons[200] = ['k', 'K', 'thunderstorm with light rain']
icons[201] = ['l', 'l', 'thunderstorm with rain']
icons[202] = ['m', 'm', 'thunderstorm with heavy rain']
icons[210] = ['l', 'l', 'light thunderstorm']
icons[211] = ['l', 'l', 'thunderstorm']
icons[212] = ['n', 'n', 'heavy thunderstorm']
icons[221] = ['n', 'n', 'ragged thunderstorm']
icons[230] = ['l', 'l', 'thunderstorm with light drizzle']
icons[231] = ['m', 'm', 'thunderstorm with drizzle']
icons[232] = ['m', 'm', 'thunderstorm with heavy drizzle']
icons[300] = ['g', 'G', 'light intensity drizzle']
icons[301] = ['s', 's', 'drizzle']
icons[302] = ['t', 't', 'heavy intensity drizzle']
icons[310] = ['g', 'G', 'light intensity drizzle rain']
icons[311] = ['h', 'h', 'drizzle rain']
icons[312] = ['i', 'i', 'heavy intensity drizzle rain']
icons[313] = ['j', 'j', 'shower rain and drizzle']
icons[314] = ['j', 'j', 'heavy shower rain and drizzle']
icons[321] = ['j', 'j', 'shower drizzle']
icons[500] = ['g', 'G', 'light rain']
icons[501] = ['h', 'h', 'moderate rain']
icons[502] = ['i', 'i', 'heavy intensity rain']
icons[503] = ['j', 'j', 'very heavy rain']
icons[504] = ['j', 'j', 'extreme rain']
icons[511] = ['x', 'x', 'freezing rain']
icons[520] = ['g', 'G', 'light intensity shower rain']
icons[521] = ['h', 'h', 'shower rain']
icons[522] = ['i', 'i', 'heavy intensity shower rain']
icons[531] = ['j', 'j', 'ragged shower rain']
icons[600] = ['o', 'O', 'light snow']
icons[601] = ['p', 'p', 'snow']
icons[602] = ['q', 'q', 'heavy snow']
icons[611] = ['y', 'y', 'sleet']
icons[612] = ['x', 'x', 'shower sleet']
icons[615] = ['x', 'x', 'light rain and snow']
icons[616] = ['x', 'x', 'rain and snow']
icons[620] = ['x', 'x', 'light shower snow']
icons[621] = ['x', 'x', 'shower snow']
icons[622] = ['x', 'x', 'heavy shower snow']
icons[701] = ['0', '0', 'mist']
icons[711] = ['0', '0', 'smoke']
icons[721] = ['0', '0', 'haze']
icons[731] = ['7', '7', 'sand', 'dust whirls']
icons[741] = ['0', '0', 'fog']
icons[751] = ['7', '7', 'sand']
icons[761] = ['7', '7', 'dust']
icons[762] = ['7', '7', 'volcanic ash']
icons[771] = ['6', '6', 'squalls']
icons[781] = ['1', '1', 'tornado']
icons[800] = ['a', 'A', 'clear sky']
icons[801] = ['b', 'B', 'few clouds']
icons[802] = ['c', 'C', 'scattered clouds']
icons[803] = ['d', 'D', 'broken clouds']
icons[804] = ['e', 'f', 'overcast clouds']
icons[900] = ['1', '1', 'tornado']
icons[901] = ['2', '2', 'tropical storm']
icons[902] = ['3', '3', 'hurricane']
icons[903] = ['4', '4', 'cold']
icons[904] = ['5', '5', 'hot']
icons[905] = ['6', '6', 'windy']
icons[906] = ['u', 'u', 'hail']
icons[951] = ['a', 'A', 'calm']
icons[952] = ['9', '9', 'light breeze']
icons[953] = ['9', '9', 'gentle breeze']
icons[954] = ['9', '9', 'moderate breeze']
icons[955] = ['9', '9', 'fresh breeze']
icons[956] = ['6', '6', 'strong breeze']
icons[957] = ['6', '6', 'high wind', 'near gale']
icons[958] = ['6', '6', 'gale']
icons[959] = ['6', '6', 'severe gale']
icons[960] = ['2', '2', 'storm']
icons[961] = ['3', '3', 'violent storm']
icons[962] = ['4', '4', 'hurricane']

def is_night(time, sunrise, sunset):
 return int(time < sunrise or time > sunset)

def calc_wind(w_spd, w_dir):
 w_dir = float(w_dir)
 w_spd = float(w_spd)
 w_spd = int(round(Decimal(w_spd*1.6), 0))
 if w_spd == 0:
  w_dir = 0x25
 else:
  w_dir = int(((w_dir*16.0)/360.0)) + 0x31
  w_dir += 16*int(w_spd/25)
 return (w_spd, chr(w_dir))

def calc_min_max_temp(time, time_entries):
 max_temperature = int(round(Decimal(time_entries[0].find('temperature').get('max'))))
 min_temperature = int(round(Decimal(time_entries[0].find('temperature').get('min'))))
 for time_entry in time_entries:
  time_from = parse(time_entry.get('from'))
  time_to = parse(time_entry.get('to'))
  if time.day == time_from.day and time.day == time_to.day:
   max_temp = int(round(Decimal((time_entry.find('temperature').get('max')))))
   min_temp = int(round(Decimal((time_entry.find('temperature').get('min')))))
   if max_temp > max_temperature:
    max_temperature = max_temp
   if min_temp < min_temperature:
    min_temperature = min_temp
 return (min_temperature, max_temperature)

###
# Today
###
tree = ET.parse(currentweather)
current = tree.getroot()
city = current.find('city')
sun = city.find('sun')
sunrise = parse(sun.get('rise'))
sunset = parse(sun.get('set'))
night = is_night(now, sunrise, sunset)
i = 0
moments[i][icon] = icons[int(current.find('weather').get('number'))][night]
moments[i][day] = weekday[int(sunrise.weekday())]
moments[i][cur_temp] = int(round(Decimal((current.find('temperature').get('value')))))
p_mode = current.find('precipitation').get('mode')
if p_mode != 'no':
 moments[i][prec] = int(round(Decimal((current.find('precipitation').get('value')))))
temp_unit = temp_units[str(current.find('temperature').get('unit'))]
moments[i][last_current_update] = parse(current.find('lastupdate').get('value'))
w_spd = current.find('wind').find('speed').get('value')
w_dir = current.find('wind').find('direction').get('value')
(moments[i][wind_speed], moments[i][wind_dir]) = calc_wind(w_spd, w_dir)

###
# Following days...
###
tree = ET.parse(forecast)
root = tree.getroot()
i += 1
time_entries = root.findall('forecast/time')
for time_entry in time_entries:
 time_from = parse(time_entry.get('from'))
 time_to = parse(time_entry.get('to'))
 if moments[i][time] > time_from and moments[i][time] < time_to:
  next_year = moments[i][time].year
  next_month = moments[i][time].month
  next_day = moments[i][time].day
  sunrise = sunrise + relativedelta(year=next_year, month=next_month, day=next_day)
  sunset = sunset + relativedelta(year=next_year, month=next_month, day=next_day)
  night = is_night(moments[i][time], sunrise, sunset)
  (moments[i][min_temp], moments[i][max_temp]) = calc_min_max_temp(moments[i][time], time_entries)
  moments[i][icon] = icons[int(time_entry.find('symbol').get('number'))][night]
  moments[i][hour] = moments[i][time]
  moments[i][day] = weekday[int(moments[i][time].weekday())]
  moments[i][prec] = time_entry.find('precipitation').get('value')
  i += 1
  if i >= len(moments):
   break

###
# Writing on conky file
###
f = open(conkyfile, 'w')
f.write('# center\n')
f.write('${offset 85}${font ConkyWeather:size=60}%s${font}\n' % str(moments[0][icon]))
f.write('${voffset -20}\n')
f.write('# left side\n')
f.write('Temp.: ${offset 0}${voffset 0}%s%s\n' % (str(moments[0][cur_temp]), temp_unit))
f.write('Prec.: %s\n' % str(moments[0][prec]))
f.write('Day: %s\n' % str(moments[0][day]))
f.write('Last Update: %s\n' % moments[0][last_current_update].strftime('%H:%M'))
f.write('# right side\n')
f.write('${alignr}${offset -40}${voffset -60}${font ConkyWindNESW:size=35}%s${font}\n' % str(moments[0][wind_dir]))
f.write('${alignr}${voffset 4}%s km/h\n' % str(moments[0][wind_speed]))
f.write('${voffset 5}${stippled_hr 1}\n')
del moments[0]
days = ('Day:', )
hours = ('Hour:', )
icons = ()
max_temps = ('H:', )
min_temps = ('L:', )
precs = ('Prec:', )
for index in moments:
 days += (str(moments[index][day]), )
 hours += (str(moments[index][hour].strftime('%H:%M')), )
 icons += (str(moments[index][icon]), )
 max_temps += (str(moments[index][max_temp]) + temp_unit, )
 min_temps += (str(moments[index][min_temp]) + temp_unit, )
 precs += (str(moments[index][prec]), )
f.write('${offset 47}${voffset 5}${font ConkyWeather:size=30}')
f.write('${goto 55}%s${goto 120}%s${goto 185}%s${font}\n' % icons)
f.write('${voffset -4}\n')
f.write('%s${goto 60}%s${goto 125}%s${goto 190}%s\n' % days)
f.write('%s${goto 60}%s${goto 125}%s${goto 190}%s\n' % hours)
f.write('%s${goto 60}%s${goto 125}%s${goto 190}%s\n' % max_temps)
f.write('%s${goto 60}%s${goto 125}%s${goto 190}%s\n' % min_temps)
f.write('%s${goto 60}%s${goto 125}%s${goto 190}%s\n' % precs)
f.close()
