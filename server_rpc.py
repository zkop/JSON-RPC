from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher
import json

from pke.unsupervised import TopicRank

@dispatcher.add_method
def get_terms(row_data):
	clusters = []
	for key, val in row_data.items():
		extractor = TopicRank()
		text = ". ".join(val)		 		
		extractor.load_document(input= text)
		try:
			extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ'})
			extractor.candidate_weighting(threshold=0.74, method='average')
			top_words = []
			for (key_phrases, score) in extractor.get_n_best(n=10):
				#if len(key_phrases.split(" ")) <= 2:
				top_words.append(key_phrases)
				#if len(top_words) == 10: break
			clusters.append(
				{
					"size": len(val),
					"topWords": top_words
				}
			)
		except:
			clusters.append(
				{
					"size": len(val),
					"topWords": []
				}
			)

	return clusters


@Request.application
def application(request):
	response = JSONRPCResponseManager.handle(request.data, dispatcher)
	return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
	run_simple('localhost', 4000, application)