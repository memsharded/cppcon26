cmake_minimum_required(VERSION 3.25)
project(myws CXX)

include(FetchContent)

function(add_project PACKAGE_NAME SUBFOLDER)
    message(STATUS "Adding project: ${PACKAGE_NAME}. Folder: ${SUBFOLDER}")
    FetchContent_Declare(
        ${PACKAGE_NAME}
        SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/${SUBFOLDER}
        SYSTEM
        OVERRIDE_FIND_PACKAGE
    )
    FetchContent_MakeAvailable(${PACKAGE_NAME})
endfunction()

add_compile_definitions(PKG_VERSION="WS_01")

add_project(engine engine)
add_library(engine::engine ALIAS engine)
add_project(game game)
