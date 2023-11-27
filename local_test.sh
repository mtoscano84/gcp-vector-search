python3 -m venv local_test_env
source local_test_env/bin/activate
pip3 install -r src/requirements.txt
#python3 src/main.py --emb_data_path data/images.json --alloydb_uri projects/mtoscano-demo-01/locations/us-central1/clusters/alloydb-cluster01/instances/alloydb-inst01 --alloydb_user image_store --alloydb_passwd Image_001 --alloydb_db_name image_store
python3 src/main.py --input_file_path data/3918601717_6_1_1.jpg
