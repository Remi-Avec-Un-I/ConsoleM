from enum import Enum
from string import printable
from functools import lru_cache

class Keys(Enum):
    SPACE = ' '
    ESCAPE = '\x1b' # this is the escape character, it is used to detect arrow keys and other special keys
    UP_ARROW = '\x1b[A'
    DOWN_ARROW = '\x1b[B'
    RIGHT_ARROW = '\x1b[C'
    LEFT_ARROW = '\x1b[D'
    TAB = '\t'
    ENTER = '\n'
    BACKSPACE = '\x7f'
    DELETE = '\x1b[3~'
    HOME = '\x1b[H'
    END = '\x1b[F'
    PG_UP = '\x1b[5~'
    PG_DOWN = '\x1b[6~'
    INSERT = '\x1b[2~'

    n0 = '0'
    n1 = '1'
    n2 = '2'
    n3 = '3'
    n4 = '4'
    n5 = '5'
    n6 = '6'
    n7 = '7'
    n8 = '8'
    n9 = '9'

    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    f = 'f'
    g = 'g'
    h = 'h'
    i = 'i'
    j = 'j'
    k = 'k'
    l = 'l'
    m = 'm'
    n = 'n'
    o = 'o'
    p = 'p'
    q = 'q'
    r = 'r'
    s = 's'
    t = 't'
    u = 'u'
    v = 'v'
    w = 'w'
    x = 'x'
    y = 'y'
    z = 'z'

    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    O = 'O'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    T = 'T'
    U = 'U'
    V = 'V'
    W = 'W'
    X = 'X'
    Y = 'Y'
    Z = 'Z'

    SQUARED = '²'
    AND = '&'
    E_ACUTE = 'é'
    QUOTE = '"' # "
    APOSTROPHE = "'" # '
    LEFT_PARENTHESIS = '('
    RIGHT_PARENTHESIS = ')'
    MINUS = '-'
    UNDERSCORE = '_'
    E_GRAVE = 'è'
    C_CEDILLA = 'ç'
    A_CIRCUMFLEX = 'â'
    E_CIRCUMFLEX = 'ê'
    I_CIRCUMFLEX = 'î'
    O_CIRCUMFLEX = 'ô'
    U_CIRCUMFLEX = 'û'
    A_GRAVE = 'à'
    EQUAL = '='
    PLUS = '+'
    PERCENT = '%'
    DOLLAR = '$'
    EURO = '€'
    POUND = '£'
    TILDE = '~'
    CARET = '^'
    DIESE = '#'
    STAR = '*'
    DEGREE = '°'
    SECTION = '§'
    o_SLASH = 'ø'
    O_SLASH = 'Ø'
    MU = 'µ'
    THORN = 'Þ'
    THORN2 = 'þ'
    ETH = 'Ð'
    ETH2 = 'ð'
    Æ = 'Æ'
    æ = 'æ'

    AT = '@'
    LEFT_SQUARE_BRACKET = '['
    RIGHT_SQUARE_BRACKET = ']'
    LEFT_CURLY_BRACKET = '{'
    RIGHT_CURLY_BRACKET = '}'
    BACKSLASH = '\\'
    PIPE = '|'
    SEMICOLON = ';'
    COLON = ':'
    EXCLAMATION_MARK = '!'
    QUESTION_MARK = '?'
    COMMA = ','
    DOT = '.'
    SLASH = '/'
    BACKQUOTE = '`'
    GRAVE = '`'
    ARROBASE = '@'




    CTRL_A = '\x01'
    CTRL_B = '\x02'
    CTRL_C = '\x03'
    CTRL_D = '\x04'
    CTRL_E = '\x05'
    CTRL_F = '\x06'
    CTRL_G = '\x07'
    CTRL_H = '\x08'
    CTRL_I = '\x09'
    CTRL_J = '\x0a'
    CTRL_K = '\x0b'
    CTRL_L = '\x0c'
    CTRL_M = '\x0d'
    CTRL_N = '\x0e'
    CTRL_O = '\x0f'
    CTRL_P = '\x10'
    CTRL_Q = '\x11'
    CTRL_R = '\x12'
    CTRL_S = '\x13'
    CTRL_T = '\x14'
    CTRL_U = '\x15'
    CTRL_V = '\x16'
    CTRL_W = '\x17'
    CTRL_X = '\x18'
    CTRL_Y = '\x19'
    CTRL_Z = '\x1a'

    F1 = '\x1bOP'
    F2 = '\x1bOQ'
    F3 = '\x1bOR'
    F4 = '\x1bOS'



    @classmethod
    @lru_cache()
    def get(cls, key, default=None):
        return cls.__members__.get(key, default)

    @classmethod
    @lru_cache(maxsize=1)
    def get_from_value(cls, value, default=None):
        for key in cls.__members__:
            if cls[key].value == value:
                return cls[key]
        return default

    @classmethod
    @lru_cache(maxsize=1)
    def get_all_keys(cls):
        return [key for key in cls]


    @classmethod
    def get_normal_chars(cls) -> list:
        return [
            cls.__members__[key] for key in cls.__members__
                if (Keys[key].value in printable or Keys[key].value.isalpha() or Keys[key].value.isdigit()) and len(Keys[key].value) == 1
        ]

    @classmethod
    @lru_cache(maxsize=1)
    def get_printable(cls) -> list:
        return [
            cls.__members__[key] for key in cls.__members__
                if Keys[key].value in printable
        ]

    @property
    def get_name(self):
        return self.name.lower().replace("_", " ")

if __name__ == "__main__":
    # get Keys.ARROW from "ARROW"
    print(Keys.__members__)
    print(Keys["SPACE"] in Keys.get_normal_chars(), Keys["SPACE"])
    print(Keys["SPACE"].value in printable)
    print(Keys.get("RIGHT_ARROW", "Not found"))
    print(Keys.get_normal_chars())