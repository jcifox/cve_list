import argparse

import ccopy_lib

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int, default=0)
args = parser.parse_args()
start = args.start
ccopy_lib.account_detail(start)