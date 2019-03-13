# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
# storage_client = storage.Client()

# The name for the new bucket
bucket_name = 'kokodayo-test-box'

# # Creates the new bucket
# bucket = storage_client.create_bucket(bucket_name)
#
# print('Bucket {} created.'.format(bucket.name))


destination_blob_name = "README.md"
source_file_name = "./README.md"
storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(destination_blob_name)

blob.upload_from_filename(source_file_name)

print('File {} uploaded to {}.'.format(
    source_file_name,
    destination_blob_name))
