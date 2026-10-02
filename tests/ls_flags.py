from testflows.core import *
from testflows.connect import Shell
from testflows.asserts import error
from requirements.requirements import (
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
)


@TestScenario
@Name("Plain ls command")
@Requirements(RQ_SRS_099_Ls_command("1.0"))
def scenario1(self):
    """Check 'ls' lists the files and directories of the current directory."""
    with Shell() as bash:
        try:
            with Given("a known file exists in the current directory"):
                bash("touch known_file")
            with When("I run ls on the current directory"):
                cmd = bash("ls")
            with Then("the output should contain the known file"):
                assert cmd.exitcode == 0, error("ls command failed")
                assert "known_file" in cmd.output, error("ls did not list known_file")
        finally:
            with Finally("teardown: remove the known file"):
                bash("rm -f known_file")


@TestScenario
@Name("ls -l shows total and file details")
@Requirements(RQ_SRS_099_Ls_command_flag_l("1.0"))
def scenario2(self):
    """Check 'ls -l' returns the total block count and detailed file listing."""
    with Shell() as bash:
        try:
            with Given("a known file exists in the current directory"):
                bash("touch known_file")
            with When("I run ls -l on the current directory"):
                cmd = bash("ls -l")
            with Then("the output should include a 'total' line and the known file"):
                assert cmd.exitcode == 0, error("ls -l command failed")
                assert "total" in cmd.output, error("ls -l output does not contain 'total'")
                assert "known_file" in cmd.output, error("ls -l did not list known_file")
        finally:
            with Finally("teardown: remove the known file"):
                bash("rm -f known_file")


