import random, shutil, sys, time

MIN_STREAM_LENGTH = 10
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAMS_CHARS = ["0", "1"]

DENSITY = 0.02
WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

print("Digital Stream")
print("Press Ctrl-C quit.")
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
            if columns[i] > 0:
                print(random.choice(STREAMS_CHARS), end="")
                columns[i] -= 1
            else:
                print(" ", end="")
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
