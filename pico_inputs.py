import json
import json.decoder
import time
import typing

import serial


class ScreenInputs(typing.TypedDict):
    band: str
    volume: float
    power: bool
    tuning: float


screenInputs: ScreenInputs


elapsed = 0
prev = time.time()

with serial.Serial("/dev/ttyACM0", 19200, timeout=1) as ser:
    while True:
        lineBytes: bytes = ser.readline()  # read a '\n' terminated line
        line = lineBytes.decode("UTF-8")[0:-2]

        try:
            screenInputs = ScreenInputs(json.loads(line))
        except json.decoder.JSONDecodeError as e:
            continue

        now = time.time()
        elapsed += now - prev

        if elapsed > 1:
            print(screenInputs)
            elapsed = 0

        prev = now
