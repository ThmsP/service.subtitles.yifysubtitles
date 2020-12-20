import yifytest as tst

test = tst.TestService()
# imdb=test.lookup('oblivion','2013')
# Kingsman Services Secrets (2015)
imdb=test.lookup('Insaisissables' ,'2013')
test.search(imdb,'French')