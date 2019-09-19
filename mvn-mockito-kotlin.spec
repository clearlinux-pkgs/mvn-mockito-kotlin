#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-mockito-kotlin
Version  : 1.6.0
Release  : 1
URL      : https://github.com/nhaarman/mockito-kotlin/archive/1.6.0.tar.gz
Source0  : https://github.com/nhaarman/mockito-kotlin/archive/1.6.0.tar.gz
Source1  : https://repo1.maven.org/maven2/com/nhaarman/mockito-kotlin/1.6.0/mockito-kotlin-1.6.0.jar
Source2  : https://repo1.maven.org/maven2/com/nhaarman/mockito-kotlin/1.6.0/mockito-kotlin-1.6.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-mockito-kotlin-data = %{version}-%{release}
Requires: mvn-mockito-kotlin-license = %{version}-%{release}
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
# Mockito-Kotlin
[ ![Download](https://maven-badges.herokuapp.com/maven-central/com.nhaarman/mockito-kotlin/badge.svg) ](https://maven-badges.herokuapp.com/maven-central/com.nhaarman/mockito-kotlin)

%package data
Summary: data components for the mvn-mockito-kotlin package.
Group: Data

%description data
data components for the mvn-mockito-kotlin package.


%package license
Summary: license components for the mvn-mockito-kotlin package.
Group: Default

%description license
license components for the mvn-mockito-kotlin package.


%prep
%setup -q -n mockito-kotlin-1.6.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-mockito-kotlin
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-mockito-kotlin/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/nhaarman/mockito-kotlin/1.6.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/nhaarman/mockito-kotlin/1.6.0/mockito-kotlin-1.6.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/nhaarman/mockito-kotlin/1.6.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/nhaarman/mockito-kotlin/1.6.0/mockito-kotlin-1.6.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/nhaarman/mockito-kotlin/1.6.0/mockito-kotlin-1.6.0.jar
/usr/share/java/.m2/repository/com/nhaarman/mockito-kotlin/1.6.0/mockito-kotlin-1.6.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-mockito-kotlin/LICENSE
