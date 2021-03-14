cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',\
        'B', 'B', 'F', 'F', 'B', 'F']

cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',\
        'B', 'B', 'F', 'F', 'F', 'F']

cap3 = [] 

def pleaseConformOnepass(caps):
    #　追加
    try:
        caps = caps + [caps[0]]
    except IndexError:
        return print("list is empty")

    for i in range(1, len(caps)):    
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                print('People in positons', i, end=' ')
                f_start = i 
            else:
                # 追加
                if i - f_start == 1:
                    print('flip your caps')
                    continue
                print('though', i-1, 'flip your caps')


pleaseConformOnepass(cap1)