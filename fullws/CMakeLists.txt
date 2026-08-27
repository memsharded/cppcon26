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

include(build/conanws_build_order.cmake)

foreach(pair ${CONAN_WS_BUILD_ORDER})
    string(FIND "${pair}" ":" pos)
    string(SUBSTRING "${pair}" 0 "${pos}" pkg)
    math(EXPR pos "${pos} + 1")  # Skip the separator
    string(SUBSTRING "${pair}" "${pos}" -1 folder)

    add_project(${pkg} ${folder})
    # This target should be defined in the liba/CMakeLists.txt, but we can fix it here
    get_target_property(target_type ${pkg} TYPE)
    if (NOT target_type STREQUAL "EXECUTABLE")
        add_library(${pkg}::${pkg} ALIAS ${pkg})
    endif()
endforeach()
