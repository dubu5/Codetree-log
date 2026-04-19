a, b, c = map(int, input().split())

sum = a+b+c
avr = sum // 3 # 3의 배수니까 몫연산해도 무방함

print(f"{sum}\n{avr}\n{sum-avr}")