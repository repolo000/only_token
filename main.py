if __name__=='__main__':
    with open('tokens.txt','r') as f:
        tokens=f.read().split('\n')
    go=[]
    for token in tokens:
        try:
            if not token=='':
                tokenone=token.split(':')[2]
        except:
            print('이메일:비밀번호:토큰 순으로 입력해주세요')
            print('========================================================')
            exit()
        go.append(tokenone)
    with open('tokens.txt','w') as f:
        f.write('\n'.join(go))
    print(f'총 {len(go)}개의 토큰이 입력되었습니다.')
    print('========================================================')
    print('tokens.txt 파일을 열어서 확인해주세요.')
    print('========================================================')
    input()
