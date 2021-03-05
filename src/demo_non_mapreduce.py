from core import Inverted_Index_Generator

DATADIR = "../dataset"

if __name__ == '__main__':
    gen = Inverted_Index_Generator(DATADIR)

    inverted_index = gen.generate()

    print(inverted_index)