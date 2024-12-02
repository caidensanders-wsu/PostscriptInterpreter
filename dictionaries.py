from limiteddict import LimitedDict

mappings = [
	["dict", lambda x, y: dict_operation(x, y)],
	["length", lambda x, y: length_operation(x, y)],
	["maxlength", lambda x, y: maxlength_operation(x, y)],
	["begin", lambda x, y: begin_operation(x, y)],
	["end", lambda x, y: end_operation(x, y)],
	["def", lambda x, y: def_operation(x, y)], 
]

def dict_operation(operand_stack, dictionary_stack):
	if operand_stack.size() < 1:
		print("not enough operands.")
		return

	max_length = operand_stack.pop()

	operand_stack.push(LimitedDict(max_length))

def length_operation(operand_stack, dictionary_stack):
	pass

def maxlength_operation(operand_stack, dictionary_stack):
	operand_stack.push(dictionary_stack.peek().max_length)

def begin_operation(operand_stack, dictionary_stack):
	dictionary_stack.push(operand_stack.pop())

def end_operation(operand_stack, dictionary_stack):
	dictionary_stack.pop()

def def_operation(operand_stack, dictionary_stack):
	if operand_stack.size() < 2:
		print("not enough operands.")
		return

	value = operand_stack.pop()
	name = operand_stack.pop()

	if isinstance(name, str) and name.startswith("/"):
		key = name[1:]
		dictionary_stack.peek()[key] = value
	else:
		operand_stack.push(name)
		operand_stack.push(value)
