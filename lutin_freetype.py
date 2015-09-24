#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "FreeType lib (generate font with true type file)"


def create(target):
	my_module = module.Module(__file__, 'freetype', 'LIBRARY')
	
	#remove compilation warning (specific for external libs):
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
		'freetype/pshinter/pshinter.c'])
	
	my_module.compile_flags('c', [
		'-W',
		'-Wall',
		'-DPIC',
		'-DDARWIN_NO_CARBON',
		'-DFT2_BUILD_LIBRARY',
		'-DANDROID_FONT_HACK=1'])
	
	my_module.add_export_path(tools.get_current_path(__file__))
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/internal")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/internal/services")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/psaux")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/pshinter")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/psnames")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/raster")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/sfnt")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/smooth")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/truetype")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/autofit")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/base")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/cff")
	my_module.add_path(tools.get_current_path(__file__)+"/freetype/config")
	
	my_module.compile_version_CC(1999)
	
	# add the currrent module at the 
	return my_module
	

