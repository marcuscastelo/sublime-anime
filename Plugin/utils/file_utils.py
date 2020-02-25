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