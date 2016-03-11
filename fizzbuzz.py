import sys


def better_fizzbuzz():
    for x in range(1, 101):
        msg = ""
        if x % 3 == 0:
            msg += "Fizz"
        if x % 5 == 0:
            msg += "Buzz"

        print '{0} {1}'.format(x, msg)


def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0:
            if x % 5 == 0:
                print '{0} {1}'.format(x, " FizzBuzz")
            else:
                print '{0} {1}'.format(x, " Fizz")
        elif x % 5 == 0:
            print '{0} {1}'.format(x, " Buzz")


def main(args):
    """
    :param args: args from main
    :rtype: None
    """
    better_fizzbuzz()


if __name__ == '__main__':
    main(sys.argv[1:])
