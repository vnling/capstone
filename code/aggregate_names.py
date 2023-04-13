import sys

def aggregate():
    args = sys.argv[1:]
    output = open(args[1], 'a')
    with open(args[0], 'r') as input:
        for line in input:
            name = line.split(',')[0]
            output.write(name + '\n')
    output.close()

def clean():
    output = open(sys.argv[2], 'w')
    no_duplicates = set()
    with open(sys.argv[1], 'r') as names:
        for line in names:
            no_duplicates.add(line)
        for name in list(no_duplicates):
            output.write(name)
    output.close()

def main():
    clean()

main()