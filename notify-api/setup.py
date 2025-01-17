# Copyright © 2019 Province of British Columbia.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Installer and setup for this module."""
import ast
import io
import os
import re
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup


_version_re = re.compile(r"__version__\s+=\s+(.*)")  # pylint: disable=invalid-name

with open("src/notify_api/version.py", "rb") as f:
    version = str(
        ast.literal_eval(
            _version_re.search(  # pylint: disable=invalid-name
                f.read().decode("utf-8")
            ).group(1)
        )
    )


def read_requirements(filename):
    """
    Get application requirements from the requirements.txt file.

    :return: Python requirements
    """
    return [
        line.strip()
        for line in read(filename).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


def read(*paths, **kwargs):
    """
    Read the contents of a text file safely.

    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


REQUIREMENTS = read_requirements("requirements.txt")

setup(
    name="notify_api",
    version=version,
    author_email="patrick.wei@gov.bc.ca",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    license=read("LICENSE"),
    long_description=read("README.md"),
    zip_safe=False,
    install_requires=REQUIREMENTS,
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
    ],
)
