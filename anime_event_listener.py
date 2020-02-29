import sublime
import sublime_plugin

from Anime.utils import is_cursor_at_first_word, list_all_anime, is_anime, get_time

completions = []
def update_animes(view):
	global completions
	animes = list_all_anime(view)

	completions = [[a,a+':\n\n'] for a in animes]

def add_current_time(view):
	currTime = get_time(False)
	textTime = get_time(is_cursor_at_first_word(view))
	completions.append([currTime, textTime])


class AnimeEventListener(sublime_plugin.EventListener):

	def on_load_async(self, view):
		if is_anime(view):
			update_animes(view)

	def on_post_save_async(self, view):
		if is_anime(view):
			update_animes(view)

	def on_query_completions(self, view, prefix, locations):
		if not is_anime(view):
			return []

		selections = view.sel()
		if len(selections) != 1: 
			return []

		add_current_time(view)

		return (completions, sublime.INHIBIT_WORD_COMPLETIONS |
            sublime.INHIBIT_EXPLICIT_COMPLETIONS)
