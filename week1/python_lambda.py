# x를 입력받아 m(x)를 출력하는 함수 lambda x: m(x)

def main():
    #두 수 x,y를 받아 [x와 y의 합, x와 y의 곱]의 리스트를 반환하는 함수
    addmul = lambda x,y: [x+y, x*y]
    res1 = addmul(10,4)
    res2 = addmul(19, 23)

    # 한글의 모든 가능한 자모음 조합을 차례로 원소로 가지는 리스트
    res3 = [chr(i) for i in range(ord('가'),ord('힣')+1)]

    # 0부터 122까지의 합
    res4 = sum(i for i in range(123))

    # 0부터 20까지 짝수만 리스트에 담는 필터
    res5 = list(filter(lambda x: x%2==0, range(20)))
    
    return res1, res2, res3, res4, res5

def print_ans(**kwargs):
    for key in kwargs.keys():
        print(key,':',kwargs[key])

res1, res2, res3, res4, res5 = main()
print_ans(res1=res1, res2=res2, res3=res3, res4=res4, res5=res5)
