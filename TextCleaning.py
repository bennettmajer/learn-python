#!/usr/local/bin/python3

"""TextCleaning.py: Methods to clean unstructured text data"""

__author__ = "Bennett Majerowski"


extracted_data = """I luv my &lt;3 iphone &amp;
you’re awsm apple.DisplayIsAwesome,
sooo happppppy 🙂 http://www.apple.com"""

print(extracted_data)


# 1. Escape HTML characters
# Data from the web has lots of garbage. Get rid of the garbage.
from html.parser import HTMLParser
html_parser = HTMLParser()
tweet = html_parser.unescape(extracted_data)
print(tweet)


# 2. Decoding data
# Transforming complex symbols into easier to understand characters

# maybe i won't continue
