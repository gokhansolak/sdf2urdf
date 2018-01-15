" Check built in python3
if !has('python3')
	finish
endif

let s:path = expand('<sfile>:p:h')

function! PoseToOrigin()
	py3file pose2origin.py
endfunc

function! ChildToAttrib()
	py3file child2attrib.py
endfunc

function! SdfToUrdf()
	py3file sdf2urdf.py
endfunc

command! S2up call PoseToOrigin()

command! S2uc call ChildToAttrib()

command! S2u call SdfToUrdf()

