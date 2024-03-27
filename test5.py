print("버튼1: 콜라, 버튼2: 사이다, 버튼3: 환타 입니다. 세개의 버튼 중 하나를 고르시오.")

a = input()
if a=='버튼1':
    print("콜라")
elif a=='버튼2':
    print("사이다")
elif a=='환타':
    print("환타")
else:
    print("정확히 입력해 주세요")



b=int(input())
bac = b//100
ship = (b-(bac*100))//10
il = b-(bac*100)-(ship*10)
print("백의 자리:",bac,"십의 자리:",ship,"일의 자리:",il)