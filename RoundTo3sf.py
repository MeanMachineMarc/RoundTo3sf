import sign

def round_3sf(num):
    if (num) - int(num) == 0: #Integer
       decimalPlaces= 3 - len(str(int(num)))
       rounded = round(int(num),decimalPlaces)
       
    elif int(num) > 0: #Float, > 1
       len_b4_dp = len(str(int(num)))
       len_aft_dp = len(str(num))-len_b4_dp - 1
       decimalPlaces= 4 + len_aft_dp - len(str(num))
       rounded = round(num,decimalPlaces)
       
    else: #Negative Float or Float, < 1
       hold1 = num 
       hold2 = abs(num)
       num = abs(num)
       count = 0
       while num < 1:
             count = count + 1
             num = 10 * num    
       
       if sign.sign(hold1) == -1 and hold2 > 1: #Negative Float, abs > 1
          len_b4_dp = len(str(int(num)))
          len_aft_dp = len(str(num)) - len_b4_dp - 1
          decimalPlaces = 4 + len_aft_dp - len(str(num))
          rounded = round(hold1,decimalPlaces)
     
       else: #Float, abs < 1
          decimalPlaces = 2 + count 
          rounded = round(hold1,decimalPlaces)    

    return rounded

