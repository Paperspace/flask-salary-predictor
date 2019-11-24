import requests
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-y', '--years', help='years of experience', type=float, default=1.8)
parser.add_argument('-u', '--url', help='endpoint url', default='http://localhost/api')
parser.add_argument('-U', '--username', help='basic auth username')
parser.add_argument('-P', '--password', help='basic auth password')

args = parser.parse_args()

print('server:', args.url)
print('years of exprience:', args.years)

auth=None
if args.username and args.password:
    auth=(args.username, args.password)

r = requests.post(args.url, json={'exp': args.years,}, auth=auth)
print('predicted salary:', round(r.json()))
