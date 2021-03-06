# rpmrebuild autogenerated specfile

BuildRoot: /root/.tmp/rpmrebuild.11926/work/root
AutoProv: no
%undefine __find_provides
AutoReq: no
%undefine __find_requires
# Do not try autogenerate prereq/conflicts/obsoletes and check files
%undefine __check_files
%undefine __find_prereq
%undefine __find_conflicts
%undefine __find_obsoletes
# Be sure buildpolicy set to do nothing
%define __spec_install_post %{nil}
# Something that need for rpm-4.1
%define _missing_doc_files_terminate_build 0

# HDP specific parameters
%define hdp_version 2.6.1.0
%define tez_src /root/tez
%define tez_version 0.9.2-SNAPSHOT

Name:          tez_2_6_1_0_129
Version:       0.9.1.2.6.1.0
Release:       129
License:       Apache License v2.0 
Group:         Development/Libraries
Summary:       Tez is an application framework which allows for a complex directed-acyclic-graph of tasks for processing data and is built atop Apache Hadoop YARN.


URL:           http://tez.incubator.apache.org







Provides:      tez_2_6_1_0_129 = 0.9.1.2.6.1.0-129
Requires:      /bin/sh  
Requires:      /bin/sh  
Requires:      /bin/sh  
Requires:      hadoop_2_6_1_0_129  
Requires:      hadoop_2_6_1_0_129-hdfs  
Requires:      hadoop_2_6_1_0_129-mapreduce  
Requires:      hadoop_2_6_1_0_129-yarn  
Requires:      hdp-select >= 2.6.1.0-129
#Requires:      rpmlib(CompressedFileNames) <= 3.0.4-1
#Requires:      rpmlib(FileDigests) <= 4.6.0-1
#Requires:      rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires:      sh-utils  
#Requires:      rpmlib(PayloadIsXz) <= 5.2-1
#suggest
#enhance
%description
Tez is an application framework which allows for a complex
directed-acyclic-graph of tasks for processing data
and is built atop Apache Hadoop YARN.
%prep -p /bin/sh
# make sure that the current build dir is configured under /usr/hdp

echo "Build root: $RPM_BUILD_ROOT"
echo "HDP version: %{hdp_version}"
echo "Release: %{release}"
echo "Tez src: %{tez_src}"
echo "Tez version: %{tez_version}"

%define hdp_build %hdp_version-%release
%define hdp /usr/hdp/%hdp_version-%release
%define jar_version %{tez_version}.%{hdp_build}
TEZ_DIST=%tez_src/tez-dist/target/tez-%tez_version-minimal

if [ ! -d "$RPM_BUILD_ROOT" ]; then
  echo "Build root $RPM_BUILD_ROOT doesn't exist"
  mkdir $RPM_BUILD_ROOT
fi

if [ ! -d "$TEZ_DIST" ]; then
  echo "Tez distribution source doesn't exist. Make sure that a version of Tez is built from source and is available under tez-dist module at $TEZ_DIST"
  exit -1;
fi

# cleanup everything before we start
rm -rf $RPM_BUILD_ROOT/*

# create a current HDP dir
mkdir -p $RPM_BUILD_ROOT%{hdp}

# current build parameters
HDP_OUT=$RPM_BUILD_ROOT%hdp
OUT=$RPM_BUILD_ROOT%hdp/tez
DIST=$TEZ_DIST
SRC=%tez_src

# tez etc conf dir
mkdir -p $HDP_OUT/etc/tez/conf.dist
mkdir -p $HDP_OUT/etc/tez/conf_llap.dist

# tez conf
mkdir -p $OUT
pushd $OUT
ln -s /etc/tez/conf conf
ln -s /etc/tez/conf_llap conf_llap
popd;

# tez common jar
cp $DIST/*.jar $OUT
# tez lib
cp -r $DIST/lib $OUT
# empty tez/ui dir why!?!?
mkdir -p $OUT/ui
# tez plugins

# create a tar of tez full into $OUT/lib/tez.tar.gz
pushd $DIST/../tez-%tez_version
tar zcvf $OUT/lib/tez.tar.gz *
popd

%files
# default attribues
%defattr(0644, root, root, 0755)

# tez config
%dir %config(noreplace) %attr(0755, root, root) "%hdp/etc/tez/conf.dist"
%dir %config(noreplace) %attr(0755, root, root) "%hdp/etc/tez/conf_llap.dist"


# everything else
%attr(0755, root, root) "%hdp/tez/*"

%pre -p /bin/sh
%post -p /bin/sh
if [ !  -e "/etc/tez/conf" ]; then
    rm -f /etc/tez/conf
    mkdir -p /etc/tez/conf
fi
if [ !  -e "/etc/tez_llap/conf" ]; then
    rm -f /etc/tez_llap/conf
    mkdir -p /etc/tez_llap/conf
fi
#cp -rp  /usr/hdp/3.0.0.0-1064/etc/tez/conf.dist/* /etc/hdp/3.0.0.0-1064/tez
#alternatives --install /usr/hdp/3.0.0.0-1064/etc/tez/conf tez_3_0_0_0_1064-conf /usr/hdp/3.0.0.0-1064/etc/tez/conf.dist 30
%preun -p /bin/sh
#if [ "$1" = 0 ]; then
        #alternatives --remove tez_3_0_0_0_1064-conf /usr/hdp/3.0.0.0-1064/etc/tez/conf.dist || :
#fi

#######################
#### FILES SECTION ####
#######################
%changelog
