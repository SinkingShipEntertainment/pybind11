name = "pybind11"

version = "2.6.2"

authors = [
    "Pybind"
]

description = \
    """
    pybind11 is a lightweight header-only library that exposes C++ types in Python
    and vice versa, mainly to create Python bindings of existing C++ code.
    Its goals and syntax are similar to the excellent Boost.Python library by
    David Abrahams: to minimize boilerplate code in traditional extension modules by
    inferring type information using compile-time introspection.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"],
]

uuid = "repository.pybind11"


def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.PYBIND11_ROOT_DIR = "{root}"
    env.pybind11_ROOT = "{root}"
    env.pybind11_DIR = "{root}/share/cmake/pybind11"
