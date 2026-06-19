cmake_minimum_required(VERSION 3.10)
project(Fawkes)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

file(GLOB SOURCES "src/*.cpp" "apps/*.cpp")

add_executable(fawkes ${SOURCES})

target_include_directories(fawkes PRIVATE include)
