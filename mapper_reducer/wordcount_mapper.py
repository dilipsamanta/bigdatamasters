import sys

def mapWords():
    for line in sys.stdin:
        line = line.strip()

        words = line.split()

        for word in words:
            print(word,"\t", 1)

if __name__ == "__main__":
    mapWords()