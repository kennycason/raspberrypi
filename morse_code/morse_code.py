from enum import Enum
from typing import Dict, List

# The length of a dot is one unit
# A dash is three units
# The space between parts of the same letter is one unit
# The space between letters is three units
# The space between words is seven units.

DOT_UNITS = 1
DASH_UNITS = 3
SIGNAL_BREAK_UNITS = 1
SYMBOL_BREAK_UNITS = 3
WORD_BREAK_UNITS = 7

UNIT_TIME = 0.1  # seconds
DOT_TIME = UNIT_TIME * DOT_UNITS
DASH_TIME = UNIT_TIME * DASH_UNITS
SIGNAL_BREAK_TIME = UNIT_TIME * SIGNAL_BREAK_UNITS
SYMBOL_BREAK_TIME = UNIT_TIME * SYMBOL_BREAK_UNITS
WORD_BREAK_TIME = UNIT_TIME * WORD_BREAK_UNITS

class Signal(Enum):
    DOT = 1
    DASH = 2

SYMBOL_MAP: Dict[str, List[Signal]] = {
    ' ': [],
    'A': [Signal.DOT, Signal.DASH],
    'B': [Signal.DASH, Signal.DOT, Signal.DOT, Signal.DOT],
    'C': [Signal.DASH, Signal.DOT, Signal.DASH, Signal.DOT],
    'D': [Signal.DASH, Signal.DOT, Signal.DOT],
    'E': [Signal.DOT],
    'F': [Signal.DOT, Signal.DOT, Signal.DASH, Signal.DOT],
    'G': [Signal.DASH, Signal.DASH, Signal.DOT],
    'H': [Signal.DOT, Signal.DOT, Signal.DOT, Signal.DOT],
    'I': [Signal.DOT, Signal.DOT],
    'J': [Signal.DOT, Signal.DASH, Signal.DASH, Signal.DASH],
    'K': [Signal.DASH, Signal.DOT, Signal.DASH],
    'L': [Signal.DOT, Signal.DASH, Signal.DOT, Signal.DOT],
    'M': [Signal.DASH, Signal.DASH],
    'N': [Signal.DASH, Signal.DOT],
    'O': [Signal.DASH, Signal.DASH, Signal.DASH],
    'P': [Signal.DOT, Signal.DASH, Signal.DASH, Signal.DOT],
    'Q': [Signal.DASH, Signal.DASH, Signal.DOT, Signal.DASH],
    'R': [Signal.DOT, Signal.DASH, Signal.DOT],
    'S': [Signal.DOT, Signal.DOT, Signal.DOT],
    'T': [Signal.DASH],
    'U': [Signal.DOT, Signal.DOT, Signal.DASH],
    'V': [Signal.DOT, Signal.DOT, Signal.DOT, Signal.DASH],
    'W': [Signal.DOT, Signal.DASH, Signal.DASH],
    'X': [Signal.DASH, Signal.DOT, Signal.DOT, Signal.DASH],
    'Y': [Signal.DASH, Signal.DOT, Signal.DASH, Signal.DASH],
    'Z': [Signal.DASH, Signal.DASH, Signal.DOT, Signal.DOT]
}