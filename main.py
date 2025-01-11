from livereload import Server, shell

server = Server()
server.watch('index.html')
server.serve(root='.', default_filename='index.html')