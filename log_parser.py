import argparse
import os
import re
import json
from collections import defaultdict, Counter

parser = argparse.ArgumentParser(description='Process access.log')
parser.add_argument('-f', dest='log_file', action='store', help='Path to logfile')
parser.add_argument('-d', dest='log_dir', action='store', help='Path to logdir')
args = parser.parse_args()


def parse_logs(file):
    # store method, referer, ip, durability, date and time of request
    durable_requests = defaultdict(list)
    # store log file analysis
    log_analysis = defaultdict(
        lambda: {"all_requests": 0, "GET": 0, "POST": 0, "PUT": 0, "DELETE": 0,
                 "HEAD": 0, "CONNECT": 0, "OPTIONS": 0, "TRACE": 0, "PATCH": 0,
                 "top3 popular ip": {}, "top3 long requests": []}
    )
    # list of ip addresses
    ip_addresses = []

    for line in file:
        # 213.24.134.32 - - [12/Dec/2015:18:58:51 +0100] "POST /administrator/index.php HTTP/1.1"
        # 200 4494 "http://almhuette-raith.at/administrator/"
        # "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" 2254
        ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip_match is not None:
            log_analysis["Request Counter"]["all_requests"] += 1

            ip = ip_match.group()
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE|PATCH)",
                               line)
            referer = re.search(r"\"(http.+)\"\s\"", line)
            date_time = re.search(r"\[.+\]", line)
            duration = re.search(r"\d+$", line)
            if method is not None:
                ip_addresses.append(ip)
                log_analysis["Request Counter"][method.group(1)] += 1

                if duration is not None:
                    dict_ip4 = {}

                    dict_ip4["method"] = method.group(1)
                    if referer is not None:
                        dict_ip4["url referer"] = referer.group(1)
                    dict_ip4["ip"] = ip_match.group(0)
                    dict_ip4["duration"] = int(duration.group(0))
                    dict_ip4["date-time"] = date_time.group(0)
                    durable_requests["requests unsorted"].append(dict_ip4)

    # 3 most popular ip
    log_analysis["Request Counter"]["top3 popular ip"] = Counter(ip_addresses).most_common(3)

    sort_long_request = sorted(durable_requests["requests unsorted"],
                               key=lambda k: k["duration"], reverse=True)
    # 3 most durable requests
    log_analysis["Request Counter"]["top3 long requests"] = sort_long_request[:3]

    with open(f"{file.name.rsplit('/')[-1]}--result.json",
              mode="w", encoding='UTF-8') as result_file:
        create_json_method2 = json.dumps(log_analysis, indent=4)
        result_file.write(create_json_method2)

    print(f"***** {file.name} analysis:")
    print(create_json_method2)


if args.log_dir is not None:
    for log in os.listdir(args.log_dir):
        with open(os.path.join(args.log_dir, log), mode="r", encoding='UTF-8') as log_file:
            parse_logs(log_file)

if args.log_file is not None:
    with open(args.log_file, mode="r", encoding='UTF-8') as log_file:
        parse_logs(log_file)
