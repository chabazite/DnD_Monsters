
def clean_list(list_):
    '''
    Cleanup a poorly made list-like string so it can be transformed into a list
    
    input:
            list_: list-like string (ex. 'Str+8, Dex+5, Int+3'). It has to be missing quotes around items and brackets.
    
    output:
            list_: Cleaned list-like string ready for conversion (ex. ['Str+8','Dex+5','Int+3'])
    '''

    list_ = list_.replace(', ', '","')
    list_ = '["'+list_+'"]'
    return list_
