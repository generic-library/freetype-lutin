#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools


def get_type():
	return "LIBRARY"

def get_desc():
	return "generate fonts with true type file"

def get_licence():
	return "FTL"
	"""
	"LGPL-3": {
		"generic":False,
		"contaminate-static":False,
		"contaminate-dynamic":False,
		"redistribute-source":False,
		"title":"FreeType License (BSD-like)",
		"licence-file":""
		},
	"""

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "freetype"

def get_maintainer():
	return ["Mailing-list Freetype <freetype-devel@nongnu.org>"]

def get_version():
	return [2,7,0]

def configure(target, my_module):
	my_module.remove_compile_warning()
	my_module.add_src_file([
	    'freetype/src/base/ftdebug.c',
	    'freetype/src/base/ftinit.c',
	    'freetype/src/base/ftbase.c',
	    'freetype/src/base/ftbbox.c',
	    'freetype/src/base/ftbdf.c',
	    'freetype/src/base/ftbitmap.c',
	    'freetype/src/base/ftcid.c',
	    'freetype/src/base/ftfntfmt.c',
	    'freetype/src/base/ftfstype.c',
	    'freetype/src/base/ftgasp.c',
	    'freetype/src/base/ftglyph.c',
	    'freetype/src/base/ftgxval.c',
	    'freetype/src/base/ftlcdfil.c',
	    'freetype/src/base/ftmm.c',
	    'freetype/src/base/ftotval.c',
	    'freetype/src/base/ftpatent.c',
	    'freetype/src/base/ftpfr.c',
	    'freetype/src/base/ftstroke.c',
	    'freetype/src/base/ftsynth.c',
	    'freetype/src/base/fttype1.c',
	    'freetype/src/base/ftwinfnt.c',
	    'freetype/src/truetype/truetype.c',
	    'freetype/src/type1/type1.c',
	    'freetype/src/cff/cff.c',
	    'freetype/src/cid/type1cid.c',
	    'freetype/src/pfr/pfr.c',
	    'freetype/src/type42/type42.c',
	    'freetype/src/winfonts/winfnt.c',
	    'freetype/src/pcf/pcf.c',
	    'freetype/src/bdf/bdf.c',
	    'freetype/src/sfnt/sfnt.c',
	    'freetype/src/autofit/autofit.c',
	    'freetype/src/pshinter/pshinter.c',
	    'freetype/src/raster/raster.c',
	    'freetype/src/smooth/smooth.c',
	    'freetype/src/cache/ftcache.c',
	    'freetype/src/gzip/ftgzip.c',
	    'freetype/src/lzw/ftlzw.c',
	    'freetype/src/bzip2/ftbzip2.c',
	    'freetype/src/psaux/psaux.c',
	    'freetype/src/psnames/psnames.c',
	    'freetype/src/tools/apinames.c'
	    ])
	my_module.add_header_path('freetype/include/', regex='*.h', recursive=True)
	my_module.add_flag('c', [
		'-W',
		'-Wall',
		'-pedantic',
		'-ansi',
		'-DPIC',
		'-DDARWIN_NO_CARBON',
		'-DFT2_BUILD_LIBRARY',
		'-DANDROID_FONT_HACK=1',
		'-DFT_CONFIG_OPTION_SYSTEM_ZLIB',
		#'-DFT_CONFIG_OPTION_USE_PNG',
		'-DFT_CONFIG_CONFIG_H="<include/freetype/config/ftconfig.h>"',
		'-DFT_CONFIG_MODULES_H="<include/freetype/config/ftmodule.h>"',
		'-Wno-extended-offsetof'
		])
	my_module.add_path("freetype/")
	my_module.add_path("freetype/src/")
	my_module.compile_version("c", 1999)
	my_module.add_depend([
	    'c',
	    'z',
	    #'png'
	    ])
	if    "Linux" in target.get_type() \
	   or "Android" in target.get_type():
		my_module.add_path("freetype/builds/unix")
		my_module.add_path("freetype/include/freetype/config/")
		my_module.add_src_file('freetype/builds/unix/ftsystem.c')
		my_module.add_flag('c', [
		    '-DHAVE_UNISTD_H=1',
		    '-DHAVE_FCNTL_H=1',
		    '-DHAVE_STDINT_H=1',
		    ])
	elif    "MacOs" in target.get_type() \
	     or "IOs" in target.get_type():
		my_module.add_path("freetype/builds/mac")
		my_module.add_path("freetype/include/freetype/config/")
		my_module.add_src_file('freetype/builds/mac/ftmac.c')
	elif    "Windows" in target.get_type():
		my_module.add_path("freetype/builds/unix")
		my_module.add_src_file('freetype/builds/unix/ftsystem.c')
		my_module.add_path("freetype/include/freetype/config/")
		my_module.add_flag('c', [
		    '-DHAVE_UNISTD_H=1',
		    '-DHAVE_FCNTL_H=1',
		    '-DHAVE_STDINT_H=1',
		    ])
	
	
	return True
"""
 -Iobjs -I./builds/unix -Iinclude 
 -DFT_CONFIG_OPTION_USE_BZIP2
 -I/usr/include/harfbuzz
 -I/usr/include/glib-2.0
 -I/usr/lib/glib-2.0/include
 -DFT_CONFIG_OPTION_USE_HARFBUZZ
 -DFT_CONFIG_CONFIG_H="<ftconfig.h>"
 
 -DFT_CONFIG_MODULES_H="<ftmodule.h>"
 -o objs/ftsystem.lo 
"""