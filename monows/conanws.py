import os
import json
from conan import Workspace
from conan import ConanFile
from conan.tools.files import save
from conan.tools.cmake import CMakeDeps, CMakeToolchain, cmake_layout, CMake


class Ws(Workspace):
    def root_conanfile(self):
        return MyWs


class MyWs(ConanFile):
    """ This is a special conanfile, used only for workspace definition of layout
    and generators. It shouldn't have requirements, tool_requirements. It shouldn't have
    build() or package() methods
    """
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def generate(self):
        cmake = CMake(self)
        cmake.configure()

    def layout(self):
        cmake_layout(self)