from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

author = '© Kariyushi Rao, 2018'

doc = """
Participants respond to three questions testing knowledge of probability, and two questions
testing financial literacy.  
"""

 
class QuestionV1(Page):
	form_model = models.Player
	form_fields = ['numeracy1', 'numeracy2', 'numeracy3', 'financial1', 'financial2']

	def is_displayed(self):
		return self.participant.vars['treatment_num'] == 'QV1'

class QuestionV2(Page):
	form_model = models.Player
	form_fields = ['numeracy1', 'numeracy2', 'numeracy3', 'financial1', 'financial2']

	def is_displayed(self):
		return self.participant.vars['treatment_num'] == 'QV2'

class QuestionV3(Page):
	form_model = models.Player
	form_fields = ['numeracy1', 'numeracy2', 'numeracy3', 'financial1', 'financial2']

	def is_displayed(self):
		return self.participant.vars['treatment_num'] == 'QV3'

class QuestionV4(Page):
	form_model = models.Player
	form_fields = ['numeracy1', 'numeracy2', 'numeracy3', 'financial1', 'financial2']

	def is_displayed(self):
		return self.participant.vars['treatment_num'] == 'QV4'        

page_sequence = [
	QuestionV1,
	QuestionV2,
	QuestionV3,
	QuestionV4,
]
