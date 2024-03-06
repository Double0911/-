#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    number = int(input())  #輸入的數字
    count = 0   #次方
    ans = 0    #答案(二進位)
    ans_16 = "" #答案(十六進位)
    #先算出輸入的數字小於2的幾次方
    while True:
        if 2**count < number:
            count += 1
        else:
            break
            
    #開始PPT上算二進位的邏輯        
    for i in range(count, -1, -1):
        if number >= 2**i:
            ans = ans + 10**i
            number = number - 2**i
            
        else:
            continue
    
    print("二進位為",ans)
    
    #算位數
    num_digit = len(str(ans))
    
    #四個為一組，不足四個多一組
    if num_digit % 4 != 0:
        group = (num_digit//4) + 1
    else:
        group = num_digit//4

    #PPT上邏輯
    for x in range(group,0,-1):
        temp_num = 0
        temp_16 = ""
        temp_num = (2**3)*(ans//(10**(4*x-1))%10) + (2**2)*(ans//(10**(4*x-2))%10)         + (2**1)*(ans//(10**(4*x-3))%10) + (2**0)*(ans//(10**(4*x-4))%10)
        if temp_num == 10:
            temp_16 = "A"
        elif temp_num == 11:
            temp_16 = "B"
        elif temp_num == 12:
            temp_16 = "C"
        elif temp_num == 13:
            temp_16 = "D"
        elif temp_num == 14:
            temp_16 = "E"
        elif temp_num == 15:
            temp_16 = "F"
        else:
            temp_16 = str(temp_num)

        ans_16 = ans_16 + temp_16
    
    print("16進位為",ans_16)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




