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
	return [2,3,6]

def configure(target, my_module):
	my_module.remove_compile_warning()
	my_module.add_src_file([
		'freetype/base/ftbbox.c',
		'freetype/base/ftbitmap.c',
		'freetype/base/ftglyph.c',
		'freetype/base/ftstroke.c',
		'freetype/base/ftxf86.c',
		'freetype/base/ftbase.c',
		'freetype/base/ftsystem.c',
		'freetype/base/ftinit.c',
		'freetype/base/ftgasp.c',
		'freetype/base/ftadvanc.c',
		'freetype/raster/raster.c',
		'freetype/sfnt/sfnt.c',
		'freetype/smooth/smooth.c',
		'freetype/autofit/autofit.c',
		'freetype/truetype/truetype.c',
		'freetype/cff/cff.c',
		'freetype/psnames/psnames.c',
		'freetype/pshinter/pshinter.c'
		])
	my_module.add_header_file([
		'freetype/ftgzip.h',
		'freetype/ftxf86.h',
		'freetype/ftlist.h',
		'freetype/fterrdef.h',
		'freetype/ft2unix.h',
		'freetype/ftoutln.h',
		'freetype/ftsnames.h',
		'freetype/ftmm.h',
		'freetype/ftmoderr.h',
		'freetype/ftchapters.h',
		'freetype/ftgasp.h',
		'freetype/ftlzw.h',
		'freetype/fterrors.h',
		'freetype/ftsystem.h',
		'freetype/ftwinfnt.h',
		'freetype/ftimage.h',
		'freetype/t1tables.h',
		'freetype/fttypes.h',
		'freetype/ftotval.h',
		'freetype/ttnameid.h',
		'freetype/ft2build.h',
		'freetype/ftglyph.h',
		'freetype/ftbbox.h',
		'freetype/ttunpat.h',
		'freetype/tttags.h',
		'freetype/ftcache.h',
		'freetype/ftbdf.h',
		'freetype/ftpfr.h',
		'freetype/ftlcdfil.h',
		'freetype/ftmac.h',
		'freetype/ftsizes.h',
		'freetype/ftcid.h',
		'freetype/ftstroke.h',
		'freetype/ftmodapi.h',
		'freetype/tttables.h',
		'freetype/ftsynth.h',
		'freetype/ftrender.h',
		'freetype/ftgxval.h',
		'freetype/freetype.h',
		'freetype/ftbitmap.h',
		'freetype/ftadvanc.h',
		'freetype/fttrigon.h',
		'freetype/ftincrem.h',
		'freetype/config/ftstdlib.h',
		'freetype/config/ftheader.h',
		'freetype/config/ftmodule.h',
		'freetype/config/ftconfig.h',
		'freetype/config/ftoption.h',
		])
	my_module.add_flag('c', [
		'-W',
		'-Wall',
		'-DPIC',
		'-DDARWIN_NO_CARBON',
		'-DFT2_BUILD_LIBRARY',
		'-DANDROID_FONT_HACK=1'])
	my_module.add_path(".")
	my_module.add_path("freetype/")
	my_module.add_path("freetype/internal")
	my_module.add_path("freetype/internal/services")
	my_module.add_path("freetype/psaux")
	my_module.add_path("freetype/pshinter")
	my_module.add_path("freetype/psnames")
	my_module.add_path("freetype/raster")
	my_module.add_path("freetype/sfnt")
	my_module.add_path("freetype/smooth")
	my_module.add_path("freetype/truetype")
	my_module.add_path("freetype/autofit")
	my_module.add_path("freetype/base")
	my_module.add_path("freetype/cff")
	my_module.add_path("freetype/config")
	my_module.compile_version("c", 1999)
	my_module.add_depend([
	    'c'
	    ])
	return True

