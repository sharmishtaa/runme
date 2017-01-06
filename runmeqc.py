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


    print "NOW IN MAIN FILE!!!!!!!!!!!!!!!!!!"

    try :
	file = open("TESTFILE.txt",'w+')
	file.close()
    except:
	print "Something is wrong!"
	sys.exit(0) 

    time.sleep(2)

    #1. Create Statetable
    sttablecmd = "python /data/array_tomography/ForSharmi/allen_SB_code/MakeAT/make_state_table.py --inputDirectory "
    sttablecmd = sttablecmd + os.getcwd() + "/../raw/data/ --outputFile statetable"
    print sttablecmd
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    #os.system(sttablecmd)

    time.sleep(20)

    #2. 2D alignment and stitching

    df =pd.read_csv("statetable")

    uniq_channel_sessions = df.groupby(['ribbon','session','ch']).groups.keys()
    R = []
    C = []
    S = []
    for (rib,sess,chan) in uniq_channel_sessions:	
	R.append(rib)
	C.append(chan)
	S.append(sess)

    for x in range (0,20):
	print x
    	for index in range (0,len(R)):
    		cmd = "PYTHONPATH='' luigi stitch_ribbon_session_channel --module stitch_ribbon --workers 4 "
		cmd = cmd + " --ribbon " + str(R[index])
		cmd = cmd + " --channel " + str(C[index])
		cmd = cmd + " --session " + str(S[index])
		print cmd
    		result = run_celerycommand.apply_async(args=[cmd,os.getcwd()])	
	
	time.sleep(1800)
	
    #3. 3D alignment

    #runalignmentqc()

    #run_alignment_setup()


    #for x in range(0,3):
    #	cmd = "PYTHONPATH='' luigi align3d --module align3d  --workers 4"
    #	print cmd
    #	result = run_celerycommand.apply_async(args=[cmd,os.getcwd()])		
    #	time.sleep(3600)
    

