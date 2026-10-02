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
        '[Ls command] SHALL list the files and directories contained in the current directory and SHALL exit with code 0 on success.\n'
        '\n'
        'For example, given a directory containing a file `my_file.txt` and a directory `images`:\n'
        '\n'
        '```bash\n'
        'ls\n'
        '```\n'
        '\n'
        'Outputs:\n'
        '\n'
        '```bash\n'
        'images  my_file.txt\n'
        '```\n'
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
        '[Ls command] with the flag **-l** SHALL return the long listing format and SHALL exit with code 0 on success.\n'
        'The output SHALL include a `total` line with the number of 1024-byte blocks of data in the given directory,\n'
        'followed by one line per file or directory containing the following information:\n'
        '\n'
        '* File permissions\n'
        '* Number of links\n'
        '* Owner name\n'
        '* Owner group\n'
        '* File size\n'
        '* Time of last modification\n'
        '* File or directory name\n'
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

RQ_SRS_099_Ls_command_default_ignoresDotEntries = Requirement(
    name='RQ.SRS-099.Ls.command.default.ignoresDotEntries',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command], when invoked without the **-a** or **--all** flag, SHALL ignore entries whose name starts with a dot (`.`),\n'
        'including the implied `.` and `..` entries, and SHALL exit with code 0 on success.\n'
        '\n'
        'For example, given a directory containing a visible file `my_file.txt`, a visible directory `images`, a hidden file `.bashrc`, and a hidden directory `.config`:\n'
        '\n'
        '```bash\n'
        'ls\n'
        '```\n'
        '\n'
        'Outputs:\n'
        '\n'
        '```bash\n'
        'images  my_file.txt\n'
        '```\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.3'
)

RQ_SRS_099_Ls_command_flag_a = Requirement(
    name='RQ.SRS-099.Ls.command.flag.a',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **-a** SHALL NOT ignore entries whose name starts with a dot (`.`) and SHALL exit with code 0 on success.\n'
        '\n'
        'For example, given the same directory as above:\n'
        '\n'
        '```bash\n'
        'ls -a\n'
        '```\n'
        '\n'
        'Outputs:\n'
        '\n'
        '```bash\n'
        '.  ..  .bashrc  .config  images  my_file.txt\n'
        '```\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.4'
)

RQ_SRS_099_Ls_command_flag_a_includesCurrentDirectoryEntry = Requirement(
    name='RQ.SRS-099.Ls.command.flag.a.includesCurrentDirectoryEntry',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **-a** SHALL include the `.` entry, representing the current directory, in the listing.\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.5'
)

RQ_SRS_099_Ls_command_flag_a_includesParentDirectoryEntry = Requirement(
    name='RQ.SRS-099.Ls.command.flag.a.includesParentDirectoryEntry',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **-a** SHALL include the `..` entry, representing the parent directory, in the listing.\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.6'
)

RQ_SRS_099_Ls_command_flag_a_includesEntriesWithMultipleLeadingDots = Requirement(
    name='RQ.SRS-099.Ls.command.flag.a.includesEntriesWithMultipleLeadingDots',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **-a** SHALL list entries whose name starts with more than one leading dot (e.g. `..config`).\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.7'
)

RQ_SRS_099_Ls_command_flag_a_includesHiddenDirectories = Requirement(
    name='RQ.SRS-099.Ls.command.flag.a.includesHiddenDirectories',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **-a** SHALL list directories whose name starts with a dot (`.`), not only hidden files.\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.8'
)

RQ_SRS_099_Ls_command_flag_a_preservesNonHiddenEntries = Requirement(
    name='RQ.SRS-099.Ls.command.flag.a.preservesNonHiddenEntries',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **-a** SHALL still list entries that do not start with a dot, alongside the entries that start with a dot.\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.9'
)

