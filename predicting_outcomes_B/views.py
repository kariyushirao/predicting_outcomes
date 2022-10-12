from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

author = '© Kariyushi Rao, 2018'

doc = """
Participants observe sequences of 8 signals from one of three different generators: analysts, stocks, or a bingo cage.  
Participants are asked to predict the identity of the next (9th) signal - either up/down (analyst, stocks) or red/blue (bingo cage).  
"""


class InstructionsBingo(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['treatment'] == 'bingo'

class InstructionsAnalyst(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['treatment'] == 'analyst'

class InstructionsStock(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['treatment'] == 'stock'        

class ComprehensionBingo(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['treatment'] == 'bingo'
        
    form_model = models.Player
    form_fields = ['comprehension1','comprehension2', 'comprehension3b', 'comprehension4b', 'comprehension5b']

    def error_message(self, values):
        numrounds = (values['comprehension1'] == 8)
        whatjudgment = (values['comprehension2'] == 2)
        whatround = (values['comprehension3b'] == 1)
        whatsequence = (values['comprehension4b'] == 2)
        whatcage= (values['comprehension5b'] == 3)
        if not (numrounds and whatjudgment and whatround and whatsequence and whatcage):
            return 'It looks like you may have answered one or more questions incorrectly. Please review your answers and correct any mistakes.'

class ComprehensionAnalyst(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['treatment'] == 'analyst'
        
    form_model = models.Player
    form_fields = ['comprehension1','comprehension2', 'comprehension3a', 'comprehension4a']

    def error_message(self, values):
        numrounds = (values['comprehension1'] == 8)
        whatjudgment = (values['comprehension2'] == 2)
        whatround = (values['comprehension3a'] == 1)
        whatsequence = (values['comprehension4a'] == 2)
        if not (numrounds and whatjudgment and whatround and whatsequence):
            return 'It looks like you may have answered one or more questions incorrectly. Please review your answers and correct any mistakes.'

class ComprehensionStock(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['treatment'] == 'stock'
        
    form_model = models.Player
    form_fields = ['comprehension1','comprehension2', 'comprehension3s', 'comprehension4s']

    def error_message(self, values):
        numrounds = (values['comprehension1'] == 8)
        whatjudgment = (values['comprehension2'] == 2)
        whatround = (values['comprehension3s'] == 1)
        whatsequence = (values['comprehension4s'] == 2)
        if not (numrounds and whatjudgment and whatround and whatsequence):
            return 'It looks like you may have answered one or more questions incorrectly. Please review your answers and correct any mistakes.'

class PredictBingo(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'bingo'

    form_model = models.Player
    form_fields = ['prediction_b']

    def vars_for_template(self):
        return {
			'image_path': 'predicting_outcomes_B/pictures/{}'.format(self.player.sequence_name)
        }

class PredictAnalyst(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'analyst'

    form_model = models.Player
    form_fields = ['prediction_as']

    def vars_for_template(self):
        return {
            'image_path': 'predicting_outcomes_B/pictures/{}'.format(self.player.sequence_name)
        }

class PredictStock(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'stock'

    form_model = models.Player
    form_fields = ['prediction_as']

    def vars_for_template(self):
        return {
            'image_path': 'predicting_outcomes_B/pictures/{}'.format(self.player.sequence_name)
        }

page_sequence = [
    InstructionsBingo,
    InstructionsAnalyst,
    InstructionsStock,
    ComprehensionBingo,
    ComprehensionAnalyst,
    ComprehensionStock,
    PredictBingo,
    PredictAnalyst,
    PredictStock
]
