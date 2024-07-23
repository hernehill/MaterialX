name = "materialx"

version = "1.38.10.hh.1.0.0"

authors = [
    "ILM & AcademySoftwareFoundation",
]

description = (
    """Open standard for transfer of rich material and look-development contents"""
)

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
    "pybind11",
]

private_build_requires = []

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
    ["python-3.12"],
]

# NOTE: Run (first time only), after git clone: git submodule update --init --recursive


def commands():
    env.REZ_MATERIALX_ROOT = "{root}"
    env.MATERIALX_ROOT = "{root}"
    env.MATERIALX_LOCATION = "{root}"
    env.MATERIALX_INCLUDE_DIR = "{root}/include"

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/lib/cmake/MaterialX")
    env.PYTHONPATH.append("{root}/python")


uuid = "repository.MaterialX"
