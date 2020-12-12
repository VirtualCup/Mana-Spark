from StringHelper import StringHelper;
from UnityTMProFont import UnityTMProFont;

import os, sys;

reload(sys);
sys.setdefaultencoding('utf8');

txtFiles = [
    "ManaSpark/StreamingAssets/Localization/messages_en.bytes"
];

def gen_fon():
	sh = StringHelper();
	for path in txtFiles:
		sh.add_file_text(path);
	sh.add_western();

	f = open("Font/textmin.txt", "wb");
	f.write(sh.get_chars().decode("utf-8").encode("utf-8-sig"));
	f.close();

	"""
	# Can't add " ", make sure the path have no space.
	bmfc_filepath = "Font/Font Atlas-sharedassets0.assets-40612.bmfc";
	output_filepath = "Font/Font Atlas-sharedassets0.assets-40612.fnt";

	bmfont_tool_path = "E:\\BMFont\\bmfont.com";
	text_file_path = "\"Font\\textmin.txt\"";
	bmfc_filepath = "\"" + bmfc_filepath.replace("/", "\\") + "\"";
	output_filepath = "\"" + output_filepath.replace("/", "\\") + "\"";
	
	commandstr = " ".join((bmfont_tool_path , "-c" ,bmfc_filepath, "-o", output_filepath, "-t" ,text_file_path));
	os.system(commandstr.encode('mbcs'));
	"""
	
	fon = UnityTMProFont("OriginalFile/unnamed asset-sharedassets0.assets-40612.dat", version = 17, font_version=[1, 0, 55]);
	fon.read_from_bmfont("Font/Font SDF-sharedassets0.assets-40612.fnt");
	fon.save_to_raw("ManaSpark/unnamed asset-sharedassets0.assets-40612.dat");

gen_fon();