"""Setup module for day of code package."""

from setuptools import setup

setup(
    name="day of code",
    description="Day of code katas.",
    package_dir={"": "src"},
    author="Joseph Kim",
    author_email="joseph.kim.kr@gmail.com",
    py_modules=[],
    install_requires=[],
    extras_require={
        "test": ["pytest", "pytest-cov", "pytest-watch", "tox"],
        "development": ["ipython"]
    },
    entry_points={
    }
)
