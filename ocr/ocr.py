# #!/usr/bin/python3
import click
import logging
import src.preprocessing as preProcess
import src.ocrhelper as ocrHelper
import os
import pathlib


@click.command()
@click.option('--input', type=str, default="", help='input file path')
@click.option('--output', type=str, default="res.txt", help='output file path')
@click.option('--verbose', is_flag=True)
def main(input, output, verbose):

    # imput filters
    file = pathlib.Path(input)
    if not file.exists():
        print("File not exist")
        exit(0)

    _, file_extension = os.path.splitext(input)
    path = os.path.abspath(input)
    logging.getLogger(__name__)

    if(verbose):
        logging.basicConfig(level=logging.DEBUG)
    logging.debug("Start")
    logging.debug(file_extension)
    if(file_extension == ".png" or file_extension == ".jpg"):
        image = preProcess.preprocessingImage(path)
        ocrHelper.ocrImage(image, output)
    if(file_extension == ".pdf"):
        count = preProcess.preprocessingPDF(path)
        ocrHelper.ocrPDF(path, count, output)


logging.info("done")

if __name__ == '__main__':
    main()