RQ_SRS_099_Ls_command_flag_a_emptyDirectory = Requirement(
    name='RQ.SRS-099.Ls.command.flag.a.emptyDirectory',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **-a** on an empty directory SHALL list only the `.` and `..` entries and SHALL exit with code 0 on success.\n'
        '\n'
        'For example, given an empty directory:\n'
        '\n'
        '```bash\n'
        'ls -a\n'
        '```\n'
        '\n'
        'Outputs:\n'
        '\n'
        '```bash\n'
        '.  ..\n'
        '```\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.10'
)

RQ_SRS_099_Ls_command_flag_all = Requirement(
    name='RQ.SRS-099.Ls.command.flag.all',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **--all** SHALL NOT ignore entries whose name starts with a dot (`.`) and SHALL exit with code 0 on success.\n'
        '\n'
        'For example, given the same directory as above:\n'
        '\n'
        '```bash\n'
        'ls --all\n'
        '```\n'
        '\n'
        'Outputs:\n'
        '\n'
        '```bash\n'
        '.  ..  .bashrc  .config  images  my_file.txt\n'
        '```\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.11'
)

RQ_SRS_099_Ls_command_flag_all_includesCurrentDirectoryEntry = Requirement(
    name='RQ.SRS-099.Ls.command.flag.all.includesCurrentDirectoryEntry',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **--all** SHALL include the `.` entry, representing the current directory, in the listing.\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.12'
)

RQ_SRS_099_Ls_command_flag_all_includesParentDirectoryEntry = Requirement(
    name='RQ.SRS-099.Ls.command.flag.all.includesParentDirectoryEntry',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **--all** SHALL include the `..` entry, representing the parent directory, in the listing.\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.13'
)

RQ_SRS_099_Ls_command_flag_all_includesEntriesWithMultipleLeadingDots = Requirement(
    name='RQ.SRS-099.Ls.command.flag.all.includesEntriesWithMultipleLeadingDots',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **--all** SHALL list entries whose name starts with more than one leading dot (e.g. `..config`).\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.14'
)

RQ_SRS_099_Ls_command_flag_all_includesHiddenDirectories = Requirement(
    name='RQ.SRS-099.Ls.command.flag.all.includesHiddenDirectories',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **--all** SHALL list directories whose name starts with a dot (`.`), not only hidden files.\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.15'
)

RQ_SRS_099_Ls_command_flag_all_preservesNonHiddenEntries = Requirement(
    name='RQ.SRS-099.Ls.command.flag.all.preservesNonHiddenEntries',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **--all** SHALL still list entries whose name does not start with a dot, together with the entries whose name does.\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.16'
)

RQ_SRS_099_Ls_command_flag_all_emptyDirectory = Requirement(
    name='RQ.SRS-099.Ls.command.flag.all.emptyDirectory',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **--all** on an empty directory SHALL list only the `.` and `..` entries and SHALL exit with code 0 on success.\n'
        '\n'
        'For example, given an empty directory:\n'
        '\n'
        '```bash\n'
        'ls --all\n'
        '```\n'
        '\n'
        'Outputs:\n'
        '\n'
        '```bash\n'
        '.  ..\n'
        '```\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.17'
)

RQ_SRS_099_Ls_command_flag_all_equivalentToFlagA = Requirement(
    name='RQ.SRS-099.Ls.command.flag.all.equivalentToFlagA',
    version='1.0',
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[Ls command] with the flag **--all** SHALL produce output identical to [Ls command] with the flag **-a**, since **--all** is the long-form name of the same option.\n'
        '\n'
    ),
    link=None,
    level=2,
    num='3.18'
)

