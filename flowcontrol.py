mappings = [
	["if", lambda x, y: if_operation(x, y)],
	["ifelse", lambda x, y: ifelse_operation(x, y)],
	["for", lambda x, y: repeat_operation(x, y)],
	["repeat", lambda x, y: repeat_operation(x, y)],
]

def if_operation(stack, parser):
	if stack.size() < 2:
		print("not enough operands.")
		return
	
	if not isinstance(stack.peek(), list):
		print("must be a codeblock.")
		return

	proc = stack.pop()
	truth = stack.pop()

	if truth:
		for item in proc:
			parser(item)

def ifelse_operation(stack, parser):
	if stack.size() < 2:
		print("not enough operands.")
		return
	
	if not isinstance(stack.peek(), list):
		print("must be a codeblock.")
		return

	proc1 = stack.pop()

	if not isinstance(stack.peek(), list):
		print("must be a codeblock.")
		stack.push(proc1)
		return

	proc2 = stack.pop()
	truth = stack.pop()

	if truth:
		for item in proc2:
			parser(item)
	else:
		for item in proc1:
			parser(item)

def for_operation(stack, parser):
	if stack.size() < 4:
		print("not enough operands.")
		return

	proc = stack.pop()
	l = stack.pop()
	k = stack.pop()
	j = stack.pop()

	i = j
	while i < l:
		for item in proc:
			parser(item)
		i += k

def repeat_operation(stack, parser):
	if stack.size() < 2:
		print("not enough operands.")
		return

	if not isinstance(stack.peek(), list):
		print("must be a codeblock.")
		return

	proc = stack.pop()
	count = stack.pop()

	for i in range(count):
		for item in proc:
			parser(item)	
