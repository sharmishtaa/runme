import os

for i in range(100,124):
	cmd = "python create_fast_stacks.py --statetable statetable_0"+str(i)
	os.system(cmd)

