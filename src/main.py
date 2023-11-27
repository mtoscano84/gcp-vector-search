import base64
import os
import functions_framework
import logging
from google.cloud import storage
import argparse
import gradio as gr

def do_load(params):
   logging.basicConfig(level=logging.INFO)
   input_file_path = params.input_file_path
   logging.info(f'input_file_path : {input_file_path}')
   return input_file_path

def upload_image_to_gcs(input_file_path):
    # Set environment variables for GCS bucket and blob name
    bucket_name = 'landing-image-repo'
    blob_name = 'blob_new_image'   
    
    # Create a StorageServiceClient object
    storage_client = storage.Client()

    # Get or create the destination bucket
    destination_bucket = storage_client.bucket(bucket_name)
#    destination_bucket.create_if_not_exists()
    blob = destination_bucket.blob(blob_name)

    # Abort if the image already exists in the bucket
    generation_match_precondition = 0

    blob.upload_from_filename(input_file_path, if_generation_match=generation_match_precondition)

    print(
        f"File {input_file_path} uploaded to {bucket_name}."
    )

def process_file(fileobj): 
    file_path = fileobj.name
    upload_image(file_path)
    return

demo = gr.Interface(
    fn=process_file,
    inputs=[
        "file",
    ],
    outputs="text"
)

if __name__ == '__main__':
#    parser = argparse.ArgumentParser(description='Loader image to GCS')
#    parser.add_argument('--input_file_path', type=str)
#    params = parser.parse_args()
#    input_file_path = do_load(params)
#    upload_image_to_gcs(input_file_path)
    demo.launch()