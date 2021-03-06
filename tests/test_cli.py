"""Tests for src/cli.py"""
from unittest.mock import patch

from cli import parse_arguments


@patch("argparse.ArgumentParser")
def test_command(mock_args):
    parse_arguments()
    mock_args().add_argument.assert_called()
    mock_args().add_argument.assert_any_call(
        "-l",
        "--link",
        type=str,
        help="URL link to Wikipedia page",
    )
    mock_args().add_argument.assert_any_call(
        "-d",
        "--directory",
        type=str,
        help="Name of directory where file will be save",
    )
    mock_args().add_argument.assert_any_call(
        "-n",
        "--number-of-links",
        type=int,
        help="The number of url links that will be queued for processing",
    )
    mock_args().add_argument.assert_any_call(
        "-mw", "--max-workers", type=int, help="The humber of work threads"
    )
    mock_args().add_argument.assert_any_call(
        "-ll",
        "--logging-level",
        type=str,
        default="INFO",
        help="level for logging module",
    )
    mock_args().add_argument.assert_any_call(
        "-c",
        "--config",
        type=str,
        default="../etc/config.ini",
        help="config file for config parser",
    )
    mock_args().parse_args.assert_called_once()
