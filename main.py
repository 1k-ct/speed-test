import datetime
import json
from time import sleep
import schedule

import speedtest


def add_to_file(results):
    try:
        with open('speedtest.json', 'r') as f:
            data = json.load(f)
    except:
        data = {"results": []}
        with open('speedtest.json', 'w') as f:
            json.dump(data, f, indent=2)

    data["results"].append(results)
    with open('speedtest.json', 'w') as f:
        json.dump(data, f, indent=2)


def task():
    results = speedtest.do_speedtest()
    parsed_results = speedtest.parse_speedtest_results(results)
    add_to_file(parsed_results)
    print("ok?")


def do_24times():
    schedule.every().days.at("00:00").do(task)
    schedule.every().days.at("01:00").do(task)
    schedule.every().days.at("02:00").do(task)
    schedule.every().days.at("03:00").do(task)
    schedule.every().days.at("04:00").do(task)
    schedule.every().days.at("05:00").do(task)
    schedule.every().days.at("06:00").do(task)
    schedule.every().days.at("07:00").do(task)
    schedule.every().days.at("08:00").do(task)
    schedule.every().days.at("09:00").do(task)
    schedule.every().days.at("10:00").do(task)
    schedule.every().days.at("11:00").do(task)
    schedule.every().days.at("12:00").do(task)
    schedule.every().days.at("13:00").do(task)
    schedule.every().days.at("14:00").do(task)
    schedule.every().days.at("15:00").do(task)
    schedule.every().days.at("16:00").do(task)
    schedule.every().days.at("17:00").do(task)
    schedule.every().days.at("18:00").do(task)
    schedule.every().days.at("19:00").do(task)
    schedule.every().days.at("20:00").do(task)
    schedule.every().days.at("21:00").do(task)
    schedule.every().days.at("22:00").do(task)
    schedule.every().days.at("23:00").do(task)

    while True:
        schedule.run_pending()
        sleep(1)


def do_once():
    task()


def main():
    # do_24times()
    # do_once()
    print("start time: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    main()
