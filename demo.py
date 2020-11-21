# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: docopt.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg_four>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg_four>]      Takes any value (this is an optional positional argument)
"""

from docopt import docopt
opt = docopt(__doc__)

def main(arg1, arg2, arg3, arg4):
    print(opt)
    print(type(opt))
    print(opt["<arg_four>"])
    
if __name__ == "__main__":
    main(opt["<arg1>"], opt["--arg2"], opt["--arg3"], opt["<arg_four>"])
