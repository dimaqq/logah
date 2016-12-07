# logah
Docker log aggregator

Start the aggregator
```
docker-compose -f docker-compose.yml run --rm async
```

Start a test container in another terminal
```
docker run -it --rm python bash
```

You should see (in first terminal):
```
detected container 12a270051ef0e11ca59de4a3213a6c490c911fadf4f736062b861381909cd916
log line b'root@12a270051ef0:/# '
log line b'\x1b[Kroot@12a270051ef0:/# ls -l'
log line b'total 64'
log line b'drwxr-xr-x   2 root root 4096 Nov  7 22:28 bin'
log line b'drwxr-xr-x   2 root root 4096 Sep 12 04:09 boot'
log line b'drwxr-xr-x   5 root root  380 Nov 24 20:15 dev'
```
