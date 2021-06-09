from msg_parser import MsOxMessage
import datetime
import json
import eml_parser
output_eml_file_path="output"

msg_obj = MsOxMessage("sample.msg")
saved_path = msg_obj.save_email_file(output_eml_file_path)

def json_serial(obj):
  if isinstance(obj, datetime.datetime):
      serial = obj.isoformat()
      return serial


with open('./output/sample.eml', 'rb') as emlreader:
  raw_email = emlreader.read()

ep = eml_parser.EmlParser()
parsed_eml = ep.decode_email_bytes(raw_email)

json_serialize=json.dumps(parsed_eml, default=json_serial)
print(json_serialize)
with open( "datafile.json" , "w" ) as write:
    json.dump( json_serialize , write,indent=4 )
