import sublime
import sublime_plugin

import re

from Anime.utils import *

anime_completions = []
friend_completions = []
def update_animes(view):
	global anime_completions
	animes = list_all_anime(view)

	anime_completions = [[a,a+':\n\n'] for a in animes]

def update_friends(view):
	global friend_completions
	friends = list_all_friends(view)

	friend_completions = [[f,f] for f in friends]
	pass

def is_in_friend_curly_brackets(view):
	typed_so_far = get_text_from_start_to_cursor(view)
	return None != re.match(r'^(?:(?!\})[^{\n])*\{(?:(?!\})[^{\n])*$', typed_so_far)


class AnimeEventListener(sublime_plugin.EventListener):

	def on_load_async(self, view):
		if is_anime(view):
			update_animes(view)
			update_friends(view)

	def on_post_save_async(self, view):
		if is_anime(view):
			update_animes(view)
			update_friends(view)

	def on_query_completions(self, view, prefix, locations):

		if not is_anime(view):
			return []
		selections = view.sel()
		if len(selections) != 1: 
			return []

		# Friends
		if is_in_friend_curly_brackets(view):
			return (friend_completions, sublime.INHIBIT_WORD_COMPLETIONS |
            sublime.INHIBIT_EXPLICIT_COMPLETIONS)

		return (anime_completions, sublime.INHIBIT_WORD_COMPLETIONS |
            sublime.INHIBIT_EXPLICIT_COMPLETIONS)

