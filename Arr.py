Controller = True
Elements = []
sumA = 0


while Controller:
	Elements.append(input("Enter numbers"))
	Elements.append(input("Enter numbers"))



	Controller= False


for num in Elements:
	s = sum(map(int,str(num)))

	sumA += s

print(sumA)
