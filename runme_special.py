import luigi
from stitching import stitch_section
from runluigi import runluigi
import time
import os
import sys
sys.path.insert(0,'/data/array_tomography/ForSharmi/allen_SB_code/celery/')
sys.path.insert(0,os.getcwd())
from celery import Celery
from tasks import run_celerycommand
from runalignmentqc import runalignmentqc
import pandas as pd
from run_alignment_setup import run_alignment_setup

if __name__ == '__main__':

    minribbon = 3
    maxribbon = 3
    curribbon = 3

    while (curribbon >= minribbon) & (curribbon <= maxribbon) :
	
    	try :
		file = open("TESTFILE.txt",'w+')
		file.close()
    	except:
		print "Something is wrong with permissions!"
		sys.exit(0) 

        time.sleep(2)

    	#1. Create Statetable
        if curribbon < 10:
		ribnum = "000"+str(curribbon)
	if (curribbon >= 10) & (curribbon < 100) :
		ribnum = "00"+str(curribbon)
	if (curribbon >= 100) :
		ribnum = "0"+str(curribbon)	
	statetablefile = "statetable_"+ribnum		
    	cmd1 = "python /data/array_tomography/ForSharmi/allen_SB_code/MakeAT/make_state_table_ext_multi.py --projectDirectory /nas2/data/M259292_Scnn1aTg2_1/  /nas/data/M259292_Scnn1aTg2_1/ --outputFile " + statetablefile + " --oneribbononly True --ribbon "+ribnum
    	#os.system(cmd1)

        time.sleep(2)

 	#2. Create flatfield tilespecs
	cmd2 = "python create_ff_tilespecs.py --rootdir /nas2/data/M259292_Scnn1aTg2_1 --statetablefile "+statetablefile
	#os.system(cmd2)

	#3. 2D alignment and stitching

    	df =pd.read_csv(statetablefile)

    	uniq_channel_sessions = df.groupby(['ribbon','session','ch','section']).groups.keys()
    	R = []
	C = []
    	S = []
	T = []
    	for (rib,sess,chan,sect) in uniq_channel_sessions:
			R.append(rib)
			C.append(chan)
			S.append(sess)
	    		T.append(sect)

    	for x in range (0,2):
		print x
    		for index in range (0,len(R)):
    			#cmd = "PYTHONPATH='' luigi stitch_ribbon_session_channel --module stitch_ribbon --workers 4 --statetablefile "+statetablefile
				cmd = "PYTHONPATH='' luigi stitch_section --module stitching --workers 4 "
				cmd = cmd + " --ribbon " + str(R[index])
				cmd = cmd + " --channel " + str(C[index])
				cmd = cmd + " --session " + str(S[index])
				cmd = cmd + " --section " + str(T[index])
				print cmd
    				result = run_celerycommand.apply_async(args=[cmd,os.getcwd()])	
	
		time.sleep(300)
	
	curribbon = curribbon + 1
