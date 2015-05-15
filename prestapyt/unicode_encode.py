#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def unicode2encoding(text, encoding='utf-8'):
    if sys.version_info < (3, 0):
        if isinstance(text, unicode):
            try:
                text = text.encode(encoding)
            except Exception:
                pass
    return text

def encode(text, encoding='utf-8'):
    if sys.version_info < (3, 0):
        if isinstance(text, (str, unicode)):
            return unicode2encoding(text, encoding=encoding)
    return str(text)
