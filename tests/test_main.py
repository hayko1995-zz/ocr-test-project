import sys
sys.path.append('../ocr')
from ocr.ocr import main
from click.testing import CliRunner



def test_main():  # test software worsk or not
    runner = CliRunner()
    result = runner.invoke(main, input="..\ocr\sample\1.png")
    assert result.exit_code == 0
 
 #TODO add more testes