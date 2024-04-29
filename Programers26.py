n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

answer = [] # ["######", "### #", "## ##", " #### ", " #####", "### # "]


#print(bin(8)[2:])
print(bin(31))
print(bin(14))
print(bin(31|14))

for i in range(0,len(arr1)):
    result = '{}'.format((bin(arr1[i]|arr2[i])[2:])).zfill(n)
    print(result)
    # result = result.replace('1','#')
    # result = result.replace('0',' ')
    # answer.append(result)
    
# print(answer)
    

            

    
    

    






