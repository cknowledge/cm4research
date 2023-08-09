# Reproducibility report automated by CM

We successfully ran [Refiners "Hello World" example](https://github.com/finegrain-ai/refiners#getting-started) with the following settings:

* OS: Ubuntu 22.04.2 LTS
* Python: 3.10.12
* CUDA 11.5.0 and 11.8.0
* PyTorch CUDA 2.0.0 and 2.0.1
* Refiners from PYPI: 0.1.0
* GPU: Nvidia T4
* CPU: AWS 4-core x64

Disk space required: ~15GB

Steps to reproduce:

Install [CM automation language](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull main repository with CM automation recipes for AI/ML systems:
```bash
cm pull repo mlcommons@ck
```

Pull this repository with reproducibility reports automated by CM:
```bash
cm pull repo cknowledge@cm-reproduce
```

Install Python virtual env via CM:
```bash
cmr "install python-venv" --name=refiners --version_min=3.10.1
```

Get CUDA 11.8.0 via CM:
```bash
cmr "get cuda" --version=11.8.0
```

Get PyTorch CUDA 2.0.1:
```bash
cmr "get generic-python-lib _torch_cuda" --version=2.0.1 --adr.python.name=refiners
```

Get Diffusers Python library 0.18.2 (0.19+ currently doesn't work and being fixed):
```bash
cmr "get generic-python-lib _package.diffusers" --version=0.18.2 --adr.python.name=refiners
```

Get Refiners Python library 0.1.0:
```bash
cmr "get generic-python-lib _package.refiners" --version=0.1.0 --adr.python.name=refiners
```


Run refiner's "Hello World" example:
```bash
cmr "run python-app refiners hello-world _cuda" --adr.python.name=refiners
```

You should see pokemon_cat.png in your current directory.

You can regenerate image for your prompt as following:
```bash
cmr "run python-app refiners hello-world _cuda" --adr.python.name=refiners --skip_convert --output=new.png --prompt="guardians of the galaxy"
```
