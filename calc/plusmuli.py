from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	first_number = d.get('first_number', [0])[0]
	second_number = d.get('second_number', [0])[0]
	try:
		first_number, second_number = int(first_number), int(second_number)
		sum=first_number+second_number			
		mul=first_number*second_number
	except ValueError:
		sum=-1
		mul=-1

	response_body = html % {
		'sum': sum,
		'mul': mul
	}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]


