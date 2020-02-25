import sublime
import sublime_plugin

from Anime.utils import *

class AnimeTitleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		anime_title = find_closest_anime_title(self.view)
		self.view.insert(edit, get_cursor(self.view), anime_title)

