################################################################################
# Author: Emily Cassanmagnago 
# Date: 02/21/2021
# This program calculates roulette colors
# based on pocket number
################################################################################

quan = int(input("Please input the number of packages to be purchased: "))
if quan <= 0:
	print("  Invalid Input!")
elif ((quan > 0) and (quan < 10)):
	print("  No discount applied.")
	total = quan * 99
	print("  The final price for purchasing %1d packages is $%10,.2f" % (quan, total))
elif ((quan >= 10) and (quan < 20)):
	print("  10% discount applied.")
	total = quan * 99
	total = total * 0.9
	print("  The final price for purchasing %1d packages is $%10,.2f" % (quan, total))
elif ((quan >= 20) and (quan < 50)):
	print("  25% discount applied.")
	total = quan * 99
	total = total * 0.75
	print("  The final price for purchasing %1d packages is $%10,.2f" % (quan, total))
elif ((quan >= 50) and (quan < 100)):
	print("  35% discount applied.")
	total = quan * 99
	total = total * 0.65
	print("  The final price for purchasing %1d packages is $%10,.2f" % (quan, total))
else:
	print("  45% discount applied.")
	total = quan * 99
	total = total * 0.55
	print("  The final price for purchasing %1d packages is $%10,.2f" % (quan, total))
