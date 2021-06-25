################################################################################
#
# Bare Conductive Pi Cap
# ----------------------
#
# keyboard.py - map keyboard strokes to the electrodes of the Pi Cap
#
# Written for Raspberry Pi.
#
# Bare Conductive code written by Stefan Dzisiewski-Smith, Szymon Kaliski and
# Pascal Loose.
#
# This work is licensed under a MIT license https://opensource.org/licenses/MIT
#
# Copyright (c) 2017, Bare Conductive
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
################################################################################

from time import sleep
import signal, sys, MPR121
import uinput

KEY_MAPPING = {
                0: uinput.KEY_SPACE,
                1: uinput.KEY_LEFT,
                2: uinput.KEY_DOWN,
                3: uinput.KEY_RIGHT,
                4: uinput.KEY_UP,
                5: uinput.KEY_H,
                6: uinput.KEY_E,
                7: uinput.KEY_L,
                8: uinput.KEY_L,
                9: uinput.KEY_O,
                10: uinput.KEY_ENTER,
                11: uinput.KEY_TAB
              }

device = uinput.Device(KEY_MAPPING.values())

try:
  sensor = MPR121.begin()
except Exception as e:
  print (e)
  sys.exit(1)

num_electrodes = 12

# this is the touch threshold - setting it low makes it more like a proximity trigger default value is 40 for touch
touch_threshold = 40

# this is the release threshold - must ALWAYS be smaller than the touch threshold default value is 20 for touch
release_threshold = 20

# set the thresholds
sensor.set_touch_threshold(touch_threshold)
sensor.set_release_threshold(release_threshold)

# handle ctrl+c gracefully
def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
  if sensor.touch_status_changed():
    sensor.update_touch_data()
    for i in range(num_electrodes):
      if sensor.is_new_touch(i):
        print ("electrode {0} was just touched".format(i))
        device.emit_click(KEY_MAPPING[i])
      elif sensor.is_new_release(i):
        print ("electrode {0} was just released".format(i))

  sleep(0.01)
