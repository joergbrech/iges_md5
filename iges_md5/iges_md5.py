import hashlib
import argparse

def md5(file, hdr_fnc):
    """
    calculates the md5 checksum of an ascii file, excluding its header.

    input:
         - hdr_func: hdr_func is a function that takes a string as an input and returns True, if it is part of the
                     header and False otherwise. The implementation depends on the file format of the header

    output: The md5 checksum of the file without the header
    """

    hash_md5 = hashlib.md5()
    with open(file, "rb") as f:
        while hdr_fnc(f.readline()):
            pass

        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def iges_hdr_fnc(string):
    """identifies a line of an iges file as a header line"""

    if len(string)<73 or string[72] == ord('S') or string[72] == ord('G'):
        return True
    return False


def main():

    parser = argparse.ArgumentParser(description='returns MD5 Checksum of IGES file')
    parser.add_argument('input_file', type=str, help='Input file')
    parser.add_argument('--ignore-header', '-i', help='ignore header lines', action="store_true")
    args = parser.parse_args()

    func = lambda line: False
    if args.ignore_header:
        func = iges_hdr_fnc

    print(md5(args.input_file, func))


if __name__ == '__main__':
    main()
