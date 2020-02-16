from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))

from mrz.generator.td1_belgian import TD1CodeGenerator  # Comment this line AFTER BUILD or INSTALL
#from build.lib.mrz.generator.td1_belgian import TD1CodeGenerator   OPEN AFTER BUILD or INSTALL

print(TD1CodeGenerator("ID",                # Document type   Normally 'I' or 'ID' for id cards              
                       "BEL",               # Country         3 letters code or country name        
                       "5920785560139",#!!!!!! Document number | 12 numbers for the belgian ID cards | 9 + < + 3 + <<<<<<<<<<<
                                       #!!!!!! where '<' = 0
                       "871111",            # Birth date      YYMMDD
                       "M",                 # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "250316",            # Expiry date     YYMMDD
                       "BEL",               # Nationality
                       "Van Der Velden",    # Surname         Special characters will be transliterated     
                       "GREET HILDE",       # Given name(s)   Special characters will be transliterated
                       "",                  # Optional data 1)
                       "87111122390"))      # Optional data 2)
