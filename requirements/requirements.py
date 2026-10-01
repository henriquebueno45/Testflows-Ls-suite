# These requirements were auto generated
# from software requirements specification (SRS)
# document by TestFlows v2.0.250110.1002922.
# Do not edit by hand but re-generate instead
# using 'tfs requirements generate' command.
from testflows.core import Specification
from testflows.core import Requirement

Heading = Specification.Heading

RQ_SRS_099_Ls_command = Requirement(
    name='RQ.SRS-099.Ls.command',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] SHALL return all of the files and directories of the current directory\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.1'
)

RQ_SRS_099_Ls_command_flag_l = Requirement(
    name='RQ.SRS-099.Ls.command.flag.l',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **-l** SHALL return the total field with the number of 1024-byte blocks of data on the given directory\n'
        '\n'
        'For example:\n'
        '\n'
        '```bash\n'
        'ls -l\n'
        '```\n'
        '\n'
        'Outputs:\n'
        '\n'
        '```bash\n'
        'total 24232\n'
        '-rw-r--r-- 1 user 197609 23777028 Jan 15 20:38 Cosmere_RPG_Beta_Rules_Preview.pdf\n'
        'drwxr-xr-x 1 user 197609        0 Apr  9 07:46 images/\n'
        '-rw-r--r-- 1 user 197609      890 Apr  9 07:48 my_file.txt\n'
        '-rw-r--r-- 1 user 197609   305366 Apr  9 07:48 report.csv\n'
        '```\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.2'
)

RQ_SRS_099_Ls_command_flag_a = Requirement(
    name='RQ.SRS-099.Ls.command.flag.a',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **-a** SHALL return visible and hidden files in the listing. Hidden elements in Linux comprehend files and/or directories that start with a dot (e.g. .bashrc)\n'
        '\n'
        'For example:\n'
        '\n'
        '```bash\n'
        'ls -a\n'
        '```\n'
        '\n'
        'Outputs:\n'
        '\n'
        '```bash\n'
        'engines                        ontime_benchmark\n'
        '..                          example                        parquet\n'
        'aes_encryption              extended_precision_data_types  part_moves_between_shards\n'
        'aggregate_functions         functions                      rbac\n'
        'alter                       .git                           README.md\n'
        'altinity.png                .github                        regression.py\n'
        'atomic_insert               .gitignore \n'
        '```'
    ),
    link=None,
    level=2,
    num='3.3'
)

Software_Requirements_Specification = Specification(
    name='Software Requirements Specification',
    description=None,
    author=None,
    date=None,
    status=None,
    approved_by=None,
    approved_date=None,
    approved_version=None,
    version=None,
    group=None,
    type=None,
    link=None,
    uid=None,
    parent=None,
    children=None,
    headings=(
        Heading(name='SRS099 Ls parameters usage - Bash command', level=0, num=''),
        Heading(name='Introduction', level=1, num='1'),
        Heading(name='Related Resources', level=1, num='2'),
        Heading(name='Requirements ', level=1, num='3'),
        Heading(name='RQ.SRS-099.Ls.command', level=2, num='3.1'),
        Heading(name='RQ.SRS-099.Ls.command.flag.l', level=2, num='3.2'),
        Heading(name='RQ.SRS-099.Ls.command.flag.a', level=2, num='3.3'),
        ),
    requirements=(
        RQ_SRS_099_Ls_command,
        RQ_SRS_099_Ls_command_flag_l,
        RQ_SRS_099_Ls_command_flag_a,
        ),
    content=r'''
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
'''
)
