mappings = [
	["print", lambda x: print_operation(x)],
	["=", lambda x: equals_print_operation(x)],
	["==", lambda x: double_equals_print_operation(x)],
	["pstack", lambda x: pstack_operation(x)],
]

def print_operation(stack):
	if stack.size() < 1:
		print("not enough operands")
		return

	if isinstance(stack.peek(), str):
		print(stack.pop())

def equals_print_operation(stack):
	if stack.size() < 1:
		print("not enough operands.")
		return

	print(stack.pop())

def double_equals_print_operation(stack):
	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()

	if isinstance(op, str):
		print('(' + op + ')')
	else:
		print(op)

def pstack_operation(stack):
	if stack.size() < 1:
		print("not enough operands.")
		return

	items = []

	try:
		while True:
			items.append(stack.pop())
	except IndexError:
		for item in items:
			if isinstance(item, str):
				print('(' + item + ')')
			else:
				print(item)
		for item in reversed(items):
			stack.push(item)
