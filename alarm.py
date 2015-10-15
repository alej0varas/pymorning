#!/usr/bin/env python

# Run a command after `hours`[6] and `minutes`[0] +/- a random delta
# to be used as an alarm clock.

import popen2
import sys
import time
from datetime import datetime, timedelta
from random import choice, randint


VOLUME_INCREMENT_RATE = 60  # in seconds
VOLUME_INCREMENT = 5  # as a percentage
VOLUME_MAX_VALUE = 100  # as a percentage
VOLUME_INCREMENT_COMMAND = 'pactl set-sink-volume 1 +%s%%' % VOLUME_INCREMENT
VOLUME_TO_MINIMUM_COMMAND = 'pactl set-sink-volume 1 0%'

REFRESH_RATE = 60  # in seconds
DELTA_SIZE = 10  # in minutes
RANDOM_DELTA = randint(0, DELTA_SIZE * 60) * choice((-1, 1))

MACRO_FILE_PATH = 'autoplay-spotify.cnee'
ALARM_COMMAND = '/usr/bin/cnee --replay -f %s' % MACRO_FILE_PATH


def main(sleep_time_hours, sleep_time_minutes):

    sleep_time = sleep_time_hours * 60 * 60 + sleep_time_minutes * 60 + RANDOM_DELTA

    # It can be done with this two lines only but the following is
    # more fancy
    # time.sleep(sleep_time)
    # popen2.popen3(ALARM_COMMAND)

    sleep_time_delta = timedelta(0, sleep_time)
    alarm = datetime.now() + sleep_time_delta
    sys.stdout.write('%s\n' % alarm)

    while datetime.now() < alarm:
        sleep_time = alarm - datetime.now()
        sys.stdout.write('%s\n' % str(sleep_time))
        time.sleep(REFRESH_RATE)

    popen2.popen3(VOLUME_TO_MINIMUM_COMMAND)

    popen2.popen3(ALARM_COMMAND)

    for i in range(0, VOLUME_MAX_VALUE / VOLUME_INCREMENT_RATE):
        time.sleep(VOLUME_INCREMENT_RATE)
        popen2.popen3(VOLUME_INCREMENT_COMMAND)


if __name__ == "__main__":
    sleep_time_hours, sleep_time_minutes = 6, 0
    if len(sys.argv) > 1:
        sleep_time_hours = int(sys.argv[1])
    if len(sys.argv) > 2:
        sleep_time_minutes = int(sys.argv[2])
    main(sleep_time_hours, sleep_time_minutes)