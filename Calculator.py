def cal(pre,back,method):
    pre=float(pre)
    back=float(back)
    if method=='+':
        return pre+back
    elif method=='-':
        return pre-back
    elif method=='*':
        return pre*back
    elif method=='/':
        return pre/back
    elif method=='%':
        return pre%back
    elif method=='^':
        return pre**back
def main():
    method=None
    memory=None
    waiting=False
    while(1):
        print('input:')
        if waiting:
            b=input()
            p=cal(memory,b,method)
            waiting=False
            print('out:',p)
        else:
            p=input()
        if p in ['+','-','*','/','%','^']:
            if memory==None:
                continue
            method=p
            waiting=True
            continue
        elif p=='':
            print(memory)
            continue
        memory=p
        if len(str(memory))>8:
            return 'error!'
if __name__ == "__main__":
    print(main())