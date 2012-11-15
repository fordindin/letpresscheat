#!/usr/bin/env python
# coding: utf-8

import os
import re
from sys import argv
from os.path import basename,dirname,realpath

if len(argv) == 1 or argv[1] in ("-h", "--help"):
		print "%s <list of letters> [<filter letters>]" % basename(argv[0])

letters=argv[1]
workingdir=dirname(realpath(argv[0]))
dictpath=os.path.join(workingdir, "Mueller7accentGPL.ru_RU.UTF-8")

dictf=open(dictpath)
dictd=dictf.readlines()
dictf.close()

words=[]

for l in dictd:
		regex = re.compile("\\b[%s]{1,12}\\b" % letters)
		m = regex.match(l)
		next_word=False
		if m:
				w = m.group()
				for l in letters:
						if letters.count(l) < w.count(l):
								next_word=True
								break
				if next_word: continue
				else: words.append(w)

def cmp(a,b):
		if len (a) > len (b): return 1
		elif len (a) == len (b): return 0
		else: return -1
words=list(set(words))
words.sort(cmp=cmp)

for w in words:
		if len(argv) > 2:
				nextl = False
				for l in argv[2]:
						if w.count(l) == 0:
								nextl=True
								break
						if nextl: continue
				if not nextl: print w
		else:
				print w
