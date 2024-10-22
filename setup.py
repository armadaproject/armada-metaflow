"""Setup.py for armada-metaflow which provides @armada step decorator for metaflow"""

from setuptools import setup, find_namespace_packages

version = "0.0.1"

with open("OSS_VERSION", "rt", encoding="utf-8") as f:
    mf_version = f.read()

setup(
    name="armada-metaflow",
    version=version,
    description="Armada Metaflow Custom Extension",
    author="GR-OSS",
    author_email="clif@gr-oss.io",
    packages=find_namespace_packages(include=["metaflow_extensions.*"]),
    py_modules=[
        "metaflow_extensions",
    ],
    install_requires=[
        f"metaflow=={mf_version}",
        "armada-client",
    ],
)
