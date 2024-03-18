# Steps to create a test environment
This article illustrates the basic requirements and steps to prepare a test environment to launch sandboxes.
Each boxes may have additional steps to get ready.

## Install Docker on your Mac PC
Download the installer of Docker Desktop and follow the instuction. "Use recommended settings" would be sufficient.
https://docs.docker.com/desktop/install/mac-install/

## Verify
Once it's installed, you can verify it. For example,

Docker version
```
% docker --version
Docker version 24.0.6, build ed223bc
```

Run a container
```
% docker run -d redis
Unable to find image 'redis:latest' locally
latest: Pulling from library/redis
2c6d21737d83: Pull complete 
...
Status: Downloaded newer image for redis:latest
9cc88f5b8f0ca5091b1148c518c60329ce7f42c74cfbfb0600e213520d3a85af
```

You can see a container running in Desktop app and/or `docker ps`
