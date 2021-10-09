import os
import time
import random


DEFAULT_FILE = "quotes.txt"


class QuoteList:
    def __init__(self, quotes_file=DEFAULT_FILE):
        self.filename = quotes_file
        self._load()
    def _load(self):
        self.quotes = []
        self.loadtime = time.time()
        with open(self.filename) as f:
            text = f.read()
        pars = text.split('\n\n')
        for p in pars:
            lines = [l for l in p.splitlines() if l and not l[0]=="#"]
            if not lines: continue
            quote = ' '.join(lines)
            self.quotes.append(quote)
    def load(self):
        # reload if needed
        if self.loadtime < os.path.getmtime(self.filename):
            self._load()
    def qotd(self):
        self.load()
        return random.choice(self.quotes)
    def __len__(self):
        self.load()
        return len(self.quotes)
