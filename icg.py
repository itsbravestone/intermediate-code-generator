from collections import defaultdict

def get_prior(op):
    prior={"*":1,"/":1,"+":2,"-":2}
    high=op[0]
    for o in op:
        if prior[o] < prior[high]:
            high = o
            break
        return high

def is_op(o):
    op=["*","/","+","-"]
    if o in op:
        return True
    else:
        return False

def tac(string):
    op=[]
    tokens=string.split()
    tad=defaultdict(str)

    for t in tokens:
        if is_op(t):
            op.append(t)

    j=1
    while op:
        high=get_prior(op)
        idx=op.index(high)
        op.pop(idx)

        idx_str=tokens.index(high)
        if len(tad)==0:
            tad["T"+ str(j)]=""+ tokens[idx_str-1] + tokens[idx_str] + tokens[idx_str+1]
            j+=1
        else:
            before=tokens[idx_str-1]
            after=tokens[idx_str+1]
            temp_before=before
            temp_after=after
            for key,val in tad.items():
                if before in val:
                    temp_before=str(key)
                if after in val:
                    temp_after=str(key)
            tad["T"+ str(j)]=temp_before + high + temp_after
            j+=1
    print("\nThe three address code for "+string+" is:")
    for key,value in tad.items():
        print(key," = ",value)
tac("a + b * c - d")
tac("a * b / c - d")
