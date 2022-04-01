import sys
res = []

def main(lines):
    res = list(str(lines))
    return res

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
