import sys, time
import sevseg

secondLeft = 7265

try:
    while True:
        print("\n" * 60)

        hours = str(secondLeft // 3600)
        minutes = str((secondLeft % 3600) // 60)
        seconds = str(secondLeft % 60)

        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(hours, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(f"{hTopRow} * {mTopRow} * {sTopRow}")
        print(f"{hMiddleRow} * {mMiddleRow} * {sMiddleRow}")
        print(f"{hBottomRow} * {mBottomRow} * {sBottomRow}")

        if secondLeft == 0:
            print()
            print("   * * * * BOOM * * * *")
            break

        print()
        print("Press Ctrl-C to quit.")

        time.sleep(1)
        secondLeft -= 1
except KeyboardInterrupt:
    print("Contdown")
    sys.exit()
