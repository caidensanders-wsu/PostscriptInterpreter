class LimitedDict:
	def __init__(self, max_length):
		self.max_length = max_length
		self.dict = {}

	def __setitem__(self, key, value):
		if len(self.dict) < self.max_length:
			self.dict[key] = value
		else:
			raise ValueError("Dictionary is full.")

	def __getitem__(self, key):
		return self.dict[key]

	def __iter__(self):
		return iter(self.dict)
	
	def __len__(self):
		return len(self.dict)
