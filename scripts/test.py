import os

prog_name = os.path.basename(__file__)
home_dir = os.path.expanduser("~")
print('{0}: {1}'.format(prog_name, home_dir))
