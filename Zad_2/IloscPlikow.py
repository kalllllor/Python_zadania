import os.path


def fileCounter():
    DIR = '/Users'
    liczbaplikow = 0
    for nazwa in os.listdir(DIR):
        if os.path.isfile(os.path.join(DIR, nazwa)):
            liczbaplikow += 1

    print("Liczba plikow w " + str(DIR) + ": " + str(liczbaplikow))


if __name__ == "__main__":
    fileCounter()