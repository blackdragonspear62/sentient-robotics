cmake_minimum_required(VERSION 3.16)
project(sentient_sonic_deploy VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# ============================================================
# Dependencies
# ============================================================
find_package(Eigen3 3.3 REQUIRED)
find_package(yaml-cpp REQUIRED)

# ONNX Runtime
set(ONNXRUNTIME_ROOT "" CACHE PATH "Path to ONNX Runtime installation")
if(ONNXRUNTIME_ROOT)
    set(ONNXRUNTIME_INCLUDE_DIRS "${ONNXRUNTIME_ROOT}/include")
    set(ONNXRUNTIME_LIBRARIES "${ONNXRUNTIME_ROOT}/lib/libonnxruntime.so")
endif()

# ZeroMQ
find_package(PkgConfig)
pkg_check_modules(ZMQ libzmq)

# ============================================================
# Sentient-SONIC Deploy Library
# ============================================================
add_library(sentient_sonic_core STATIC
    src/inference_engine.cpp
    src/safety_controller.cpp
    src/robot_interface.cpp
    src/state_estimator.cpp
    src/zmq_bridge.cpp
    src/onnx_utils.cpp
)

target_include_directories(sentient_sonic_core PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${ONNXRUNTIME_INCLUDE_DIRS}
    ${ZMQ_INCLUDE_DIRS}
)

target_link_libraries(sentient_sonic_core PUBLIC
    Eigen3::Eigen
    yaml-cpp
    ${ONNXRUNTIME_LIBRARIES}
    ${ZMQ_LIBRARIES}
    pthread
)

# ============================================================
# Executables
# ============================================================
add_executable(sentient_deploy src/main_deploy.cpp)
target_link_libraries(sentient_deploy PRIVATE sentient_sonic_core)

add_executable(sentient_test_inference src/test_inference.cpp)
target_link_libraries(sentient_test_inference PRIVATE sentient_sonic_core)

# G1 specific deployment reference
add_executable(g1_deploy_onnx_ref src/g1_deploy_onnx_ref.cpp)
target_link_libraries(g1_deploy_onnx_ref PRIVATE sentient_sonic_core)

# ============================================================
# Install
# ============================================================
install(TARGETS sentient_deploy sentient_sonic_core
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(DIRECTORY include/ DESTINATION include)
