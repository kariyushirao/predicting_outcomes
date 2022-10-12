from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import csv
import itertools

author = '© Kariyushi Rao, 2018'

doc = """
Participants respond to three questions testing knowledge of probability, and two questions
testing financial literacy.  
"""


class Constants(BaseConstants):
	name_in_url = 'wrapup_qs'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	def creating_session(self):
		# The "treatments" in this app represent different orderings of the five questions.
		# This is not the most efficient method for randomizing the order of the questions
		# across participants, but was selected in order to accommodate other constraints.
		num_treatments = itertools.cycle(['QV1', 'QV2', 'QV3', 'QV4'])

		# Assigns treatment (question ordering) at the participant level
		if self.round_number == 1:
			for p in self.get_players():
				treatment_num = next(num_treatments)
				p.participant.vars['treatment_num'] = treatment_num
				p.treatment_num = treatment_num
		else:
			for p in self.get_players():
				treatment_num = p.participant.vars['treatment_num']
				p.treatment_num = treatment_num

class Group(BaseGroup):
	pass


class Player(BasePlayer):
	treatment_num = models.TextField()
	
	numeracy1 = models.CharField()
	numeracy2 = models.CharField()
	numeracy3 = models.CharField()

	financial1 = models.IntegerField(
		choices=[[1, 'Less than 2 years'],[2, 'At least 2 years but less than 5 years'], 
				[3, 'At least 5 years but less than 10 years'], [4, 'At least 10 years']],
		widget=widgets.RadioSelect
		)
	financial2 = models.IntegerField(
		choices=[[1, 'more safe than'],[2, 'the same as'], [3, 'less safe than']],
		widget=widgets.RadioSelect
		)

