def round_3sf(num):
    if (num)-int(num)==0:
       num=abs(num)
       x=3-len(str(int(num)))
       rounded=round(int(num),x)
       return rounded
    elif int(num)>0:
       num=abs(num)
       len_b4_dp=len(str(int(num)))
       len_aft_dp=len(str(num))-len_b4_dp-1
       x=4+len_aft_dp-len(str(num))
       rounded=round(num,x)
       return rounded
    else:  
       num=abs(num)
       num1=num
       count=0
       while num<1:
             count=count+1
             num=10*num               
       x=2+count      
       rounded=round(num1,x)     
       return rounded
while True:
    num=float(input("Enter number: "))
    if num<0:
       print(-1*round_3sf(num))
    else:
       print(round_3sf(num)) 
