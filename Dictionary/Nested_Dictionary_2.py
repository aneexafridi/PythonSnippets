Items = {
"RBOO111":{"name":"Royban Sunglasses","price":112.98,"models":["Black","Tortoise"]},
"DWCO317":{"name":"Drone with Camera","price":72.95,"models":["White","Black"]},
"MTS0540":{"name":"T-Shirt","price":2.95,"models":["small","medium","large"]},
"ECD2989":{"name":"Echo Dot","price":29.99}
}
print(f"{'ID key':<20}{'Name':<15}{'price':<15}{'models'}")
print("*"*70)
for u  in Items:
	print(u,end=" \t\t")
	for v in Items[u]:
		print(Items[u][v],"\t\t",end=" ")
	print()
