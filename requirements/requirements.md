# SRS099 Ls parameters usage - Bash command 
# Software Requirements Specification

# SRS099 Ls parameters usage - Bash command
# Software Requirements Specification

## Table of contents



## Introduction

This software requirements specification covers requirements related to Bash command [Ls] and all of its possible options. This document specifies which use and the expected output in a specific environment.

## Related Resources

**Linux manual page**
* https://man7.org/linux/man-pages/man1/ls.1.html

## Requirements 

### RQ.SRS-099.Ls.command
version: 1.0

[Ls command] SHALL return all of the files and directories of the current directory

### RQ.SRS-099.Ls.command.flag.l
version: 1.0

[Ls command] with the flag **-l** SHALL return the total field with the number of 1024-byte blocks of data on the given directory

For example:

```bash
ls -l
```

Outputs:

```bash
total 24232
-rw-r--r-- 1 user 197609 23777028 Jan 15 20:38 Cosmere_RPG_Beta_Rules_Preview.pdf
drwxr-xr-x 1 user 197609        0 Apr  9 07:46 images/
-rw-r--r-- 1 user 197609      890 Apr  9 07:48 my_file.txt
-rw-r--r-- 1 user 197609   305366 Apr  9 07:48 report.csv
```

### RQ.SRS-099.Ls.command.flag.a
version: 1.0

[Ls command] with the flag **-a** SHALL return visible and hidden files in the listing. Hidden elements in Linux comprehend files and/or directories that start with a dot (e.g. .bashrc)

For example:

```bash
ls -a
```

Outputs:

```bash
engines                        ontime_benchmark
..                          example                        parquet
aes_encryption              extended_precision_data_types  part_moves_between_shards
aggregate_functions         functions                      rbac
alter                       .git                           README.md
altinity.png                .github                        regression.py
atomic_insert               .gitignore 
```