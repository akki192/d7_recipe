print('Hello')

logging.config.dictConfig(yaml.load(open("logging.cfg"), Loader=yaml.FullLoader))
uri_hash = hashlib.md5(uri.encode()).hexdigest()
test.foo()
