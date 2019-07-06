
def main():

    """
    Call functions to create lists of prefixes and powers
    in base 10 and base 2, then print them.
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| SI Prefixes   |")
    print("-----------------\n")

    base10_list = create_base10_list()

    print_base10(base10_list)

    print("")

    base2_list = create_base2_list()

    print_base2(base2_list)

    print(create_base10_list.__doc__)


def create_base10_list():

    """
    Create a list of base 10 prefixes with corresponding powers.
    """

    base10 = [{"prefix": "yotta", "power": 24},
              {"prefix": "zetta", "power": 21},
              {"prefix": "exa", "power": 18},
              {"prefix": "peta", "power": 15},
              {"prefix": "tera", "power": 12},
              {"prefix": "giga", "power": 9},
              {"prefix": "mega", "power": 6},
              {"prefix": "kilo", "power": 3},
              {"prefix": "hecto", "power": 2},
              {"prefix": "deca", "power": 1},

              {"prefix": "(none)", "power": 0},

              {"prefix": "deci", "power": -1},
              {"prefix": "centi", "power": -2},
              {"prefix": "milli", "power": -3},
              {"prefix": "micro", "power": -6},
              {"prefix": "nano", "power": -9},
              {"prefix": "pico", "power": -12},
              {"prefix": "femto", "power": -15},
              {"prefix": "atto", "power": -18},
              {"prefix": "zepto", "power": -21},
              {"prefix": "yocto", "power": -24}]

    return base10


def print_base10(base10_list):

    """
    Use list from create_base10_list function
    to print prefixes, powers and values.
    """

    for b in base10_list:

        if b["power"] >= 0:
            print("{:6s} 10^{:<3} = {:>26}".format(b["prefix"], b["power"], 10**b["power"]))
        else:
            print("{:6s} 10^{:<3} = {:>26.{prec}f}".format(b["prefix"], b["power"], 10**b["power"], prec=abs(b["power"])))


def create_base2_list():

    """
    Create a list of base 2 prefixes with corresponding powers.
    """

    base2 = [{"prefix": "kibibyte", "power": 10},
             {"prefix": "mebibyte", "power": 20},
             {"prefix": "gibibyte", "power": 30},
             {"prefix": "tebibyte", "power": 40},
             {"prefix": "pebibyte", "power": 50},
             {"prefix": "exbibyte", "power": 60},
             {"prefix": "zebibyte", "power": 70},
             {"prefix": "yobibyte", "power": 80}]

    return base2


def print_base2(base2_list):

    """
    Use list from create_base2_list function
    to print prefixes, powers and values.
    """

    for b in base2_list:

        print("1 {}: 2^{} = {:>33,} bytes".format(b["prefix"], b["power"], 2**b["power"]))


main()
