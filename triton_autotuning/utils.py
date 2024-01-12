from functools import lru_cache
import subprocess


# From https://stackoverflow.com/a/4104188
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


@lru_cache(maxsize=None)
@run_once
def assert_git_exists() -> None:
    """Check if git is installed and available in the path."""
    try:
        subprocess.check_output(["git", "--version"])
    except Exception:  # any error means git is not installed
        raise OSError(
            "Git is not installed. Please install git and try again."
        )


@lru_cache(maxsize=None)
@run_once
def assert_gh_exists():
    """Check if gh is installed."""
    try:
        subprocess.check_output(["gh", "--version"])
    except Exception:  # any error means git is not installed
        raise OSError(
            "Github cli is not installed. Please install gh and try again."
        )


@lru_cache(maxsize=None)
@run_once
def get_spreadsheet_url() -> str:
    """Get the SPREADSHEET_URL github repo variable by `gh variable list |grep SPREADSHEET_URL`."""
    assert_git_exists()
    assert_gh_exists()
    try:
        out = subprocess.check_output(["gh", "variable", "list"]).decode(
            "utf-8"
        )
    except Exception:
        raise OSError("Failed to run `gh variable list`.")
    for line in out.splitlines():
        if "SPREADSHEET_URL" in line:
            return line.split()[1]
    raise OSError("Failed to find SPREADSHEET_URL in `gh variable list`.")
