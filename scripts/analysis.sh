# Copyright 2019 Ryan Wick (rrwick@gmail.com)
# https://github.com/rrwick/August-2019-consensus-accuracy-update

# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should
# have received a copy of the GNU General Public License along with this program. If not, see
# <http://www.gnu.org/licenses/>.

python3 scripts/chop_up_assembly.py $1 100000 > pieces.fasta
minimap2 -x asm5 -t 8 -c hybrid_reference.fasta pieces.fasta > pieces.paf
python3 scripts/read_length_identity.py pieces.fasta pieces.paf > pieces.data
printf $1"\t"
python3 scripts/medians.py pieces.data
rm pieces.*
