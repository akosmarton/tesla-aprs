import datetime
from datetime import datetime, timezone

def get_hours_and_mins_from_mins(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes

def get_aprs_passcode_for_callsign(callsign):
    hash = 0x73e2
    callsign = callsign[:10]

    for i in range(0, len(callsign), 2):
        hash ^= ord(callsign[i]) << 8
        if i+1 < len(callsign):
            hash ^= ord(callsign[i + 1])
        hash &= 0xFFFF

    return hash

def convert_coord_to_aprs(degrees, is_latitude):
    degrees = abs(degrees)
    degree_whole = int(degrees)
    degree_fraction = degrees - degree_whole
    minutes = degree_fraction * 60
    if is_latitude:
        return f"{degree_whole:02d}{minutes:05.2f}"
    else:
        return f"{degree_whole:03d}{minutes:05.2f}"

def convert_unix_timestamp_to_aprs(utc_timestamp):
    dt = datetime.fromtimestamp(utc_timestamp, tz=timezone.utc)
    day = str(dt.day).zfill(2)
    hours = str(dt.hour).zfill(2)
    minutes = str(dt.minute).zfill(2)
    return day, hours, minutes