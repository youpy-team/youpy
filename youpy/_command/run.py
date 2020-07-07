# -*- encoding: utf-8 -*-
"""Run a project.
"""


import argparse

from youpy._cli.argparse import ArgparseFormatter
from youpy._cli.argparse import parse_cli_args
from youpy._runner import run


PROGNAME = "youpy-run"

def mkcli():
    parser = argparse.ArgumentParser(
        prog=PROGNAME,
        description=__doc__,
        formatter_class=ArgparseFormatter)
    parser.add_argument(
        "project_dir",
        action="store",
        type=str,
        help="Path to the project directory to run")
    return parser

def main(argv, opts):
    opts, _ = parse_cli_args(mkcli(), argv[1:], opts)
    run(opts.project_dir)