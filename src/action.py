import re

serverlines = []

def relevantLines(rawlines):
    finallines = []
    for line in rawlines:
        if re.match("^\s*(#.*)?$", line):
            continue
        finallines.append(rawline.strip())
    return finallines

def load(settings):
    global serverlines

    fh = open(settings["serverfile"])
    rawlines = fh.readlines()
    fh.close()

    serverlines = relevantLines(rawlines)

def dispatch(action, namefilter):
    # TODO - list, edit, run, cp, add, remove
    pass

