
def has_teen(a, b, c):
	if a >= 13 and a <= 19:
		return True 
	if b >= 13 and b <= 19:
		return True 
	if c >= 13 and c <= 19:
		return True 		
	else:
		return False

print has_teen(1, 2, 3)#False
print has_teen(1, 13, 3)#True 
print has_teen(14, 2, 3)#^
print has_teen(1, 2, 15)#^
print has_teen(16, 17, 3)#^
print has_teen(18, 2, 19)#^
print has_teen(1, 18, 17)#^
print has_teen(16, 15, 14)#^

def not_string(str):
	if not str.startswith("not"):
		return ("not" +  str)
	else:
		return (str + "not")

print not_string("not selfish")
print not_string("selfish")	

def icy_hot(a, b):
	if a > 100 and b >= 100:
		return False
	if a < 0 and b <= 0:
		return False
	if a < 0 or a > 100:
		return True
	if b < 0 or b > 100:
		return True
	else:
		return False

print icy_hot(-3, 50)#True
print icy_hot(0, 101)#True
print icy_hot(60, 60)#False

def closer_to(a, b, c):
	guess1 = a - b
	guess2 = a - c
	if abs(guess1) > abs(guess2):
		return c
	if abs(guess1) < abs(guess2):
		return b
	if abs(guess1) == abs(guess2):
		return 0
	

print closer_to(100, 150, 150)#Return 0
print closer_to(100, 50, 101)#Return b
print closer_to(100, 102, 50)#Return a

def two_as_one(a, b, c):
	if a + b == c:
		return True
	if a + c == b:
		return True 
	if b + c == a:
		return True
	else:
		return False

print two_as_one(1, 2, 3)#True
print two_as_one(1, 4, 3)#True
print two_as_one(7, 4, 3)#True
print two_as_one(2, 4, 3)#False
print two_as_one(200, 2, 4)#False

def pig_latinify(str):
	if str.startswith("a") or str.startswith("e") or str.startswith("i") or str.startswith("o") or str.startswith("u"):
		return(str + "way")
	if str.startswith("A") or str.startswith("E") or str.startswith("I") or str.startswith("I") or str.startswith("U"):
		return(str + "way")	

print pig_latinify("and")
print pig_latinify("eat")
print pig_latinify("isotope")
print pig_latinify("olivander")
print pig_latinify("ukelele")
print pig_latinify("And")
print pig_latinify("Eat")
print pig_latinify("Isotope")
print pig_latinify("Olivander")
print pig_latinify("Ukelele")
# print pig_latinify("basket")
# print pig_latinify("salad")
# print pig_latinify("apple")
# print pig_latinify("apple ")
# print pig_latinify("fuck")
# print pig_latinify("fuck ")



