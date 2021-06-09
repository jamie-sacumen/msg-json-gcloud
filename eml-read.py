import email
from email import policy
from email.parser import BytesParser
import glob
file_list = glob.glob('testmail.eml') # returns list of files
print(file_list)
with open(file_list[0], 'rb') as fp:  # select a specific email file from the list
        msg = BytesParser(policy=policy.default).parse(fp)
        text = msg.get_body(preferencelist=('plain')).get_content()
        print(text)
