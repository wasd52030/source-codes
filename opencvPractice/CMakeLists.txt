cmake_minimum_required(VERSION 3.0.0)
project(opencv_practice VERSION 0.1.0)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

include(CTest)
enable_testing()

find_package(OpenCV REQUIRED)                              
include_directories(${OpenCV_INCLUDE_DIRS})

file(GLOB images "./images/*")
# 複製上面所找到的images資料夾下面的檔案到叫做images的資料夾裡面
file(COPY ${images} DESTINATION images)

aux_source_directory(. DIR_SRCS)
add_subdirectory(chessBoard)

add_executable(main main.cpp)
target_link_libraries (main ${OpenCV_LIBS}) 
target_link_libraries(main chessBoard)

