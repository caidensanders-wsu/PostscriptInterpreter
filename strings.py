mappings = [
	["length", lambda x: length_operation(x)],
	["get", lambda x: get_operation(x)],
	["getinterval", lambda x: get_interval_operation(x)],
	["putinterval", lambda x: put_interval_operation(x)],
]

def length_operation(stack):
	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()

	if not isinstance(op, str):
		print("operand must be a string.")
		return

	stack.push(len(op))

def get_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	index = stack.pop()
	op = stack.pop()

	if not isinstance(op, str):
		print("operand must be a string.")
		return

	if len(op) < index:
		print("index out of bounds.")
		return

	stack.push(op[index])

def get_interval_operation(stack):
	if stack.size() < 3:
		print("not enough operands.")
		return

	count = stack.pop()
	index = stack.pop()
	op = stack.pop()

	if not isinstance(op, str):
		print("operand must be a string.")
		return

	if len(op) < index + count:
		print("index out of bounds.")
		return

	stack.push(op[index : index + count])

def put_interval_operation(stack):
	if stack.size() < 3:
		print("not enough operands.")
		return

	string2 = stack.pop()
	index = stack.pop()
	string1 = stack.pop()

	if not (isinstance(string2, str) or isinstance(string1, str)):
		print("operand must be a string.")
		return

	if len(string1) < index:
		print("index out of bounds.")
		return

	stack.push(string1[:index] + string2 + string1[index:])
