from random import sample,shuffle

lower_case = [chr(c) for c in range(97,123)]
upper_case = [chr(c) for c in range(65,91)]
Dights = [0,1,2,3,4,5,6,7,8,9]
Special_char = ['!','_','.','*']

List = list()
List.extend(lower_case)
List.extend(upper_case)
List.extend(Dights)
List.extend(Special_char)

password = sample(List,k=9)

print((password))

