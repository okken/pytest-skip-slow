import pytest

@pytest.fixture()
def examples(pytester):
    pytester.copy_example("examples/test_slow.py")

def test_skip_slow(pytester, examples):
    result = pytester.runpytest("-v")
    result.stdout.fnmatch_lines([
        "*test_normal PASSED*",
        "*test_slow SKIPPED (need --slow option to run)*"
    ])
    result.assert_outcomes(passed=1, skipped=1)

def test_run_slow(pytester, examples):
    result = pytester.runpytest("--slow")
    result.assert_outcomes(passed=2)

def test_run_only_slow(pytester, examples):
    result = pytester.runpytest("-v", "-m", "slow", "--slow")
    result.stdout.fnmatch_lines(["*test_slow PASSED*"])
    outcomes = result.parseoutcomes()
    assert outcomes['passed'] == 1
    assert outcomes['deselected'] == 1

def test_help(pytester):
    result = pytester.runpytest("--help")
    result.stdout.fnmatch_lines([
        "*--slow * include tests marked slow*"
    ])
