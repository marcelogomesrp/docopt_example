#!/usr/bin/env python3

"""pynum.py.

Usage:
  pynum.py [-i=<name> | --input_file=<name>] [-o=<name> | --output_file=<name>]
  pynum.py --tui
  pynum.py -h | --help
  pynum.py --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.
  -i=<name> --input_file=<name>     File to read.
  -o=<name> --output_file=<name>    File to write.
  --tui                             Use TUI to get information

"""

from docopt import docopt

from services import NumService, ScreenServices


def main() -> None:
    args = docopt(__doc__, version='pynum.py 1.0')
    (input_file, output_file, tui) = ScreenServices.read_args(args)

    input_service = ScreenServices.get_input_service(input_file, tui)
    output_service = ScreenServices.get_output_service(output_file, tui)

    data = input_service.read_data()

    numService = NumService(data)
    data_numerabled = numService.get_numerable_lines()

    output_service.write(data_numerabled)


if __name__ == '__main__':
    main()
