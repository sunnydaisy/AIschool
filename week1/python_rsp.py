# 가위바위보 머신 만들기 

import random as rd

def machine(**kwargs): 
    rsp_win = {'가위':'바위','보':'가위','바위':'보'}
    try:
        num_defeat = kwargs['defeat']
        del kwargs['defeat']
    except:
        num_defeat = 0
    results = []
    len_trial = []

    for key in kwargs.keys():
        len_trial = len(kwargs[key])
        r = []
        for i in kwargs[key]:
            r.append(rsp_win[i])
        results.append(r)
    for i in range(num_defeat):
        n = rd.randrange(len(results))
        m = rd.randrange(len(results[n]))
        results[n][m] = rsp_win[results[n][m]]
    return results

print(machine(t1=['가위','바위','보'],t2=['보','보']))
print(machine(t1=['가위','바위','보'],t2=['보','보'],defeat=1))
print(machine(t1=['가위','바위','보'],t2=['가위','바위','바위'],t3=['가위','가위'],defeat=5))