@TestScenario
@Name("ls ignores entries starting with . by default")
@Requirements(RQ_SRS_099_Ls_command_default_ignoresDotEntries("1.0"))
def scenario_default_ignores_dot_entries(self):
    """Check plain 'ls' (without -a/--all) ignores entries whose name starts with a dot."""
    tmp_dir = None
    with Shell() as bash:
        try:
            with Given("a hidden file and a visible file"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
                bash("touch .hidden_test visible_test")
            with When("I run plain ls on the current directory"):
                cmd = bash("ls")
            with Then("the output should contain the visible file but not the hidden file, '.' or '..'"):
                assert cmd.exitcode == 0, error("ls command failed")
                assert "visible_test" in cmd.output.split(), error("ls did not list visible_test")
                assert ".hidden_test" not in cmd.output.split(), error("ls did not ignore .hidden_test")
                assert "." not in cmd.output.split(), error("ls did not ignore the implied '.' entry")
                assert ".." not in cmd.output.split(), error("ls did not ignore the implied '..' entry")
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls -a does not ignore files starting with .")
@Requirements(RQ_SRS_099_Ls_command_flag_a("1.0"))
def scenario3(self):
    """Check 'ls -a' returns both hidden and visible files."""
    with Shell() as bash:
        try:
            with Given("a hidden file and a visible file are created"):
                bash("touch .hidden_test visible_test")
            with When("I run ls -a on the current directory"):
                cmd = bash("ls -a")
            with Then("the output should contain both the hidden and the visible file"):
                assert cmd.exitcode == 0, error("ls -a command failed")
                assert ".hidden_test" in cmd.output, error("ls -a did not list the hidden file")
                assert "visible_test" in cmd.output, error("ls -a did not list the visible file")
        finally:
            with Finally("teardown: remove the hidden and visible files"):
                bash("rm -f .hidden_test visible_test")

@TestScenario
@Name("ls -a includes the current directory entry, indicated by the '.' element in the output")
@Requirements(RQ_SRS_099_Ls_command_flag_a_includesCurrentDirectoryEntry("1.0"))
def scenario4(self):
    """Check 'ls -a' outputs the current folder, indicated by the . element in the output"""
    with Shell() as bash:
        tmp_dir = None
        try:
            with Given("the ls -a command is executed inside a folder"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
            with When("Run ls -a command on the current directory"):
                cmd = bash("ls -a")
            with Then("The output of the command SHALL contain the . element and exit with code 0"):
                assert cmd.exitcode == 0, error("ls -a command failed")
                assert "." in cmd.output.strip(), error("ls -a did not return the current directory (. element)")
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")

@TestScenario
@Name("ls -a includes the parent directory entry, indicated by the '..' element in the output")
@Requirements(RQ_SRS_099_Ls_command_flag_a_includesParentDirectoryEntry("1.0"))
def scenario5(self):
    """Check 'ls -a' outputs the parent folder, indicated by the '..' element in the output """
    tmp_dir = None
    with Shell() as bash:
        try:
            with Given("the ls -a command is executed inside a folder"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
            with When("Run the ls -a command on the current directory"):
                cmd = bash("ls -a")
            with Then("The output should contain the '..' element and exit with code 0"):
                assert cmd.exitcode == 0, error("ls -a command failed")
                assert ".." in cmd.output.split(), error("ls -a did not return the parent folder ('..' element)")
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")

@TestScenario
@Name("ls -a includes entries with multiple leading dots")
@Requirements(RQ_SRS_099_Ls_command_flag_a_includesEntriesWithMultipleLeadingDots("1.0"))
def scenario6(self):
    """Check 'ls -a' lists entries whose name starts with more than one leading dot."""
    tmp_dir = None
    multi_dot_entry = "..double_dot_file"
    with Shell() as bash:
        try:
            with Given("a file whose name starts with more than one dot"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
                bash(f"touch {multi_dot_entry}")
            with When("I run ls -a on the current directory"):
                cmd = bash("ls -a")
            with Then("the output should contain the multiple-leading-dots entry and exit with code 0"):
                assert cmd.exitcode == 0, error("ls -a command failed")
                assert multi_dot_entry in cmd.output.split(), error(
                    "ls -a did not list the entry with multiple leading dots"
                )
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls -a includes hidden directories")
@Requirements(RQ_SRS_099_Ls_command_flag_a_includesHiddenDirectories("1.0"))
def scenario_a_includes_hidden_directories(self):
    """Check 'ls -a' lists hidden directories, not only hidden files (entries include directories)."""
    tmp_dir = None
    hidden_dir = ".hidden_dir"
    with Shell() as bash:
        try:
            with Given("a hidden subdirectory"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
                bash(f"mkdir {hidden_dir}")
            with When("I run ls -a on the current directory"):
                cmd = bash("ls -a")
            with Then("the output should list the hidden directory name"):
                assert cmd.exitcode == 0, error("ls -a command failed")
                assert hidden_dir in cmd.output.split(), error("ls -a did not list the hidden directory")
            with And("the listed entry should actually be a directory"):
                cmd_l = bash("ls -la")
                assert cmd_l.exitcode == 0, error("ls -la command failed")
                lines = [l for l in cmd_l.output.splitlines() if l.strip().endswith(f" {hidden_dir}")]
                assert lines, error(f"{hidden_dir} not found in ls -la output")
                assert lines[0].startswith("d"), error(f"{hidden_dir} is not reported as a directory")
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls -a preserves non-hidden entries")
@Requirements(RQ_SRS_099_Ls_command_flag_a_preservesNonHiddenEntries("1.0"))
def scenario7(self):
    """Check 'ls -a' still lists non-hidden entries alongside hidden ones."""
    tmp_dir = None
    with Shell() as bash:
        try:
            with Given("a hidden file and a visible file"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
                bash("touch .hidden_test visible_test")
            with When("I run ls -a on the current directory"):
                cmd = bash("ls -a")
            with Then("the output should contain both the hidden and the visible entry and exit with code 0"):
                assert cmd.exitcode == 0, error("ls -a command failed")
                assert ".hidden_test" in cmd.output.split(), error("ls -a did not list the hidden file")
                assert "visible_test" in cmd.output.split(), error("ls -a did not list the visible file")
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls -a on an empty directory lists only . and ..")
@Requirements(RQ_SRS_099_Ls_command_flag_a_emptyDirectory("1.0"))
def scenario8(self):
    """Check 'ls -a' on an empty directory lists only the '.' and '..' entries."""
    tmp_dir = None
    with Shell() as bash:
        try:
            with Given("an empty, isolated directory"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
            with When("I run ls -a on the current directory"):
                cmd = bash("ls -a")
            with Then("the output should contain only the '.' and '..' entries and exit with code 0"):
                assert cmd.exitcode == 0, error("ls -a command failed")
                assert set(cmd.output.split()) == {".", ".."}, error(
                    "ls -a on an empty directory did not list only . and .."
                )
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls --all does not ignore entries starting with .")
@Requirements(RQ_SRS_099_Ls_command_flag_all("1.0"))
def scenario9(self):
    """Check 'ls --all' returns both hidden and visible entries."""
    tmp_dir = None
    with Shell() as bash:
        try:
            with Given("a hidden file and a visible file"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
                bash("touch .hidden_test visible_test")
            with When("I run ls --all on the current directory"):
                cmd = bash("ls --all")
            with Then("the output should contain both the hidden and the visible file and exit with code 0"):
                assert cmd.exitcode == 0, error("ls --all command failed")
                assert ".hidden_test" in cmd.output.split(), error("ls --all did not list the hidden file")
                assert "visible_test" in cmd.output.split(), error("ls --all did not list the visible file")
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls --all includes the '.' entry")
@Requirements(RQ_SRS_099_Ls_command_flag_all_includesCurrentDirectoryEntry("1.0"))
def scenario10(self):
    """Check 'ls --all' outputs the current folder, indicated by the '.' element."""
    tmp_dir = None
    with Shell() as bash:
        try:
            with Given("an empty, isolated directory"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
            with When("I run ls --all on the current directory"):
                cmd = bash("ls --all")
            with Then("the output should contain the '.' element and exit with code 0"):
                assert cmd.exitcode == 0, error("ls --all command failed")
                assert "." in cmd.output.split(), error("ls --all did not return the current directory (. element)")
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls --all includes the '..' entry")
@Requirements(RQ_SRS_099_Ls_command_flag_all_includesParentDirectoryEntry("1.0"))
def scenario11(self):
    """Check 'ls --all' outputs the parent folder, indicated by the '..' element."""
    tmp_dir = None
    with Shell() as bash:
        try:
            with Given("an empty, isolated directory"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
            with When("I run ls --all on the current directory"):
                cmd = bash("ls --all")
            with Then("the output should contain the '..' element and exit with code 0"):
                assert cmd.exitcode == 0, error("ls --all command failed")
                assert ".." in cmd.output.split(), error("ls --all did not return the parent folder ('..' element)")
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls --all includes entries with multiple leading dots")
@Requirements(RQ_SRS_099_Ls_command_flag_all_includesEntriesWithMultipleLeadingDots("1.0"))
def scenario12(self):
    """Check 'ls --all' lists entries whose name starts with more than one leading dot."""
    tmp_dir = None
    multi_dot_entry = "..double_dot_file"
    with Shell() as bash:
        try:
            with Given("a file whose name starts with more than one dot"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
                bash(f"touch {multi_dot_entry}")
            with When("I run ls --all on the current directory"):
                cmd = bash("ls --all")
            with Then("the output should contain the multiple-leading-dots entry and exit with code 0"):
                assert cmd.exitcode == 0, error("ls --all command failed")
                assert multi_dot_entry in cmd.output.split(), error(
                    "ls --all did not list the entry with multiple leading dots"
                )
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls --all includes hidden directories")
@Requirements(RQ_SRS_099_Ls_command_flag_all_includesHiddenDirectories("1.0"))
def scenario_all_includes_hidden_directories(self):
    """Check 'ls --all' lists hidden directories, not only hidden files (entries include directories)."""
    tmp_dir = None
    hidden_dir = ".hidden_dir"
    with Shell() as bash:
        try:
            with Given("a hidden subdirectory"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
                bash(f"mkdir {hidden_dir}")
            with When("I run ls --all on the current directory"):
                cmd = bash("ls --all")
            with Then("the output should list the hidden directory name"):
                assert cmd.exitcode == 0, error("ls --all command failed")
                assert hidden_dir in cmd.output.split(), error("ls --all did not list the hidden directory")
            with And("the listed entry should actually be a directory"):
                cmd_l = bash("ls -la")
                assert cmd_l.exitcode == 0, error("ls -la command failed")
                lines = [l for l in cmd_l.output.splitlines() if l.strip().endswith(f" {hidden_dir}")]
                assert lines, error(f"{hidden_dir} not found in ls -la output")
                assert lines[0].startswith("d"), error(f"{hidden_dir} is not reported as a directory")
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls --all preserves non-hidden entries")
@Requirements(RQ_SRS_099_Ls_command_flag_all_preservesNonHiddenEntries("1.0"))
def scenario13(self):
    """Check 'ls --all' still lists non-hidden entries alongside hidden ones."""
    tmp_dir = None
    with Shell() as bash:
        try:
            with Given("a hidden file and a visible file"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
                bash("touch .hidden_test visible_test")
            with When("I run ls --all on the current directory"):
                cmd = bash("ls --all")
            with Then("the output should contain both the hidden and the visible entry and exit with code 0"):
                assert cmd.exitcode == 0, error("ls --all command failed")
                assert ".hidden_test" in cmd.output.split(), error("ls --all did not list the hidden file")
                assert "visible_test" in cmd.output.split(), error("ls --all did not list the visible file")
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls --all on an empty directory lists only . and ..")
@Requirements(RQ_SRS_099_Ls_command_flag_all_emptyDirectory("1.0"))
def scenario14(self):
    """Check 'ls --all' on an empty directory lists only the '.' and '..' entries."""
    tmp_dir = None
    with Shell() as bash:
        try:
            with Given("an empty, isolated directory"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
            with When("I run ls --all on the current directory"):
                cmd = bash("ls --all")
            with Then("the output should contain only the '.' and '..' entries and exit with code 0"):
                assert cmd.exitcode == 0, error("ls --all command failed")
                assert set(cmd.output.split()) == {".", ".."}, error(
                    "ls --all on an empty directory did not list only . and .."
                )
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestScenario
@Name("ls --all produces output identical to ls -a")
@Requirements(RQ_SRS_099_Ls_command_flag_all_equivalentToFlagA("1.0"))
def scenario15(self):
    """Check 'ls --all' and 'ls -a' produce identical output, since --all is the long form of -a."""
    tmp_dir = None
    with Shell() as bash:
        try:
            with Given("a hidden file, a visible file and a multiple-leading-dots file"):
                tmp_dir = bash("mktemp -d").output.strip()
                bash(f"cd {tmp_dir}")
                bash("touch .hidden_test visible_test ..double_dot_file")
            with When("I run both ls -a and ls --all on the current directory"):
                cmd_a = bash("ls -a")
                cmd_all = bash("ls --all")
            with Then("both commands should exit with code 0 and produce the same set of entries"):
                assert cmd_a.exitcode == 0, error("ls -a command failed")
                assert cmd_all.exitcode == 0, error("ls --all command failed")
                assert set(cmd_a.output.split()) == set(cmd_all.output.split()), error(
                    "ls -a and ls --all did not produce the same listing"
                )
        finally:
            with Finally("teardown: remove the temporary directory"):
                if tmp_dir:
                    bash(f"rm -rf {tmp_dir}")


@TestFeature
def lsFlagsFeature(self):
    for scenario in loads(current_module(), Scenario):
        scenario()


if main():
    lsFlagsFeature()
