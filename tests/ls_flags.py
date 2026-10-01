from testflows.core import *
from testflows.connect import Shell
from testflows.asserts import error
from requirements.requirements import (
    RQ_SRS_099_Ls_command,
    RQ_SRS_099_Ls_command_flag_l,
    RQ_SRS_099_Ls_command_flag_a,
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
@Name("ls -a shows hidden and visible files")
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


@TestFeature
def lsFlagsFeature(self):
    for scenario in loads(current_module(), Scenario):
        scenario()


if main():
    lsFlagsFeature()
