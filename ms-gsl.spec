### RPM external ms-gsl 4.0.0
%define github_user microsoft
%define branch main
%define tag v%{realversion}

Source: git+https://github.com/%{github_user}/GSL.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}.tgz

BuildRequires: cmake

%prep
%setup -q -n %{n}-%{realversion}

%build
cmake -S . -B ../build \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX="%{i}" \
  -DGSL_INSTALL=ON \
  -DGSL_TEST=OFF

cmake --build ../build --parallel %{makeprocesses}

%install
cmake --install ../build
