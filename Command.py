class Command(object):
	def __init__(self, command, desc, nargs, action):
		self.command = command
		self.desc = desc
		self.nargs = nargs
		self.action = action
