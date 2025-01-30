import argparse
from astropy.io import fits
from lsp import lstsq

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, help='Path to ccd.fits')

if __name__ == "__main__":
    args = parser.parse_args()
    print(args.filename)
