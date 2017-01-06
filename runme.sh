#ALTERNATE MICRSCOPE FOR MEDIAN

#this can be done before raw data is fully collected 
#python runme_stitching.py

#create ff raw specs from full statetable
#do this only after all the raw data has been collected
#python /data/array_tomography/ForSharmi/allen_SB_code/MakeAT/make_state_table_ext_multi.py 
#--projectDirectory /nas2/data/M259292_Scnn1aTg2_1/  /nas/data/M259292_Scnn1aTg2_1/ --outputFile statetable
#python create_ff_tilespecs.py --rootdir /nas3/data/M270907_Scnn --statetablefile statetable


#python create_stitched_fullstack.py --firstStatetableNum 0 --lastStatetableNum 123 --outputStack STITCHEDSTACK_DAPI_1 --rootDir /nas3/data/M270907_Scnn1aTg2Tdt_13 --updateZval 
#python remove_outer_tiles.py --Project M270907_Scnn1aTg2Tdt_13 --inputStack STITCHEDSTACKFINAL_DAPI_1_DAPI_1 --jsonDirectory /nas3/data/M270907_Scnn1aTg2Tdt_13/processed/stitched_tilespec_ff_corrected --outputStack STITCHEDSTACKFINAL_CORRECTED_DAPI_1_DAPI_1

#python create_xml_from_tilespecs.py --inputStack STITCHEDSTACKFINAL_DAPI_1_DAPI_1 --outputDirectory ../processed/chunks30_DEC14 --sectionsPerChunk 30 --firstSection 0 --lastSection 3259

#GO STOP CELERY SCRIPTS AND RESTART WITH ONE WORKER
#ps aux | grep celery | awk '{print $2}' | xargs kill -9
#celery worker -A tasks --concurrency 1 &


#python alignme.py --chunkDirectory ../processed/chunks --outputDirectory ../processed/aligned100

#python dechunk_me.py --alignedDirectory ../processed/aligned100/ --firstSection 0 --sectionsPerChunk 100 --overlap 50 --lastSection 1215
#python dechunk_me.py --alignedDirectory ../processed/alignmenttest_dec14/ --firstSection 0 --lastSection 3259 --sectionsPerChunk 100 --overlap 50
#python dechunk_me.py --alignedDirectory ../processed/alignmenttest_dec14/ --firstSection 0 --lastSection 3260 --sectionsPerChunk 100 --overlap 50

#upload to render stack
#python checkmergedchunks.py --chunkDirectory ../processed/aligned100 --outputStack ALIGNEDSTACK_DAPI_1 --firstSection 0 --lastSection 1215 --sectionsPerChunk 100



#if all machines die and need to be restarted:


#On ibs-sharmi-ux1, from anywhere:
#sudo rabbitmq-server -detached
#luigid
#

#On ibs-forrestc-ux1:
#in /pipeline/render, do : ./deploy/jetty_base/jetty_wrapper.sh start
#sudo docker run -d -p 8000:8000 ndviz:render

#On all machines, go to /data/array_tomography/ForSharmi/allencode/celery and run: celery worker -A tasks --concurrency 10 &
