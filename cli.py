import argparse
import sys


class CLI(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description="cli tool built using python",
            usage='''python -m cli <command> [<args>]

subcommand
            ''')
        parser.add_argument('command', help='sub command to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def subcommand(self):
        parser = argparse.ArgumentParser(
            description="This is an example subcommand for the cli template"
        )
        parser.add_argument(
            '--example_arg', help="This is an example argument for the subcommand", default="hello arg!"
        )

        args = parser.parse_args(sys.argv[2:])
        print("Running subcommand with arg: %s" % args.example_arg)


if __name__ == '__main__':
    CLI()
