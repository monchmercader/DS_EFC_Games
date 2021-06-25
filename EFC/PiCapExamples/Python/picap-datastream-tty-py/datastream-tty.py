################################################################################
#
# Bare Conductive Pi Cap
# ----------------------
#
# datastream-tty.py - streams capacitive sense data from MPR121 to stdout
#
# Written for Raspberry Pi.
#
# Bare Conductive code written by Szymon Kaliski.
#
# This work is licensed under a MIT license https://opensource.org/licenses/MIT
#
# Copyright (c) 2016, Bare Conductive
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#################################################################################

from time import sleep
import signal, sys, MPR121

try:
  sensor = MPR121.begin()
except Exception as e:
  print (e)
  sys.exit(1)

# handle ctrl+c gracefully
def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# how many electrodes we have
electrodes_range = range(12)

# this is the touch threshold - setting it low makes it more like a proximity trigger default value is 40 for touch
touch_threshold = 40

# this is the release threshold - must ALWAYS be smaller than the touch threshold default value is 20 for touch
release_threshold = 20

# set the thresholds
sensor.set_touch_threshold(touch_threshold)
sensor.set_release_threshold(release_threshold)

while True:
  if sensor.touch_status_changed():
    sensor.update_touch_data()

  sensor.update_baseline_data()
  sensor.update_filtered_data()

  # touch values
  data_array = []
  for i in electrodes_range:
    # get_touch_data returns boolean values: True or False
    # we need to turn them into ints first: 1 or 0
    # and then into string: "1" or "0" so we can display them
    data_array.append(str(int(sensor.get_touch_data(i))))
  print ("TOUCH: {0}".format(" ".join(data_array)))

  # touch thresholds
  data_array = []
  for i in electrodes_range:
    data_array.append(str(touch_threshold))
  print ("TTHS: {0}".format(" ".join(data_array)))

  # release threshold
  data_array = []
  for i in electrodes_range:
    data_array.append(str(release_threshold))
  print ("RTHS: {0}".format(" ".join(data_array)))

  # filtered values
  data_array = []
  for i in electrodes_range:
    data_array.append(str(sensor.get_filtered_data(i)))
  print ("FDAT: {0}".format(" ".join(data_array)))

  # baseline values
  data_array = []
  for i in electrodes_range:
    data_array.append(str(sensor.get_baseline_data(i)))
  print ("BVAL: {0}".format(" ".join(data_array)))

  # value pairs
  data_array = []
  for i in electrodes_range:
    data_array.append(str(sensor.get_baseline_data(i) - sensor.get_filtered_data(i)))
  print ("DIFF: {0}".format(" ".join(data_array)))

  # a little delay so that we don't just sit chewing CPU cycles
  sleep(0.01)
