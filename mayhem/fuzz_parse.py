#! /usr/bin/env python3
import atheris
import sys

import fuzz_helpers

with atheris.instrument_imports(include=['gpxpy', 'xml']):
    from gpxpy.parser import GPXParser

from gpxpy.gpx import GPXException

def TestOneInput(data):
    if len(data) < 1:
        return -1
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        gpx_parser = GPXParser(fdp.ConsumeRemainingString())
        gpx = gpx_parser.parse()
        gpx.get_moving_data(raw=True)
        gpx.smooth()
        gpx.to_xml()
    except GPXException:
        return -1
    except ValueError as e:
        if any(x in str(e) for x in ['tag', 'XML', 'URI',]):
            return -1
        raise

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
