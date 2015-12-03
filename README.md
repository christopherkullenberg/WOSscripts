# WOSscripts
A few scripts for processing ISI / Web of Science data.

WOSyears.py
- Extracts publication years from an ISI / Web of Science file and creates a histogram as a time series.
- Usage: python WOSyears.py file

WOSkeywordcloud.py
- Generates a wordcloud from a ISI / Web of Science file based on the Author Keywords (DE)
- Requires the wordcloud package - https://github.com/amueller/word_cloud
- Usage: python WOSkeywordcloud.py file

WoSTSVparser.py
- Parses records from the Web of Science when saved as TSV files (Mac OS, UTF-8)
- Includes brief descriptions as code comments.
- Tested with Python 3.4
- Usage: 1) Change filename in script, 2) python3 WoSTSVparser.py
