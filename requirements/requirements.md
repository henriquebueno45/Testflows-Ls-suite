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
