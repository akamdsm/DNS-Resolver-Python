import socket, sys

host = sys.argv[1]
print("[+] {} --> {}".format(host, socket.gethostbyname(host)))
