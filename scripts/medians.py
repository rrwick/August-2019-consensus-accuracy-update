#!/usr/bin/env python3
"""
Copyright 2019 Ryan Wick (rrwick@gmail.com)
https://github.com/rrwick/August-2019-consensus-accuracy-update

This program is free software: you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version. This program is distributed in the hope that it
will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should
have received a copy of the GNU General Public License along with this program. If not, see
<http://www.gnu.org/licenses/>.
"""

import statistics
import sys


def main():
    data_filename = sys.argv[1]
    identities = []
    with open(data_filename, 'rt') as data:
        for line in data:
            if line.startswith('Name'):
                continue
            parts = line.strip().split('\t')
            identities.append(float(parts[2]))
    print(f'{statistics.median(identities)}%')


if __name__ == '__main__':
    main()