SRS099_Ls_parameters_usage_Bash_command = Specification(
    name='SRS099 Ls parameters usage - Bash command',
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
        Heading(name='Introduction', level=1, num='1'),
        Heading(name='Related Resources', level=1, num='2'),
        Heading(name='Requirements', level=1, num='3'),
        Heading(name='RQ.SRS-099.Ls.command', level=2, num='3.1'),
        Heading(name='RQ.SRS-099.Ls.command.flag.l', level=2, num='3.2'),
        Heading(name='RQ.SRS-099.Ls.command.default.ignoresDotEntries', level=2, num='3.3'),
        Heading(name='RQ.SRS-099.Ls.command.flag.a', level=2, num='3.4'),
        Heading(name='RQ.SRS-099.Ls.command.flag.a.includesCurrentDirectoryEntry', level=2, num='3.5'),
        Heading(name='RQ.SRS-099.Ls.command.flag.a.includesParentDirectoryEntry', level=2, num='3.6'),
        Heading(name='RQ.SRS-099.Ls.command.flag.a.includesEntriesWithMultipleLeadingDots', level=2, num='3.7'),
        Heading(name='RQ.SRS-099.Ls.command.flag.a.includesHiddenDirectories', level=2, num='3.8'),
        Heading(name='RQ.SRS-099.Ls.command.flag.a.preservesNonHiddenEntries', level=2, num='3.9'),
        Heading(name='RQ.SRS-099.Ls.command.flag.a.emptyDirectory', level=2, num='3.10'),
        Heading(name='RQ.SRS-099.Ls.command.flag.all', level=2, num='3.11'),
        Heading(name='RQ.SRS-099.Ls.command.flag.all.includesCurrentDirectoryEntry', level=2, num='3.12'),
        Heading(name='RQ.SRS-099.Ls.command.flag.all.includesParentDirectoryEntry', level=2, num='3.13'),
        Heading(name='RQ.SRS-099.Ls.command.flag.all.includesEntriesWithMultipleLeadingDots', level=2, num='3.14'),
        Heading(name='RQ.SRS-099.Ls.command.flag.all.includesHiddenDirectories', level=2, num='3.15'),
        Heading(name='RQ.SRS-099.Ls.command.flag.all.preservesNonHiddenEntries', level=2, num='3.16'),
        Heading(name='RQ.SRS-099.Ls.command.flag.all.emptyDirectory', level=2, num='3.17'),
        Heading(name='RQ.SRS-099.Ls.command.flag.all.equivalentToFlagA', level=2, num='3.18'),
        Heading(name='References', level=1, num='4'),
        ),
    requirements=(
        RQ_SRS_099_Ls_command,
        RQ_SRS_099_Ls_command_flag_l,
        RQ_SRS_099_Ls_command_default_ignoresDotEntries,
        RQ_SRS_099_Ls_command_flag_a,
        RQ_SRS_099_Ls_command_flag_a_includesCurrentDirectoryEntry,
        RQ_SRS_099_Ls_command_flag_a_includesParentDirectoryEntry,
        RQ_SRS_099_Ls_command_flag_a_includesEntriesWithMultipleLeadingDots,
        RQ_SRS_099_Ls_command_flag_a_includesHiddenDirectories,
        RQ_SRS_099_Ls_command_flag_a_preservesNonHiddenEntries,
        RQ_SRS_099_Ls_command_flag_a_emptyDirectory,
        RQ_SRS_099_Ls_command_flag_all,
        RQ_SRS_099_Ls_command_flag_all_includesCurrentDirectoryEntry,
        RQ_SRS_099_Ls_command_flag_all_includesParentDirectoryEntry,
        RQ_SRS_099_Ls_command_flag_all_includesEntriesWithMultipleLeadingDots,
        RQ_SRS_099_Ls_command_flag_all_includesHiddenDirectories,
        RQ_SRS_099_Ls_command_flag_all_preservesNonHiddenEntries,
        RQ_SRS_099_Ls_command_flag_all_emptyDirectory,
        RQ_SRS_099_Ls_command_flag_all_equivalentToFlagA,
        ),
    content=r'''
# SRS099 Ls parameters usage - Bash command
# Software Requirements Specification

## Table of Contents

* 1 [Introduction](#introduction)
* 2 [Related Resources](#related-resources)
* 3 [Requirements](#requirements)
    * 3.1 [RQ.SRS-099.Ls.command](#rqsrs-099lscommand)
    * 3.2 [RQ.SRS-099.Ls.command.flag.l](#rqsrs-099lscommandflagl)
    * 3.3 [RQ.SRS-099.Ls.command.default.ignoresDotEntries](#rqsrs-099lscommanddefaultignoresdotentries)
    * 3.4 [RQ.SRS-099.Ls.command.flag.a](#rqsrs-099lscommandflaga)
    * 3.5 [RQ.SRS-099.Ls.command.flag.a.includesCurrentDirectoryEntry](#rqsrs-099lscommandflagaincludescurrentdirectoryentry)
    * 3.6 [RQ.SRS-099.Ls.command.flag.a.includesParentDirectoryEntry](#rqsrs-099lscommandflagaincludesparentdirectoryentry)
    * 3.7 [RQ.SRS-099.Ls.command.flag.a.includesEntriesWithMultipleLeadingDots](#rqsrs-099lscommandflagaincludesentrieswithmultipleleadingdots)
    * 3.8 [RQ.SRS-099.Ls.command.flag.a.includesHiddenDirectories](#rqsrs-099lscommandflagaincludeshiddendirectories)
    * 3.9 [RQ.SRS-099.Ls.command.flag.a.preservesNonHiddenEntries](#rqsrs-099lscommandflagapreservesnonhiddenentries)
    * 3.10 [RQ.SRS-099.Ls.command.flag.a.emptyDirectory](#rqsrs-099lscommandflagaemptydirectory)
    * 3.11 [RQ.SRS-099.Ls.command.flag.all](#rqsrs-099lscommandflagall)
    * 3.12 [RQ.SRS-099.Ls.command.flag.all.includesCurrentDirectoryEntry](#rqsrs-099lscommandflagallincludescurrentdirectoryentry)
    * 3.13 [RQ.SRS-099.Ls.command.flag.all.includesParentDirectoryEntry](#rqsrs-099lscommandflagallincludesparentdirectoryentry)
    * 3.14 [RQ.SRS-099.Ls.command.flag.all.includesEntriesWithMultipleLeadingDots](#rqsrs-099lscommandflagallincludesentrieswithmultipleleadingdots)
    * 3.15 [RQ.SRS-099.Ls.command.flag.all.includesHiddenDirectories](#rqsrs-099lscommandflagallincludeshiddendirectories)
    * 3.16 [RQ.SRS-099.Ls.command.flag.all.preservesNonHiddenEntries](#rqsrs-099lscommandflagallpreservesnonhiddenentries)
    * 3.17 [RQ.SRS-099.Ls.command.flag.all.emptyDirectory](#rqsrs-099lscommandflagallemptydirectory)
    * 3.18 [RQ.SRS-099.Ls.command.flag.all.equivalentToFlagA](#rqsrs-099lscommandflagallequivalenttoflaga)
* 4 [References](#references)

## Introduction

The following requirements specification covers requirements related to the behavior of the Bash [Ls command] when invoked without options, and when invoked with the `-l`, `-a`, and `--all` options. This document specifies the expected behavior and output of each covered option in a Linux environment, as documented by the [Linux manual page].

## Related Resources

**Linux manual page**
* https://man7.org/linux/man-pages/man1/ls.1.html

## Requirements

### RQ.SRS-099.Ls.command
version: 1.0

[Ls command] SHALL list the files and directories contained in the current directory and SHALL exit with code 0 on success.

For example, given a directory containing a file `my_file.txt` and a directory `images`:

```bash
ls
```

Outputs:

```bash
images  my_file.txt
```

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

### RQ.SRS-099.Ls.command.default.ignoresDotEntries
version: 1.0

[Ls command], when invoked without the **-a** or **--all** flag, SHALL ignore entries whose name starts with a dot (`.`),
including the implied `.` and `..` entries, and SHALL exit with code 0 on success.

For example, given a directory containing a visible file `my_file.txt`, a visible directory `images`, a hidden file `.bashrc`, and a hidden directory `.config`:

```bash
ls
```

Outputs:

```bash
images  my_file.txt
```

### RQ.SRS-099.Ls.command.flag.a
version: 1.0

[Ls command] with the flag **-a** SHALL NOT ignore entries whose name starts with a dot (`.`) and SHALL exit with code 0 on success.

For example, given the same directory as above:

```bash
ls -a
```

Outputs:

```bash
.  ..  .bashrc  .config  images  my_file.txt
```

### RQ.SRS-099.Ls.command.flag.a.includesCurrentDirectoryEntry
version: 1.0

[Ls command] with the flag **-a** SHALL include the `.` entry, representing the current directory, in the listing.

### RQ.SRS-099.Ls.command.flag.a.includesParentDirectoryEntry
version: 1.0

[Ls command] with the flag **-a** SHALL include the `..` entry, representing the parent directory, in the listing.

### RQ.SRS-099.Ls.command.flag.a.includesEntriesWithMultipleLeadingDots
version: 1.0

[Ls command] with the flag **-a** SHALL list entries whose name starts with more than one leading dot (e.g. `..config`).

### RQ.SRS-099.Ls.command.flag.a.includesHiddenDirectories
version: 1.0

[Ls command] with the flag **-a** SHALL list directories whose name starts with a dot (`.`), not only hidden files.

### RQ.SRS-099.Ls.command.flag.a.preservesNonHiddenEntries
version: 1.0

[Ls command] with the flag **-a** SHALL still list entries that do not start with a dot, alongside the entries that start with a dot.

### RQ.SRS-099.Ls.command.flag.a.emptyDirectory
version: 1.0

[Ls command] with the flag **-a** on an empty directory SHALL list only the `.` and `..` entries and SHALL exit with code 0 on success.

For example, given an empty directory:

```bash
ls -a
```

Outputs:

```bash
.  ..
```

### RQ.SRS-099.Ls.command.flag.all
version: 1.0

[Ls command] with the flag **--all** SHALL NOT ignore entries whose name starts with a dot (`.`) and SHALL exit with code 0 on success.

For example, given the same directory as above:

```bash
ls --all
```

Outputs:

```bash
.  ..  .bashrc  .config  images  my_file.txt
```

### RQ.SRS-099.Ls.command.flag.all.includesCurrentDirectoryEntry
version: 1.0

[Ls command] with the flag **--all** SHALL include the `.` entry, representing the current directory, in the listing.

### RQ.SRS-099.Ls.command.flag.all.includesParentDirectoryEntry
version: 1.0

[Ls command] with the flag **--all** SHALL include the `..` entry, representing the parent directory, in the listing.

### RQ.SRS-099.Ls.command.flag.all.includesEntriesWithMultipleLeadingDots
version: 1.0

[Ls command] with the flag **--all** SHALL list entries whose name starts with more than one leading dot (e.g. `..config`).

### RQ.SRS-099.Ls.command.flag.all.includesHiddenDirectories
version: 1.0

[Ls command] with the flag **--all** SHALL list directories whose name starts with a dot (`.`), not only hidden files.

### RQ.SRS-099.Ls.command.flag.all.preservesNonHiddenEntries
version: 1.0

[Ls command] with the flag **--all** SHALL still list entries whose name does not start with a dot, together with the entries whose name does.

### RQ.SRS-099.Ls.command.flag.all.emptyDirectory
version: 1.0

[Ls command] with the flag **--all** on an empty directory SHALL list only the `.` and `..` entries and SHALL exit with code 0 on success.

For example, given an empty directory:

```bash
ls --all
```

Outputs:

```bash
.  ..
```

### RQ.SRS-099.Ls.command.flag.all.equivalentToFlagA
version: 1.0

[Ls command] with the flag **--all** SHALL produce output identical to [Ls command] with the flag **-a**, since **--all** is the long-form name of the same option.

## References

* [Linux manual page]

[Linux manual page]: https://man7.org/linux/man-pages/man1/ls.1.html
[Ls command]: https://man7.org/linux/man-pages/man1/ls.1.html
'''
)
