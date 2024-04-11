# Installation

This documentation is for Linux-based platforms. You need to change `python3` to `python` on Windows.

## Install CM and Virtual Env

Check the CM installation guide for you platform and OS [here](https://access.cknowledge.org/playground/?action=install).


```bash
python3 -m pip install cmind virtualenv -U
```

## Create virtual env for ABTF and CM

```
python3 -m venv abtf

source abtf/bin/activate ; export CM_REPOS=$PWD/abtf/CM
```

## Get CM repository with automation recipes for MLOps


```bash
cm pull repo mlcommons@ck --checkout=dev
```

<details close>
<summary><b>Use compact version of this repository</b></summary>

Note that this repository grew over time to ~65MB with many commits. 
If you want to use a compact copy of this repository ~7MB, you can do it as follows:

```bash
cm rm repo mlcommons@ck --all
cm pull repo cknowledge@cm-mlops-copy
```

</details>

## Get CM repository with automation recipes for ABTF

```bash
cm pull repo cknowledge@cm4research
```

## Find paths to CM repositories on your platform

```bash
cm ls repo
```

## Update all CM repos at the same time

```bash
cm pull repo
```

## Run MLPerf loadgen test

```bash
cmr "test mlperf-loadgen python"
```
