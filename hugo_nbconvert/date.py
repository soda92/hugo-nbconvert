from datetime import datetime
from pathlib import Path
import subprocess


def get_date() -> str:
    return datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S+08:00")


def get_oldest_git_date(file: Path) -> str:
    lines = subprocess.getoutput(" ".join(["git", "blame", str(file)]))
    import re

    datetimes = []
    for i in lines.split("\n"):
        r = re.findall(r"[\^a-z0-9]{8} \((.*)\)", i)
        if len(r) >= 1:
            datetimes.append(r[0])

    real_dates = []
    for i in datetimes:
        results = i.split(" ")
        date = results[1]
        time = results[2]
        timezone = results[3]
        real_date = " ".join([date, time, timezone])
        real_date = datetime.datetime.strptime(real_date, "%Y-%m-%d %H:%M:%S %z")
        real_dates.append(real_date)
        # print(real_date)

    return datetime.datetime.strftime(min(real_dates), "%Y-%m-%dT%H:%M:%S+08:00")
