
import os

mylist = ["0025","0026","0027","0028"]

for ribnum in mylist:
	print ribnum
	cmd1 = "python /data/array_tomography/ForSharmi/allen_SB_code/MakeAT/make_state_table_ext_multi.py --projectDirectory /nas2/data/M259292_Scnn1aTg2_1/  /nas/data/M259292_Scnn1aTg2_1/ --outputFile statetable --oneribbononly True --ribbon "+ribnum
	cmd2 = "python create_acquired_tilespecs.py"
	cmd3 = "python create_acquired_stacks.py"
	cmd4 = "python runmeqc.py"
	print cmd1
	os.system(cmd1)
	print cmd2
	#os.system(cmd2)
	print cmd3
	#os.system(cmd3)
	print cmd4
	os.system(cmd4)
	


