#!/usr/bin/env python

# Run a command after `hours`[6] and `minutes`[0] +/- a random delta
# to be used as an alarm clock.

import popen2
import sys
import time
from datetime import datetime, timedelta
from random import choice, randint


def main(sleep_time_hours, sleep_time_minutes, alarm_command):
    REFRESH_RATE = 60
    RANDOM_DELTA = randint(0, 10 * 60) * choice((-1, 1))

    sleep_time = sleep_time_hours * 60 * 60 + sleep_time_minutes * 60 + RANDOM_DELTA

    # It can be done with this two lines only but the following is
    # more fancy
    # time.sleep(sleep_time)
    # popen2.popen3(alarm_command)

    sleep_time_delta = timedelta(0, sleep_time)
    alarm = datetime.now() + sleep_time_delta
    sys.stdout.write('%s\n' % alarm)

    while datetime.now() < alarm:
        sleep_time = alarm - datetime.now()
        sys.stdout.write('%s\n' % str(sleep_time))
        time.sleep(REFRESH_RATE)

    popen2.popen3(alarm_command)


if __name__ == "__main__":
    macro_file_path = 'autoplay-spotify.cnee'
    alarm_command = '/usr/bin/cnee --replay -f %s' % macro_file_path
    sleep_time_hours, sleep_time_minutes = 6, 0
    if len(sys.argv) > 1:
        sleep_time_hours = int(sys.argv[1])
    if len(sys.argv) > 2:
        sleep_time_minutes = int(sys.argv[2])
    main(sleep_time_hours, sleep_time_minutes, alarm_command)