import os
import re
from datetime import datetime, timedelta


def get_timecodes(srt_filename):
    """
    """
    timecode = re.compile('\d{2}:\d{2}:\d{2},\d{3}')

    with open(srt_filename) as fp:
        subtitles = fp.read()
    timecodes = timecode.findall(subtitles)

    return timecodes


def add_subtract_delay(timecodes, delay=1):
    """
    :param float delay: This is the value of the delay (or advance) to be added
                        (or subtracted) in seconds. Milliseconds (and
                        microseconds) will be interpreted from the decimal
                        places.
                        Positive delay is added, negative delay is subtracted.
    """
    if type(timecodes) is not list:
        timecodes = [timecodes]
    new_timecodes = []
    for timecode in timecodes:
        t = datetime.strptime('2000 ' + timecode, '%Y %H:%M:%S,%f')
        t = t + timedelta(0, delay)
        timecode = t.strftime('%H:%M:%S,%f')
        new_timecodes.append(timecode[:-3])

    return new_timecodes
