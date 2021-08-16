#Program to generate equated monthly instalments (EMI)(intrest 5%/Month) of 3 year and 5 year of amount 161258/-

a=16125   #instalments for 3 years
    
e3=a/36   #instalments for 5 years
 
e5=a/60    #instalments for 3 years with 5% intrest
    
emi=e3+(0.05*e3)  #instalments for 5 years with 5% intrest

emi=e5+(0.05*e5)

print("EMI for 3 years with 5% intrest",emi)
     
print("EMI for 5 years with 5% intrest",emi)

     
