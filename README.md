# Reproduce bug

generate image
```bash
docker build -t docker_test --no-cache .
```

start container
```bash
docker run --name docker_test -itd docker_test bash
```

check if the file exists (__init__.py)
```bash
docker exec docker_test ls /opt/docker_test
```

import code
```bash
docker exec docker_test python -c "import docker_test"
```

check if the file exists (__init__.py)
```bash
docker exec docker_test ls /opt/docker_test
```

restart container
```bash
docker stop docker_test
docker start docker_test
```

check if the file exists (__init__.py)
```bash
docker exec docker_test ls /opt/docker_test
```

reproduced in:
Docker version 19.03.1, build 74b1e89
Linux test 4.1.12-124.43.4.el7uek.x86_64 #2 SMP Tue Sep 22 12:01:13 PDT 2020 x86_64 x86_64 x86_64 GNU/Linux

```bash
[root@test ~]# docker run --name docker_test -itd docker_test bash
68c854ad3997ca4b32cd66c36292bc88217f6a114bb09edb8451cee45740e350
[root@test ~]# docker exec docker_test ls /opt/docker_test
__init__.py
[root@test ~]# docker exec docker_test python -c "import docker_test"
[root@test ~]# docker exec docker_test ls /opt/docker_test
__init__.py
__pycache__
[root@test ~]# docker stop docker_test
docker_test
[root@test ~]# docker start docker_test
docker_test
[root@test ~]# docker exec docker_test ls /opt/docker_test
__pycache__
```
