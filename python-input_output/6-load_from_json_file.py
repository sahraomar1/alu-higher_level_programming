#!/usr/bin/python3
"""Are you documented?"""


import json


def load_from_json_file(filename):
    """How far now"""
    with open(filename, "r") as f:
        return json.load(f)
