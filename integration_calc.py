def f(mode, x):
	if mode == 1:
		return (5*(x**4)) + (3*(x**3)) - (10*(x)) + 2
	elif mode == 2:
		return (x**2) - 10
	elif mode == 3:
		return (40*x) + 5
	elif mode == 4:
		return x**3
	elif mode == 5:
		return (20*(x**2)) + (10*(x)) - 2
	else:
		quit()

def fprint(modes):
	if modes == 1:
		print("5x**4 + 3x**3 - 10x + 2", end="")
	elif modes == 2:
		print("(x**2) - 10", end="")
	elif modes == 3:
		print("40*x + 5", end="")
	elif modes == 4:
		print("x**3", end="")
	elif modes == 5:
		print("20*(x**2) + 10*x - 2", end ="")

def rectangle(start, end, step, mode_enter):
	total = 0
	true_start = start
	while start != end:
		start += step
		area = step * (f(mode_enter, start))
		total += area
	print("Your total area under ", end="") 
	fprint(mode_enter)
	print(" between " + str(true_start) + " and " + str(end)  + " using RSUM is "  + str(total))

def trapezoid(start, end, step, mode_enter):
	total = 0
	true_start = start
	while start != end:
		area = (((f(mode_enter, start)) + (f(mode_enter, start+step)))/2)*step
		start += step
		total += area
	print("Your total area under ", end="")
	fprint(mode_enter)
	print(" between " + str(true_start) + " and " + str(end)  + " using Trapezoidal rule is  "  + str(total))

def good_variable():
	while True:
		try:
			mode_enter = float(input("choose a function: 1, 2, 3, 4, 5, other(quit): "))	
		except ValueError or NameError:
			quit()
		else:
			if mode_enter in range(1, 6):
				while True:
					try:
						rec_trap = float(input("Would you like to calculate the area using the rectangle, trapezoid, or both(1, 2, 3): "))
						if rec_trap in range(1, 4):
							start = float(input("What is your starting number?: "))
							end = float(input("What is your ending number?: "))
							total_rectrap = float(input("How many rec/trap do you want?: "))
							break
					except ValueError or NameError:
						print("Please input a valid number. Try again.")
					else:
						print('Please select a mode of calculation.')
				break
			else:
				quit()
	difference = end - start
	step = (difference/total_rectrap)
	if rec_trap == 1:
		rectangle(start, end, step, mode_enter)
	elif rec_trap == 2:
		trapezoid(start, end, step, mode_enter)
	elif rec_trap == 3:
		rectangle(start, end, step, mode_enter)
		trapezoid(start, end, step, mode_enter)

def main():
	play = True
	while play == True:
		print("f1(x) = 5x**4 + 3x**3 - 10x + 2")
		print("f2(x) = (x**2) - 10")
		print("f3(x) = 40*x + 5")
		print("f4(x) = x**3")
		print("f5(x) = 20*(x**2) + 10*x - 2")
		good_variable()
		if play == True:
			print("Do you want to keep calculating? (yes or no)")
			play = input().lower().startswith('y')
main()


