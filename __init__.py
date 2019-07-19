__all__ = ['generators', 'parser']

# command line stuff
if __name__ == '__main__':
    import sys
    from .parser import parser

    input_fpath = sys.argv[1]
    output_fpath = sys.argv[2]

    ps = parser.Parser(input_fpath)
