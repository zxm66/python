function AsyncCompileOrRunCallback(channel,msg)
	echomsg a:msg
endfunction
let g:compile = ''
let g:file = ''
function SetCompileAndFile()
	if &filetype == 'c'
		set compile = 'gcc'
	elseif &filetype == 'java'
		set compile = 'javac'
	endif
endfunction

function AsyncCompileOrRun()
	call jobstart(['python3','src/python_data_analysis/python_dash2.py'],{'callback':'AsyncCompileOrRunCallback'})
endfunction

" 可以看出来的的是 let processnumber = jobstart(['python3','app.py']),
" call jobstop(processnumber),nvim 支持进程之间的通信。还有一个问题是。jobstop
" 传递的参数是nvim自己生成的，而不是系统的进程号。所以使用jobstop应该是不能停止系统的进程的。
" makedownpreview这个插件是可以异步查看的，所以一定是使用异步机制的。

