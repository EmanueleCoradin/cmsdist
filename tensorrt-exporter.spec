### RPM external tensorrt-exporter 11.4.0.106

%define archive TensorRT-Enterprise-%{realversion}-Linux-x86_64-cuda-13.4-Release-external

%ifarch x86_64
Source: https://developer.nvidia.com/downloads/compute/machine-learning/tensorrt/11.4.0/tars/%{archive}.tar.zst
%endif

Requires: cuda

%prep
%setup -q -T -c -n TensorRT-build
tar --zstd -xf %{SOURCE0} --strip-components=1

%build
# TensorRT is distributed as precompiled binaries.

%install
mkdir -p %{i}

cp -a include %{i}/
cp -a lib     %{i}/
cp -a cmake   %{i}/
cp -a bin     %{i}/
cp -a doc     %{i}/
