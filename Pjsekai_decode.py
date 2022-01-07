import os, sys
import binascii
from bitarray import bitarray
import glob

def decode(path, prefix = "_"):
    skip = 4	# first skip size (Byte)
    header_size = 128
    chunk_size = 8
    invert_cnt = 5

    file_name = os.path.basename(path)
    write_path = os.path.join(os.path.dirname(path), prefix + file_name)

    with open(path, 'rb') as fi, open(write_path, 'wb') as fw:
        # skip first skipping Bytes
        fi.seek(skip, os.SEEK_CUR)

        # invert some bytes on header of 128 Bytes
        # execute every 8 Bytes chunks
        for i in range((int)(header_size / chunk_size)):
            # invert first 5 Bytes
            chunk = fi.read(invert_cnt)
            # print(chunk)
            bits = bitarray()
            bits.frombytes(chunk)
            # print(bits)
            fw.write((~bits).tobytes())

            # write through last 3 Bytes
            chunk = fi.read(chunk_size - invert_cnt)
            # print(chunk)
            # bits = bitarray()
            # bits.frombytes(chunk)
            # print(bits)
            fw.write(chunk)
  
        # write rest of bin datas
        rest = fi.read()
        fw.write(rest)
    
    print("Decoded: " + file_path)


if __name__ == '__main__':
    for file_path in glob.glob(sys.argv[1], recursive=True):
        if not os.path.exists(file_path):
            print("Not exist: " + file_path)
        else:
            if os.path.isdir(file_path):
                continue
            decode(file_path, "m_")