cmake_minimum_required(VERSION 3.15...3.19)

project(project_name VERSION "0.0.1")

# Export `compile_commands.json` for LSP
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# =======================================
# Dependencies
# =======================================
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_core MODULE src/project_name.cpp)

target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})

install(TARGETS _core DESTINATION .)
