import os
import glob
from core import MapReduce, parse_doc_mr

DATADIR = "../dataset"

if __name__ == '__main__':
    data_files = glob.glob(os.path.join(DATADIR, "*"))

    mapper = MapReduce(parse_doc_mr)
    print(mapper(data_files, chunksize=8))
