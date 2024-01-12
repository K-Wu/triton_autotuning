from setuptools import setup
import setuptools
from functools import lru_cache
import os
import subprocess
from subprocess import CalledProcessError
from pathlib import Path


# Project directory root
root_path: Path = Path(__file__).resolve().parent


@lru_cache(maxsize=1)
def get_triton_autotuning_version() -> str:
    """Transformer Engine version string

    Includes Git commit as local version, unless suppressed with
    MYIE_NO_LOCAL_VERSION environment variable.

    """
    with open(root_path / "VERSION", "r") as f:
        version = f.readline().strip()
    try:
        output = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            cwd=root_path,
            check=True,
            universal_newlines=True,
        )
    except (CalledProcessError, OSError):
        pass
    else:
        commit = output.stdout.strip()
        version += f"+{commit}"
    return version


def main():
    packages = setuptools.find_packages(
        include=["triton_autotuning", "triton_autotuning.*"],
    )
    setup(
        name="triton_autotuning",
        version=get_triton_autotuning_version(),
        description="Triton Matmul Library and Autotuning",
        packages=packages,
        setup_requires=[],
        install_requires=[
            "triton",
            "absl-py",
            "tqdm",
        ],
    )


if __name__ == "__main__":
    main()
