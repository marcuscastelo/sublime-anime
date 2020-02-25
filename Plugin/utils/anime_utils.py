import sublime
import datetime
import re

def is_anime(view):
	full_name = view.file_name()
	res = re.search(r'([^\/]+)$', full_name)
	return res and res.group(1) == 'animes.txt' or False



def get_cursor(view):
	return view.sel()[0].begin()

def is_cursor_at_first_word(view):
	selected_lines = view.lines(view.sel()[0])
	if len(selected_lines) != 1:
		return False #Multiple or 0 lines selected 

	line = selected_lines[0]

	typed_text = view.substr(line)
	if ' ' in typed_text: 
		return False

	return True

	def _get_raw_time():
	now_time = datetime.datetime.now().time()
	text = str(now_time)[0:5]
	return text

def get_time(isFirst):
	raw_time = _get_raw_time()
	return raw_time + (' - ' if isFirst else ' ')

def get_date(): 
	now = datetime.datetime.now()
	text = str(now.strftime("%d/%m/%Y"))
	return text

	import sublime
import datetime
import re

def is_anime(view):
	full_name = view.file_name()
	res = re.search(r'([^\/]+)$', full_name)
	return res and res.group(1) == 'animes.txt' or False



import re

def get_view_line(view):
	return view.lines(view.sel()[0])[0]

def get_previous_line(view, line):
	return view.lines(sublime.Region(line.a-1))[0]

def rewind_lines(view, line, amount):
	for i in range(amount):
		line = get_previous_line(view, line)
	return line