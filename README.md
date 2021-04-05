# DDoS
A DDoS simulator for Python. Built for testing your apps for handling DDoS-es, and for educational purposes

# Usage
First, download it!

Arguments:
- `-t` - number of threads
- `--url` - URL to DDoS
- `--rpt` - How many requests per thread should there be

## View output in console
`python ddos_test.py --url [URL] -t [THREADS] --rpt [REQUESTS PER THREAD]`

## View output in text file
`python ddos_test.py --url [URL] -t [THREADS] --rpt [REQUESTS PER THREAD] > ddos.txt`

## Example
`python ddos_test.py --url https://example.com -t 2 --rpt 5`

# Disclaimer
Software is meant only for educational purposes & for testing your OWN website (e.g. how many users can it handle). Author doesn't allow any illegal use.

