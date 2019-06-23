string = "The b";  
count = 0;  
for i in range(0, len(string)):
    if(string[i] != ' '):
        count = count + 1;  
print("Total number of characters in a string: ",count);  