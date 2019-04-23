#!/usr/bin/env python3
#-*- coding: utf-8 -*-


import bz2
import json





def mk_meme_corpus(infile, outfile = 'picked_comments.bz2', min_score = 100, min_len = 1, max_len = 50):
    with bz2.open(outfile, 'wb') as f_write:
        for line in infile:
            line = line.decode('utf-8')
            line_dict = json.loads(line)
            if line_dict['body'] and 0 < len(line_dict['body']) < 51:
                if line_dict['score'] and line_dict['score'] > 99:
                    comment = line_dict['body'].encode()
                    #print(comment)
                    f_write.write(comment)
                    f_write.write(b'\n')
    f_write.close()


def main():
    infile = bz2.open('RC_2012-06.bz2')
    mk_meme_corpus(infile)

if __name__ == "__main__":
    main()

