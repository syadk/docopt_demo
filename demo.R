# author: Tiffany Timbers
# date: 2020-01-15

"This script prints out docopt args.
Usage: demo.R <arg1> [<arg_two>] --arg2=<arg2> [--arg3=<arg3>]

Options:
<arg>             Takes any value (this is a required positional argument)
[<arg_two>]         Takes any value (this is an option positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
" -> doc

library(docopt)
opt <- docopt(doc)

main <- function(arg, arg_two, arg2, arg3) {
  print(opt)
  print(typeof(opt))
  print(opt$arg_two)
}
main(opt$arg, opt$arg_two, opt$arg2, opt$arg3)