import sublime
import sublime_plugin

from Anime.utils import get_cursor, is_cursor_at_first_word, get_time

class AnimeTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		text = get_time(is_cursor_at_first_word(self.view))
		self.view.insert(edit, get_cursor(self.view), text)

