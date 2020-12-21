import resources.lib.yifytest as tst
import pytest

@pytest.fixture
def testservice():
  return tst.TestService()

def test_lookup(testservice):
  # test = tst.TestService()
  assert testservice.lookup('oblivion','2013') == 'tt1483013'
  # assert imdb == 'tt1483013'

def test_search(testservice):
  print(testservice.search('tt1483013', 'French'))
  # assert testservice.search('tt1483013')
# Kingsman Services Secrets (2015)
# imdb=test.lookup('Insaisissables' ,'2013')
# test.search(imdb,'French')