# http://github.com/ghodss/yaml

%global goipath         github.com/ghodss/yaml
%global commit          0ca9ea5df5451ffdf184b4428c902747c2c11cd7


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.21%{?dist}
Summary:        A better way to marshal and unmarshal YAML in Golang
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(gopkg.in/yaml.v2)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
# constant 9223372036854775807 overflows int
%ifnarch %{ix86} %{arm}
%gochecks
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.20.git0ca9ea5
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.19.20170328git0ca9ea5
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.git0ca9ea5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.git0ca9ea5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.git0ca9ea5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.git0ca9ea5
- Bump to upstream 0ca9ea5df5451ffdf184b4428c902747c2c11cd7
  related: #1249030

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitaa0c862
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.gitaa0c862
- Bump to upstream aa0c862057666179de291b67d9f093d12b5a8473
  related: #1249030

* Sat Dec 17 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.git73d445a
- Polish the spec file
  related: #1249030

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.git73d445a
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun May 15 2016 jchaloup <jchaloup@redhat.com> - 0-0.10.git73d445a
- Bump to upstream 73d445a93680fa1a78ae23a5839bad48f32ba1ee
  related: #1249030

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git588cb43
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git588cb43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.git588cb43
- Update to spec-2.1
  related: #1249030

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git588cb43
- Update spec file to spec-2.0
  resolves: #1249030

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git588cb43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git588cb43
- Bump to upstream 588cb435e59ee8b6c2795482887755841ad67207
  related: #1172603

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git3bc1590
- Bump to upstream 3bc1590d16074751993dd3b1a76e7a8d1a916a11
  related: #1172603

* Wed Dec 24 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.git92ff9d3
- Bump to 4fb5c728a37b361a1e971a3bb3d785fcc96b6ef5
  related: #1172603

* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.git92ff9d3
- First package for Fedora
  resolves: #1172603

