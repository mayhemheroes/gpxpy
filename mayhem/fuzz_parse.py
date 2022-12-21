#! /usr/bin/env python3
import atheris
import sys

import fuzz_helpers

with atheris.instrument_imports(include=['gpxpy', 'xml']):
    from gpxpy.parser import GPXParser

from gpxpy.gpx import GPXException

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    if len(data) < 1:
        return -1
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        gpx_parser = GPXParser(fdp.ConsumeRemainingString())
        gpx = gpx_parser.parse()
        gpx.to_xml()
    except GPXException:
        return -1
    except ValueError:
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
