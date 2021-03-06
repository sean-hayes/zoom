# -*- coding: utf-8 -*-

"""
    zoom

    Zoom command line utility
"""

import os
import sys
import inspect
import commands
from argparse import ArgumentParser

from zoom.utils import ItemList


class SimpleException(Exception):
    """an exception that traps everything"""
    pass


def get_functions():
    """get a dictionary containing the valid command functions"""
    functions = {
        command: getattr(commands, command) for
        command in dir(commands) if command in commands.__all__
    }
    return functions


def dispatch(args):
    """dispatch a command for running"""
    functions = get_functions()
    cmd = args[1]
    if cmd in functions:
        del sys.argv[1]
        functions[cmd]()
    else:
        print('No such command {!r}\nUse -h for help'.format(cmd))


def list_commands():
    """print lits of valid commands to stdout"""
    result = ItemList([('command', 'purpose', 'usage')])
    installed_name = os.path.split(sys.argv[0])[-1]
    for name, function in sorted(get_functions().items()):
        if not name.startswith('_'):
            doc = function.__doc__
            text = ['{} {} [<options>]'.format(installed_name, name)]
            parameters = inspect.signature(function).parameters.values()
            for parameter in parameters:
                if parameter.kind == parameter.POSITIONAL_OR_KEYWORD:
                    text.append('[{}]'.format(parameter.name))
            result.append([name, doc, ' '.join(text)])
    print('\nZoom CLI\n\n{}\n'.format(result))


def main():
    """main program

    Calls the appropriate method corresponding to the command line args.
    """
    if len(sys.argv) == 2 and sys.argv[-1] in ['-h', '--help']:
        installed_name = os.path.split(sys.argv[0])[-1]
        parser = ArgumentParser(
            description='{name} command line utility'.format(
                name=installed_name
            ),
            usage='{name} <command> [options] [arguments]\n'
                  '       {name} <command> -h\n'
                  '       {name} # list commands'.format(
                      name=installed_name
                  )
            )
        parser.add_argument('command', nargs='?')
        parser.parse_args()

    try:
        if len(sys.argv) > 1:
            dispatch(sys.argv)
        else:
            list_commands()

    except SimpleException as msg:
        print('fatal: %s' % msg)


if __name__ == '__main__':
    main()
