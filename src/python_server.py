from http.server import HTTPServer,  SimpleHTTPRequestHandler

def run(ADDRESS, PORT, server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
  ADDRESS=None
  PORT=None

  # server_address = A Tuple containing a string address, and a number port - address depends on type of server protocol
  server_address = (ADDRESS, int(PORT))

  # handler_class = a user provided request handler class, an instance of this class is created for every request
  # in this case, our handler_class is set to the SimpleHTTPRequestHandler provided by pthon
  # this handler serves files from a local directory. It can take a directory parameter that accepts a path-like object
  # it is a very Simple HTTP Req Handler compared to the Base Req Handler.
  # server_class() = HTTPServer, this is a socketserver.TCPServer SUBCLASS. It creates and listens to at the HTTP socket
  # it dispatches requests, to a request handler

  httpd = server_class(server_address, handler_class)

  print("launching server")

  # serve_forever() handle requests until an explicit shutdown() request. It is a continuous loop that
  # Polls for shutdown every poll_interval seconds. Ignores the timeout attribute.
  # it is a method inside our server class.
  httpd.serve_forever()

if __name__ ==  "__main__":
  # pass address and port as ENV variables from the global scope
  run()
