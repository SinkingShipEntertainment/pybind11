name = "pybind11"

version = "2.9.2.sse.1.0.0"

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
    c.build_thread_count = "physical_cores"

requires = [
]

private_build_requires = [
]

variants = [
    # ['platform-linux', 'arch-x86_64', 'os-centos-7', "python-2.7"],  # pointless since we cannot use Python 2 with pybind11
    ['platform-linux', 'arch-x86_64', 'os-centos-7', "python-3.7"],
    ['platform-linux', 'arch-x86_64', 'os-centos-7', "python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
]

# If want to use Ninja, run:
# rez-build -i --cmake-build-system "ninja"
# rez-release --cmake-build-system "ninja"
#
# Pass cmake arguments:
# rez-build -i
# rez-release

uuid = "repository.pybind11"


def pre_build_commands():
    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.PYBIND11_ROOT_DIR = "{root}"
    env.pybind11_ROOT = "{root}"
    env.pybind11_DIR = "{root}/share/cmake/pybind11"
