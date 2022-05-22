import Sign

def round_3sf(num):
    num2=float(num)
    if (num)-int(num)==0: #Integer
       decimalPlaces=3-len(str(int(num)))
       rounded=round(int(num),decimalPlaces)
       
    elif int(num)>0: 
       num=abs(num)
       len_b4_dp=len(str(int(num)))
       len_aft_dp=len(str(num))-len_b4_dp-1
       decimalPlaces=4+len_aft_dp-len(str(num))
       rounded=round(num,decimalPlaces)
       
    else:  
       num1=num
       num=abs(num)
       count=0
       while num<1:
             count=count+1
             num=10*num               
       decimalPlaces=2+count      
       rounded=round(num1,decimalPlaces)   

    return rounded

