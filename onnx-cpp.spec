### RPM external onnx-cpp 1.22.0
## INCLUDE cpp-standard
## INITENV +PATH LD_LIBRARY_PATH %{i}/lib

Source: https://github.com/onnx/onnx/archive/refs/tags/v%{realversion}.tar.gz

BuildRequires: cmake ninja
Requires: protobuf abseil-cpp python3

%prep
%setup -q -n onnx-%{realversion}

%build
rm -rf ../build
mkdir ../build

cmake -S . -B ../build -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX="%{i}" \
  -DCMAKE_INSTALL_LIBDIR=lib \
  -DCMAKE_CXX_STANDARD=%{cms_cxx_standard} \
  -DCMAKE_PREFIX_PATH="${PROTOBUF_ROOT};${ABSEIL_CPP_ROOT}" \
  -DCMAKE_FIND_PACKAGE_PREFER_CONFIG=ON \
  -DProtobuf_DIR="${PROTOBUF_ROOT}/lib/cmake/protobuf" \
  -DProtobuf_PROTOC_EXECUTABLE="${PROTOBUF_ROOT}/bin/protoc" \
  -DONNX_CUSTOM_PROTOC_EXECUTABLE="${PROTOBUF_ROOT}/bin/protoc" \
  -DBUILD_SHARED_LIBS=ON \
  -DONNX_BUILD_PYTHON=OFF \
  -DONNX_BUILD_TESTS=OFF \
  -DONNX_BUILD_CUSTOM_PROTOBUF=OFF \
  -DONNX_USE_PROTOBUF_SHARED_LIBS=ON \
  -DONNX_INSTALL=ON \
  -DFETCHCONTENT_FULLY_DISCONNECTED=ON

cd ../build
ninja -v %{makeprocesses}

%install
cd ../build
ninja -v %{makeprocesses} install
