Name:           deskos-multimedia-codecs
Summary:        DeskOS multimedia codecs
Version:        0.1.0
Release:        1%{?dist}

License:        GPLv3
Group:          System Environment/Base

URL:            https://deskosproject.org

Requires:       gstreamer1-libav
Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-plugins-bad-freeworld
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-ugly
Requires:       gstreamer-ffmpeg
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-bad-free
Requires:       gstreamer-plugins-bad-nonfree
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-ugly
Requires:       faac
Requires:       faad2
Requires:       flac
Requires:       lame
Requires:       libdca
Requires:       libmad
Requires:       libmatroska
Requires:       x264
Requires:       x265
Requires:       xvidcore

BuildArch:      noarch

%description
Multimedia codecs for DeskOS.

%files

%changelog
* Fri Nov 18 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1.0-1
- Initial package for DeskOS
