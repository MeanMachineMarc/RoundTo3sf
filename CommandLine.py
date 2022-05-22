import RoundTo3sf

while True:
    num=float(input("Enter number: "))
    if num<0:
        print(-1*RoundTo3sf.round_3sf(num))
    else:
        print(RoundTo3sf.round_3sf(num))
