def check_angrams(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    
    if len(str1)!=len(str2):
        return False
    
    freq1={}
    freq2={}
    
    for char in str1:
        if char in freq1:
            freq1[char]+=1
        else:
            freq1[char]=1
            
    for char in str2:
        if char in freq2:
            freq2[char]+=1
        else:
            freq2[char]=1
    return freq1 == freq2

str1 = "listen"
str2 = "silent"

if check_angrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")