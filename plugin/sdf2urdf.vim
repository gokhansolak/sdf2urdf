" Check built in python3
if !has('python3')
	finish
endif

let s:path = expand('<sfile>:p:h')

function! SdfToUrdf()
	py3file sdf2urdf.py
endfunc

"TODO: implement autoload
command! S2u call SdfToUrdf()

