def main():
    print('please input binary number:')
    s=input()
    result=0
    k=0
    for i in s[::-1]:
        if i =='1':
            result+=2**k
        elif i!='0':
            print('input error!')
        k+=1
    print('result is:',result)
if __name__ == '__main__':
    main()