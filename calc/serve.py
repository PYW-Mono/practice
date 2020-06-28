WSGIScriptAlias /calc /home/pyw20203069/gitpractice/practice/calc/plusmuli.py
WSGIPythonPath /home/pyw20203069/gitpractice/practice/calc

<Directory "/home/pyw20203069/gitpractice/practice/calc">
	AllowOverride None
	Order deny,allow
	Require all granted
</Directory>
