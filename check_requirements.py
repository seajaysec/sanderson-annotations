#!/usr/bin/python

import sys

print("Checking requirements...")

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('Could not import Beautiful Soup 4')
    print('sudo pip install BeautifulSoup4')
    sys.exit(1)

try:
    import genshi
except ImportError:
    print('Could not import Genshi')
    print('sudo pip install genshi')
    sys.exit(1)

try:
    import lxml
except ImportError:
    print('Could not import lxml')
    print('sudo pip install lxml')
    sys.exit(1)

try:
    import unidecode
except ImportError:
    print('Could not import unidecode')
    print('sudo pip install unidecode')
    sys.exit(1)

try:
    import titlecase
except ImportError:
    print('Could not import titlecase')
    print('sudo pip install titlecase')
    sys.exit(1)

