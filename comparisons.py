mappings = [
	["eq", lambda x: eq_operation(x)],
	["ne", lambda x: ne_operation(x)],
	["ge", lambda x: ge_operation(x)],
	["gt", lambda x: gt_operation(x)],
	["le", lambda x: le_operation(x)],
	["lt", lambda x: lt_operation(x)],
	["and", lambda x: and_operation(x)],
	["or", lambda x: or_operation(x)],
]

def eq_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return
	
	op1 = stack.pop()
	op2 = stack.pop()
	res = op1 == op2
	stack.push(res)

def ne_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = not (op1 == op2)
	stack.push(res)

def ge_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op2 >= op1
	stack.push(res)

def gt_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op2 > op1
	stack.push(res)

def le_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op2 <= op1
	stack.push(res)

def lt_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op2 < op1
	stack.push(res)

def and_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op1 and op2
	stack.push(res)

def or_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op1 or op2
	stack.push(res)
