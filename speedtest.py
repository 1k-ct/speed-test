import datetime
import json
import subprocess


def parse_speedtest_results(results):
    # Parse the results of the speedtest
    # and return a dictionary of the results
    #
    # results: string
    #
    # returns: dictionary
    #
    # Example:
    # {
    #   'download': '0.0Mbit/s',
    #   'upload': '0.0Mbit/s',
    #   'ping': '0.0',
    #   'server': '{..}',
    #   'timestamp': '0.0'
    # }
    download = str(convert_B_to_MB(results["download"]))+" Mbit/s"
    upload = str(convert_B_to_MB(results["upload"]))+" Mbit/s"
    ping = results["ping"]
    server = results["server"]
    timestamp = results["timestamp"]
    res = {"download": download, "upload": upload,
           "ping": ping, "server": server, "timestamp": timestamp,
           "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return res


def convert_B_to_MB(size):
    return size / 1024 / 1024


def do_speedtest():
    process = subprocess.run(
        ['speedtest-cli', '--json'], stdout=subprocess.PIPE)
    output = json.loads(process.stdout)
    return output
