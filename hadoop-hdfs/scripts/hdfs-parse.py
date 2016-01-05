#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import getopt
import json



def main(argv):
    inputfile, context, metric = "", "", ""
    help_string = "Usage:\n./%s -i <input_file>" % (argv[0])
    try:
        opts, args = getopt.getopt(argv[1:], "hi:c:m:", ["input", "context", "metric"])
    except getopt.GetoptError:
        print help_string
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print help_string
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-c", "--context"):
            context = arg
        elif opt in ("-m", "--metric"):
            metric = arg

    try:
        with open(inputfile, "r") as f:
            data = json.loads(f.read())
            if context not in ['dfs', 'metricssystem', 'ugi', 'jvm', 'rpc']:
                print "Unknown context '%s'" % context
                sys.exit(1)

            data = data[context]
            if metric not in data.keys():
                print "Unknown metric '%s'" % metric
                sys.exit(1)

            if type(metrics) is list:
                # Sum value
                metrics = [float(x) if "." in x else int(x) for x in metrics]
                metrics = sum(metrics)/len(metrics)
            print metrics
    except IOError:
        print "Error, cant read or write to file '%s'" % outputfile
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv)

