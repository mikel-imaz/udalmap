from setuptools import setup, find_packages

setup(
    author="Mikel Imaz",
    description="A wrapper for Udalmap API",
    name="udalmap",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["requests", "pandas", "matplotlib"],
    python_requires=">=3.6",
)