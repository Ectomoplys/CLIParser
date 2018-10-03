from Command import Command
import sys
import inspect

commands = []

class CLIParser(object):
	def __init__(self):
		return

	def filename(self):
		frame = inspect.stack()[1]
		module = inspect.getmodule(frame[0])
		filename = module.__file__
		return filename

	def display_help(self):
		print('commands:')
		for command in commands:
				print('  {0}\t\t{1}'.format(command.command, command.desc))

	def add_command(self, command, desc = '', nargs = 1, action = ()):
			commands.append(Command(command, desc, nargs, action))

	def get_command(self, arg):
		for command in commands:
			if command.command == arg:
				return command
		return

	def parse_args(self):
		args = sys.argv
		comm_args = []

		if args[1] == '-h' or args[1] == '-help':
			self.display_help()
		else:
			index = 1

			while index < len(args):
				arg = args[index]

				if self.exists(arg):
					command = self.get_command(arg)

					for i in range(index + 1, index + command.nargs + 1):
						comm_args.append(args[i])

					print(comm_args)
					index += command.nargs + 1
					comm_args = []
				else:
					print('{0}: {1} is not a known command. Use -help for more info.'.format(self.filename(), arg))
					break


	def exists(self, comm):
		for command in commands:
			if comm == command.command:
				return True
			
		return False

def view():
	print('viewing')

def main():
	args = sys.argv
	
	parser = CLIParser()
	
	parser.add_command('-view', desc = 'View something', action = view)
	parser.add_command('-test', nargs = 3)
	parser.add_command('-add')
	parser.parse_args()
		
if __name__ == '__main__':
	main()
                                                                                 
