import subprocess

# print subprocess.call(["echo", "Hello World!"])
# print subprocess.check_output(["echo", "Hello World!"])
# print subprocess.check_call(["echo", "Hello World!"])
# print subprocess.call(["cd", "/", "|", "ls"])
# print subprocess.check_output(["ls"])
# print subprocess.check_call(["ls"])

def subprocess_cmd(command):
	process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	# proc_stdout = process.communicate()[0].strip() # understand this
	# print process
	# print process.communicate()
	# print process.communicate()[0]
	print process.communicate()[0]
	# print proc_stdout

# print subprocess.call(["cd", "/", ";", "ls"])

subprocess_cmd('cd /; ls')