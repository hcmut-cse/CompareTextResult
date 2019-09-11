from __future__ import division
import numpy as np
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser();
    parser.add_argument("--f1", dest="f1", default="./", help="First folder")
    parser.add_argument("--f2", dest="f2", default="./", help="Second folder")
    parser.add_argument("--file", dest="file", default="", help="Specify a file to compare")

    args = parser.parse_args()
    if (not args.f1 or not args.f2):
        assert "Folder input error!"

    fileName = list()

    if (not args.file):
        if (not os.path.exists(args.f1) or not os.path.exists(args.f2)):
            assert "Input folders not found!"
        fileNameF1 = os.listdir(args.f1)
        fileNameF2 = os.listdir(args.f2)

        fileName = [f for f in fileNameF1 if f in fileNameF2]

    else:
        if (not os.path.exists(os.path.join(args.f1, args.file)) or not os.path.exists(os.path.join(args.f2, args.file))):
            assert "Input file not found!"
        fileName.append(args.file)

    fileName = list(filter(lambda x: x[-3:].lower() == 'txt', fileName))
    diffLine = list()

    for file in fileName:
        print("===========================================================")
        print("File name: " + file)
        print("===========================================================")

        compareRes = True
        with open(os.path.join(args.f1, file), 'r', encoding='utf8') as f:
            file1 = f.read().split('\n')

        with open(os.path.join(args.f2, file), 'r', encoding='utf8') as f:
            file2 = f.read().split('\n')

        for i in range(min(len(file1), len(file2))):
            if (file1[i] != file2[i]):
                if compareRes:
                    compareRes = False
                if (args.file):
                    print("_______________________________________")
                    print("          |  Folder 1: %s" % file1[i])
                    print("Line %d: <" % i)
                    print("          |  Folder 2: %s" % file2[i])
                    print("_______________________________________")
                else:
                    print("Line %d" % i)

        if (len(file1) != len(file2)):
            print("Results do not have the same length!")

        if (compareRes):
            print("OK!")
