import random

def main1():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = 13
    rnd = random.randint(0, last)
    print(quotes)
    print(quotes[rnd])
    print(quotes[len(quotes)-1])


if __name__ == "__main__":
    main1()
