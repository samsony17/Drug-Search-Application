import sys
import xml.sax

from saxloanparse import LoanParse


class SBAFedXMLParse:

    def __init__(self, filepath):
        print("passed filename: {}".format(filepath))
        source = open(filepath, 'r')
        xml.sax.parse(source, LoanParse())

if __name__ == "__main__":
    SBAFedXMLParse(str(sys.argv[1]))
