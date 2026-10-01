# SRS099 Ls parameters usage - Bash command
# Software Requirements Specification

## Table of Contents

* 1 [Introduction](#introduction)
* 2 [Related Resources](#related-resources)
* 3 [Requirements](#requirements)
    * 3.1 [RQ.SRS-099.Ls.command](#rqsrs-099lscommand)
    * 3.2 [RQ.SRS-099.Ls.command.flag.l](#rqsrs-099lscommandflagl)
    * 3.3 [RQ.SRS-099.Ls.command.flag.a](#rqsrs-099lscommandflaga)
* 4 [References](#references)

## Introduction

This software requirements specification covers requirements related to Bash command [Ls] and all of its possible options. This document specifies which use and the expected output in a specific environment.

## Related Resources

**Linux manual page**
* https://man7.org/linux/man-pages/man1/ls.1.html

## Requirements

### RQ.SRS-099.Ls.command
version: 1.0

[Ls command] SHALL return all of the files and directories of the current directory and SHALL exit with code 0 on success

### RQ.SRS-099.Ls.command.flag.l
version: 1.0

[Ls command] with the flag **-l** SHALL return the long listing format and SHALL exit with code 0 on success.
The output SHALL include a `total` line with the number of 1024-byte blocks of data in the given directory,
followed by one line per file or directory containing the following information:

* File permissions
* Number of links
* Owner name
* Owner group
* File size
* Time of last modification
* File or directory name

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

[Ls command] with the flag **-a** SHALL return visible and hidden files in the listing and SHALL exit with code 0 on success.
Hidden elements in Linux comprehend files and/or directories that start with a dot (e.g. .bashrc)

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

## References

* [Linux manual page](https://man7.org/linux/man-pages/man1/ls.1.html)
