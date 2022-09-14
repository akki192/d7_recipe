print('Hello')

logging.config.dictConfig(yaml.load(open("logging.cfg"), Loader=yaml.FullLoader))
test.foo()
