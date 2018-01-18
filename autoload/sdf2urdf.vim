
function! sdf2urdf#SdfToUrdf(path)
	echom a:path

	execute "py3file " . a:path . '/sdf2urdf.py'

endfunction

