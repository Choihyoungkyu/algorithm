#시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
N = int(input())
if 90<=N<=100:
    print('A')
elif 80<=N<90:
    print('B')
elif 70<=N<80:
    print('C')
elif 60<=N<70:
    print('D')
else:
    print('F')