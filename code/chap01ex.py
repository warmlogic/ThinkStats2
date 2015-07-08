"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG resp data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemResp(df)
    return df

def CleanFemResp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass

def ValidatePregnum(df_resp):
    # read the pregnancy dataframe
    preg = nsfg.ReadFemPreg()
    
    # dictionary to map caseid to indices of pregnancies in preg df
    preg_map = nsfg.MakePregMap(preg)
    
    for case in df_resp['caseid'].unique():
        if len(preg_map[case]) != df_resp[df_resp['caseid'] == case].pregnum.values:
            print(case)
            return False
    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
