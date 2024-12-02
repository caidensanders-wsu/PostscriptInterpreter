import math

mappings = [
	["add", lambda x: add_operation(x)],
	["div", lambda x: div_operation(x)],
	["sub", lambda x: sub_operation(x)],
	["idiv", lambda x: idiv_operation(x)],
	["mul", lambda x: mul_operation(x)],
	["mod", lambda x: mod_operation(x)],
	["abs", lambda x: abs_operation(x)],
	["neg", lambda x: neg_operation(x)],
	["ceiling", lambda x: ceiling_operation(x)],
	["floor", lambda x: floor_operation(x)],
	["round", lambda x: round_operation(x)],
	["sqrt", lambda x: sqrt_operation(x)],
]

def add_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op1 + op2
	stack.push(res)

def div_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	divisor = stack.pop()
	dividend = stack.pop()
	quotient = dividend / divisor
	stack.push(quotient)

def sub_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return
	
	subtrahend = stack.pop()
	minuend = stack.pop()
	difference = minuend - subtrahend
	stack.push(difference)

def idiv_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	divisor = stack.pop()
	dividend = stack.pop()
	quotient = dividend / divisor
	stack.push(math.floor(quotient))

def mul_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op1 * op2
	stack.push(res)

def mod_operation(stack):
	if stack.size() < 2:
		print("not enough operands.")
		return

	divisor = stack.pop()
	dividend = stack.pop()
	remainder = dividend % divisor
	stack.push(remainder)

def abs_operation(stack):
	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()
	res = abs(op)
	stack.push(res)

def neg_operation(stack):
	if stack.size() < 1:
		print("not enough operands.")
		return
	
	op = stack.pop()
	res = op * -1
	stack.push(res)

def ceiling_operation(stack):
	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()
	res = math.ceil(op)
	stack.push(res)

def floor_operation(stack):
	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()
	res = math.floor(op)
	stack.push(res)

def round_operation(stack):
	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()
	res = round(op)
	stack.push(res)

def sqrt_operation(stack):
	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()
	res = math.sqrt(op)
	stack.push(res)
