#!/usr/bin/env python3

import args
import config
import action

def main():
    settings = config.load()
    arguments = args.parse()

    action.load(settings)

    action.dispatch(arguments["action"], arguments["filter"])
