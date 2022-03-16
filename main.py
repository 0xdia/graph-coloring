import sys
from graph import graph

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('error: too few arguements.')
        print('usage: python3 main.py input_file.txt [--adjlist | --edges] (--adjlist by default)\n')
        exit()
    
    if len(sys.argv) > 3:
        print('error: too many arguements.')
        print('usage: python3 main.py input_file.txt [--adjlist | --edges] (--adjlist by default)\n')
        exit()
    
    if len(sys.argv) == 3 and sys.argv[-1] not in ['--adjlist', '--edges']:
        print('usage: python3 main.py input_file.txt [--adjlist | --edges] (--adjlist by default)\n')
        exit()

    mode = '--adjlist' if len(sys.argv) == 2 else sys.argv[-1]
    input_file = sys.argv[1]

    g = graph()
    g.read(input_file, mode)
