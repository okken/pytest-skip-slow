import pytest


@pytest.fixture()
def slow_examples(pytester):
    pytester.copy_example("examples/test_slow.py")


def test_skip_slow(pytester, slow_examples):
    result = pytester.runpytest("-v")
    result.stdout.fnmatch_lines(
        [
            "*test_normal PASSED*",
            "*test_slow SKIPPED (need --slow option to run)*",
        ],
        consecutive=True,
    )
    result.assert_outcomes(passed=1, skipped=1)


def test_run_slow(pytester, slow_examples):
    result = pytester.runpytest("--slow")
    result.assert_outcomes(passed=2)


def test_run_slow_alt(pytester, slow_examples):
    result = pytester.runpytest("--run-slow")
    result.assert_outcomes(passed=2)


def test_run_only_slow(pytester, slow_examples):
    result = pytester.runpytest("-v", "-m", "slow", "--slow")
    result.stdout.fnmatch_lines(["*test_slow PASSED*"])
    outcomes = result.parseoutcomes()
    assert outcomes["passed"] == 1
    assert outcomes["deselected"] == 1


def test_run_only_slow_alt(pytester, slow_examples):
    result = pytester.runpytest("-v", "-m", "slow", "--run-slow")
    result.stdout.fnmatch_lines(["*test_slow PASSED*"])


@pytest.fixture()
def hugemem_examples(pytester):
    pytester.copy_example("examples/test_hugemem.py")


def test_skip_hugemem(pytester, hugemem_examples):
    result = pytester.runpytest("-v")
    result.stdout.fnmatch_lines(
        [
            "*test_normal PASSED*",
            "*test_hugemem SKIPPED (need --hugemem option to run)*",
        ],
        consecutive=True,
    )
    result.assert_outcomes(passed=1, skipped=1)


def test_run_hugemem(pytester, hugemem_examples):
    result = pytester.runpytest("--hugemem")
    result.assert_outcomes(passed=2)


def test_run_hugemem_alt(pytester, hugemem_examples):
    result = pytester.runpytest("--run-hugemem")
    result.assert_outcomes(passed=2)


def test_run_only_hugemem(pytester, hugemem_examples):
    result = pytester.runpytest("-v", "-m", "hugemem", "--hugemem")
    result.stdout.fnmatch_lines(["*test_hugemem PASSED*"])
    outcomes = result.parseoutcomes()
    assert outcomes["passed"] == 1
    assert outcomes["deselected"] == 1


def test_run_only_hugemem_alt(pytester, hugemem_examples):
    result = pytester.runpytest("-v", "-m", "hugemem", "--run-hugemem")
    result.stdout.fnmatch_lines(["*test_hugemem PASSED*"])


def test_help(pytester):
    result = pytester.runpytest("--help")
    result.stdout.fnmatch_lines(
        [
            "*--slow, --run-slow * include tests marked slow*",
            "*--hugemem, --run-hugemem",
            "* include tests marked memory intensive*",
        ],
        consecutive=True,
    )
