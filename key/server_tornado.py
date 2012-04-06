import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
		self.write('data = { "category": "Advertising"}')
		#print "key : "+self.get_argument("key")
		whatever(self.get_argument("key"))


application = tornado.web.Application([
    (r"/", MainHandler),
	])

def whatever(self):
	print "whatever "+self


if __name__ == "__main__":
	application.listen(8082)
	tornado.ioloop.PeriodicCallback(whatever, 1)
	tornado.ioloop.IOLoop.instance().start()