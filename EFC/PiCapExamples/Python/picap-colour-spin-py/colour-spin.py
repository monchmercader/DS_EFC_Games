################################################################################
#
# Bare Conductive Pi Cap
# ----------------------
#
# colour-spin.py - rainbow colours on Pi Cap LED
#
# Written for Raspberry Pi.
#
# Bare Conductive code written by Szymon Kaliski and Tom Hartley
#
# This work is licensed under a MIT license https://opensource.org/licenses/MIT
#
# Copyright (c) 2018, Bare Conductive
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
from gpiozero import RGBLED

led = RGBLED(6, 5, 26, active_high=False)

# how long should each colour stay lit before switching to next one
delay_time = 0.5

ordering = [(0, 0, 1), #blue 
            (0, 1, 0), #green
            (1, 0, 0), #red
            (0, 1, 1), #cyan
            (1, 1, 0), #yellow
            (1, 0, 1), #magenta
            (1, 1, 1), #white
            (0, 0, 0)] #black (off)

running = True
while running:
  try:
    for i in ordering:
      led.color = i
      sleep(delay_time)
  except KeyboardInterrupt:
    led.off()
    running = False
