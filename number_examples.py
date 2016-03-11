import sys


def print_odd_numbers():
    """

    :rtype: None
    """
    for x in range(1, 101):
        if x % 2:
            print x


def print_mult_tables():
    for x in range(1, 13):
        result = ""
        for y in range(1, 13):
            result += str(x * y) + ' '
        print '{0}   {1}'.format(x, result)


def main(args):
    """
    :param args: args from main
    :rtype: None
    """
    #print_odd_numbers()
    print_mult_tables()


if __name__ == '__main__':
    main(sys.argv[1:])
