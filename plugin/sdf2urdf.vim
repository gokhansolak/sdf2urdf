" Check built in python3
if !has('python3')
	finish
endif

let s:path = expand('<sfile>:p:h')

command! S2u call sdf2urdf#SdfToUrdf( s:path )

