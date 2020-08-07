import os
import regex as re

def chdir2cwd( file=__file__ ):
    # print( os.getcwd() )
    excute_file_path = os.path.dirname(os.path.realpath( file ))
    os.chdir( excute_file_path )

cjk_range = "[\p{Han}]"
CJK = re.compile( cjk_range, re.UNICODE)

def extract_han( text, cjk=CJK ):
    return "".join( re.findall( cjk, text  ) )

def n_gram( text, n ):
    size = len( text )
    return [ text[i:i+n] for i in range(size-n+1) ]

def build_ridx( lst ):
    ridx = {}
    for i, em in enumerate( lst ):
        for k in em:
            if ridx.get( k ): ridx[k].append( i )
            else: ridx[k] = [ i ]
    return ridx

def flatten( lst ):
    return sum( lst, [] )

def uniq( lst ):
    return list( dict.fromkeys( lst ) )

def pair2group( lst ):                # lst : [[a,b], [a,c], [a,d,u], [c,d] ... ]
    ridx = build_ridx( lst )            # ridx : { 'a': [0,1,2], 'b':[0] ... }
    idx_list_of_pair = [ uniq( flatten( [ ridx.get( e ) for e in pair ] ) ) for pair in lst ]
    new_lst_ = [ sorted( uniq( flatten( [ lst[i] for i in idx_arr ] ) ) ) for idx_arr in idx_list_of_pair ]
    # 중복 셋트 삭제
    new_lst_ = uniq( [ tuple(item) for item in new_lst_ ] )
    # 결과 정리
    new_lst = [ list(item) for item in new_lst_ ]
    if len( lst ) ==  len( new_lst ):
        return new_lst
    else:
        return pair2group( new_lst )
