import boto3

client = boto3.client(
	'dynamodb',
	aws_access_key_id="AKIAJFEHWFDAGPYSMRQQ",
	aws_secret_access_key="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",
	region="ap-northeast-1"
)

fields = ['architecture','artist','socialmedia','teacher']
field = 'architecture'

directory = os.listdir('txt/' + field)
documents = []
dataId = 0
def read_data(directory_name):
	file_names = os.listdir('txt/'+directory_name)
	corpus = []
	for file in file_names:
		try:
			with codecs.open('txt/' + directory_name + '/' + file, 'r', 'utf-8') as f:
				article = f.read()
				if article != "" and len(article) > 500:
					client.put_item(
						TableName="DataScience",
						Item={
							'string':{
								'Field':directory_name,
								'Text':article
							}
						}
					)
					dataId += 1
		except (AttributeError, UnicodeDecodeError, ValueError):
			pass
		
	return corpus


all_docs = []
for ff in fields:
	all_docs = all_docs + read_data(ff)