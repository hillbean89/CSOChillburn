import sys

line1a, line1b = input().split('|')
line2a, line2b = input().split('|')

print(line1a, line1b, file=sys.stderr)
print(line2a, line2b, file=sys.stderr)
