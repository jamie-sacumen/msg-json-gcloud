
from google.cloud import storage
import json
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gcloud.json"

def create_json():
    
    # json value
    
    f = open('datafile.json')
    data = json.load(f)
    f.close()
    return(data)
    
def json_upload_bucket(data):  
    # Get bucket name from environment variable in app.yaml file
    #bucket_name = os.environ.get('BUCKET_NAME')
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('textsmind.appspot.com')
    # declare your file name in GCP
    blob = bucket.blob('first_text.json')
    # upload json data were we will set content_type as json
    blob.upload_from_string(
        data=json.dumps(data),
        content_type='application/json'
        )
    return 'UPLOAD COMPLETE'

if __name__=="__main__":
   json_data=create_json()
   return_msg=json_upload_bucket(json_data)
   print(return_msg)