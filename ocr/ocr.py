# #!/usr/bin/python3
import click
import logging
import src.preprocessing as preProcess
import src.postproecessing as postProcess
import src.ocr as ocr


@click.command()
@click.option('--input', type=str, help='input file path')
@click.option('--output', type=str, help='output file path')
@click.option('--verbose', is_flag=True)
def main(input, output, verbose):
    verbose = not verbose
    logging.getLogger(__name__)
    if(not verbose):
        logging.basicConfig(level=logging.DEBUG)
    logging.debug("Start")
    _newImage = postProcess.preprocessingImage(input)
    results = ocr.ocr(_newImage)
    postProcess.postProcessing(results, type, output)


if __name__ == '__main__':
    main()
