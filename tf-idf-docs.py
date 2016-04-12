import pandas as pd
import numpy as np
import os
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer

fields = ['architecture','artist','socialmedia','teacher']
field = 'architecture'

directory = os.listdir('txt/' + field)
documents = []
def read_data(directory_name):
	file_names = os.listdir('txt/'+directory_name)
	corpus = []
	for file in file_names:
		try:
			with codecs.open('txt/' + directory_name + '/' + file, 'r', 'utf-8') as f:
				article = f.read()
				if article != "" and len(article) > 500:
					corpus.append(article)
		except (AttributeError, UnicodeDecodeError, ValueError):
			pass
		
	return corpus

def read_merge_data(directory_name):
	file_names = os.listdir('txt/'+directory_name)
	document = ""
	for file in file_names:
		try:
			with codecs.open('txt/' + directory_name + '/' + file, 'r', 'utf-8') as f:
				article = f.read()
				if article != "" and len(article) > 500:
					document += article
		except (AttributeError, UnicodeDecodeError, ValueError):
			pass
		
	return document

def map_score_phrase(tfidf_vec, score_indices):
	feature_names = tfidf_vec.get_feature_names()
	highest_scoring_features = []
	for index in score_indices:
		highest_scoring_features.append(feature_names[index])
	return highest_scoring_features

def get_highest_scoring_feature(array, feature_name, nth):
	results = []
	for ind in range(0, len(array)):
		highest_scores_indices = np.argpartition(array[ind], kth=nth)[nth:]
		scores = []
		names = []
		for index in highest_scores_indices:
			scores.append(array[ind][index])
			names.append(feature_names[index])
		results.append(zip(scores, names))
	return results
		
all_docs = []
for ff in fields:
	all_docs = all_docs + read_data(ff)

# print all_docs
print len(all_docs)

tfidf_vec = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df=1, stop_words='english')

try:
	results = tfidf_vec.fit_transform(all_docs)
	print results.get_shape()	
	result_as_array = results.toarray()
	feature_names = tfidf_vec.get_feature_names()
	print type(feature_names[0])

	total_highest_scores = get_highest_scoring_feature(result_as_array, feature_names, -100)
	map_doc_with_feature = []
	for doc_index in range(0, len(all_docs)):
		dict = {
			'Text': all_docs[doc_index].encode('utf-8'),
			'Keywords': total_highest_scores[doc_index]
		}
		map_doc_with_feature.append(dict)
	
	print map_doc_with_feature
	
	# print total_highest_scores	
	# print tfidf_vec.get_stop_words()
except ValueError:
	pass
