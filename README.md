# aitlas-docker
Dockerising Aitlas tool


### Prerequisities

* Linux OS (Development and Testing done on Ubuntu 20.04)

In order to run this container you'll need docker installed.

* [Linux](https://docs.docker.com/linux/started/)

(Optional) Requirement for Nvidia GPU Passthrough

* [CUDA Capable Nvidia Graphics Card] (https://developer.nvidia.com/cuda-gpus)

* [CUDA Driver 465+] (https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#driver-installation)

### Usage

## Getting Started

docker pull alexhayhoe/aitlas

These instructions will cover usage information and for the docker container

#### Container Parameters

How to get a shell started in your container

```shell
docker run -it --name aitlas1;
-v <local directory path>:/mnt/<0-9>/<internal directory path>;
--shm-size=<>M --gpus all;
alexhayhoe/aitlas /bin/bash
```

#### Environment Variables

* `gpus` - Determines which gpus are connected if multiple capable GPUS are discovered.
* `shm-size` - Determines the memory allocation (RAM) that is given to the container from the host OS.
* `/bin/bash` - Creates a bash terminal and shells into the container when it starts.



## Built With

* nvidia/cuda
* https://gitlab.com/nvidia/container-images/cuda/blob/master/dist/11.2.0/ubuntu20.04-x86_64/devel/cudnn8/Dockerfile

## Find Us

* [GitHub](https://github.com/alex-hayhoe/aitlas-docker/)
* [Docker Hub](https://hub.docker.com/repository/docker/alexhayhoe/aitlas)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the
[tags on this repository](https://github.com/your/repository/tags).

## Authors

* - *Initial work* - [The AiTLAS toolbox (Artificial Intelligence Toolbox for Earth Observation)](https://github.com/biasvariancelabs/aitlas)
* - *Containerisation* -  **Alex Hayhoe**

See also the list of [contributors](https://github.com/your/repository/contributors) who
participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* The AiTLAS toolbox (Artificial Intelligence Toolbox for Earth Observation)
* https://github.com/biasvariancelabs/aitlas
