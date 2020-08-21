import sublime
import datetime
import re


### GENERIC CHECKS

def is_anime_list(view):
	full_name = view.file_name()

	if full_name == None: #in case no file is open
		return False 

	res = re.search(r'([^\/\\]+)$', full_name)
	return res and res.group(1) == 'anilist.anl' or False

### CURSOR UTILS

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


### DATETIME

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


## LINE SEARCHING

def sanitize_content(REGEX, anime_title):
	res = re.search(REGEX, anime_title)
	if res:
		return res.group(1)
	return None

class LineFinder:
	def __init__(self, view, start_line = None):
		if start_line == None:
			self.line = view.lines(view.sel()[0])[0]
		else:
			self.line = start_line

		self.view = view

	def get_current_line(self):
		return self.line

	def has_previous_line(self):
		return self.line.begin() != 0

	def get_previous_line(self):
		previous_end = self.line.begin()-1
		if previous_end < 0: 
			previous_end = 0
		return self.view.lines(sublime.Region(previous_end))[0]


	def get_line_content(self):
		return self.view.substr(self.line)

	def rewind(self):
		self.line = self.get_previous_line()

	def navigate(self, specs = []) -> bool:
		while True:
			if self.test_line(specs):
				return True

			if self.has_previous_line():
				self.rewind()
				continue

			return None

	def test_line(self, specs = []) -> bool:
		if len(specs) <= 0:
			return None
		
		content = self.get_line_content()
		failed_count = len(specs)
		for spec in specs:
			if spec['positive'] != (re.search(spec['regex'], content) == None):
				failed_count -= 1
		if failed_count == 0:
			return True
		return False


## linefinder_presets 

def find_closest_anime_title(view, finder = None, line = None):
		finder = finder or LineFinder(view, line)
		has_found = finder.navigate(
			[
				{
					'positive': False,
					'regex': r'^\s?$'
				},
				{
					'positive': False,
					'regex': r'\d{2}:\d{2}\s+\-\s+\d{2}:\d{2}.+'
				},
				{
					'positive': False,
					'regex': r'\d{2}/\d{2}/\d{4}'
				},
				{
					'positive': False,
					'regex': r'^\s?\[.+\]'
				},
		])
		if has_found:
			content = finder.get_line_content()
			anime_title = sanitize_content(r'^([^\/][^\/]?[^\n]*):', content)
			return anime_title
		else:
			return None

def find_last_episode(view, finder = None, line = None):
	finder = finder or LineFinder(view, line)
	has_found = finder.navigate(
		[
			{
				'positive': True,
				'regex': r'\d{2}:\d{2}\s+\-\s+\d{2}:\d{2}\s+\d{2,}'
			}
		]
	)
	if has_found:
		content = finder.get_line_content()
		episode_str = sanitize_content(r'\d{2}:\d{2}\s+\-\s+\d{2}:\d{2}\s+(\d{2,})', content)
		return episode_str
	return None


def list_all_anime(view):
	animes = set()
	finder = LineFinder(view)
	while finder.has_previous_line():
		anime_title = find_closest_anime_title(view, finder)
		if (anime_title == None):
			# print('NONE AT ', view.rowcol(finder.get_current_line().begin())[0])
			pass
		else:
			animes.add(anime_title)
		finder.rewind()
	return list(animes)

def list_all_friends(view):
	friends = set()
	finder = LineFinder(view)
	while finder.has_previous_line():
		friend_content = finder.get_line_content()
		regex_friend = re.search(r'\{([^}]+)\}', friend_content)
		if regex_friend:
			separated_by_commas = regex_friend.group(1)
			friend_names = separated_by_commas.split(', ')
			for name in friend_names:
				friends.add(name)
		finder.rewind()
	return list(friends)

def get_text_from_start_to_cursor(view):
	finder = LineFinder(view)
	line = finder.get_current_line()

	start = line.begin()
	cursor = view.sel()[0].begin()

	length = cursor-start
	content = finder.get_line_content()
	if len(content) > length:
		return content[0:length]
	else:
		return content
