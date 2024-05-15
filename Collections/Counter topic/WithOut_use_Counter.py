List = [1,4,3,2,1,1,1,3,1,5,1,1,2,1,4]

print(List,'\n')
# also apply in only once come the element in list
# just instead of max write "min"

Element = max(set(List),key=List.count)

Time_occur = max(map(List.count,set(List)))
# Time_occur = max([List.count(u) for u in set(List)])

print(f'Frequently occur Element: {Element}')
print(f'Time occur {Time_occur}')