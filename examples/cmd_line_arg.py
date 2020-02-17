import sys
import argparse

print(sys.argv)

parser = argparse.ArgumentParser('Simple tool for training')

parser.add_argument('--volume', type=int, help='Input for increasing or decreasing volume')

arg = parser.parse_args(['--volume'])
print(arg.volume)