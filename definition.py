import re
import urllib.request

try:

    word = input('Enter your word: ')
    url = 'http://www.dictionary.com/browse/' + word

    data = urllib.request.urlopen(url).read()
    data1 = data.decode('utf-8')

    m = re.search('meta name="description" content="', data1)
    start = m.end()
    end = start + 300

    newString = data1[start:end]

    m = re.search('See more.', newString)
    end = m.start() - 1

    final = newString[0:end]
    print(final)

except:
    print('Sorry, but your word is not in the dictionary. Please try again.')
