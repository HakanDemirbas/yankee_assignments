# PART 2
def bottle_song(num):
	# num = int(input(f"How many bottle(s) of beer: "))
	og_num = num

	if num > 1:
		print(f"{num} bottles of beer on the wall, {num} bottles of beer.")
		print(f"Take one down and pass it around, {num-1} bottles of beer on the wall.")
		bottle_song(num-1)
	elif num == 1:
		print(f"{num} bottle of beer on the wall, {num} bottle of beer.")
		print(f"Take one down and pass it around, {num-1} bottle of beer on the wall.")
		print(f"No more bottles of beer on the wall, no more bottles of beer.")
		print(f"Go to the store and buy some more, {og_num} bottles of beer on the wall.")


# PART 1
# def bottle_song():
# 	num = int(input(f"How many bottle(s) of beer: "))
# 	for i in range(num,0,-1):
# 		if i > 1:
# 			print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
# 			print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
# 		elif i == 1:
# 			print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
# 			print(f"Take one down and pass it around, {i-1} bottle of beer on the wall.")
# 			print(f"No more bottles of beer on the wall, no more bottles of beer.")
# 			print(f"Go to the store and buy some more, {num} bottles of beer on the wall.")

bottle_song(5)

"""
# need to have a user input for the num of bottles
# can use a for loop with a range of the num from 0 to num
# if num is greater than 2, print the first statement
# print the num of bottles and bottles on the wall and take one down
# and pass it around which will be num - 1 and store in separate variable
elif statement with the same thing but now if num == to 1 
print the same things as 12 and 13 but now with "bottle" instead
else print no more bottles and go to the store and print the num of the original num
"""