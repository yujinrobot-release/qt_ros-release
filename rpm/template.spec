Name:           ros-kinetic-qt-ros
Version:        0.2.10
Release:        0%{?dist}
Summary:        ROS qt_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/qt_ros
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-qt-build
Requires:       ros-kinetic-qt-create
Requires:       ros-kinetic-qt-tutorials
BuildRequires:  ros-kinetic-catkin

%description
Simple qt cmake build tools and master-chooser style application template.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Feb 10 2018 Daniel Stonier <d.stonier@gmail.com> - 0.2.10-0
- Autogenerated by Bloom

* Sat Aug 13 2016 Daniel Stonier <d.stonier@gmail.com> - 0.2.9-0
- Autogenerated by Bloom

