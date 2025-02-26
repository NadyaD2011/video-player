from livereload import Server, shell

server = Server()
server.watch('index.html')
server.serve(root='.')