WSGIScriptAlias /plmu /usr/local/swp2/plusmuli.py
WSGIPythonPath /usr/local/swp2

<Directory "/usr/local/swp2">
	AllowOverride None
	Order deny,allow
	Require all granted
</Directory>
