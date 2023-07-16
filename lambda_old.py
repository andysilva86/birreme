import json
import os

def lambda_handler(event, context):
	arquivo_html_nome = "Arsha/index.html" 
	html_index = open(arquivo_html_nome, 'r', encoding='utf-8')
	body = html_index.read()

	response = {
		'statusCode': 200,
		"headers": {'Content-Type':'text/html',},
		'body': body
	}

	return response