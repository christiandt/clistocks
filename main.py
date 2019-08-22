#!/usr/bin/env python
from security import Security
from searcher import Searcher

# Use issueId directly
apple = Security("36276")
print apple

# Or search for it using the Searcher
google = Security(str(Searcher('GOOG')))
print google

# Include exchange for better result
tesla = Security(str(Searcher('TSLA:NSQ')))
print tesla
