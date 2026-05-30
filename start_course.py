#!/usr/bin/env python3
"""Запуск курса «Псевдокод → Python» (в стиле Brilliant)"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'course'))
from cli import main

if __name__ == '__main__':
    main()
