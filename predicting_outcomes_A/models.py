from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)

import random
import itertools

author = '© Kariyushi Rao, 2018'

doc = """
Participants observe sequences of 8 signals from one of three different generators: analysts, stocks, or a bingo cage.  
Participants are asked to predict the likelihood that the next (9th) signal will be up (analyst, stocks) or red (bingo cage).  
"""


class Constants(BaseConstants):
	name_in_url = 'predicting_outcomes_A'
	players_per_group = None
	num_rounds = 18

	# bingo cage stimuli
	bingos = {1: {'file': 'B21_BRBBRBRR.gif'}, 2: {'file': 'B22_RBRRBRBB.gif'}, 3: {'file': 'B23_BRBRBRBB.gif'}, 4: {'file': 'B24_RBRBRBRR.gif'}, 
			5: {'file': 'B31_BRBRBRRR.gif'}, 6: {'file': 'B32_RBRBRBBB.gif'}, 7: {'file': 'B33_BRBRRBBB.gif'}, 8: {'file': 'B34_RBRBBRRR.gif'}, 
			9: {'file': 'B41_BBRBRRRR.gif'}, 10: {'file': 'B42_RRBRBBBB.gif'}, 11: {'file': 'B43_BRBRBBBB.gif'}, 12: {'file': 'B44_RBRBRRRR.gif'}, 
			13: {'file': 'B51_BBRBBBBB.gif'}, 14: {'file': 'B52_RRBRRRRR.gif'}, 15: {'file': 'B53_BRBRRRRR.gif'}, 16: {'file': 'B54_RBRBBBBB.gif'}, 
			17: {'file': 'B61_BRBBBBBB.gif'}, 18: {'file': 'B62_RBRRRRRR.gif'}, 19: {'file': 'B63_RRBBBBBB.gif'}, 20: {'file': 'B64_BBRRRRRR.gif'}, 
			21: {'file': 'B71_BRRRRRRR.gif'}, 22: {'file': 'B72_RBBBBBBB.gif'}, 23: {'file': 'B11_RBRBRBRB.gif'}, 24: {'file': 'B12_BRBRBRBR.gif'}, 
			25: {'file': 'B13_BRBRBBRB.gif'}, 26: {'file': 'B14_BRRBRBRB.gif'}, 27: {'file': 'B15_BBRRBRBR.gif'}, 28: {'file': 'B16_BBRRBRRB.gif'}, 
			29: {'file': 'B17_RBRBBRRB.gif'}, 30: {'file': 'B18_RRBBRRBR.gif'}, 31: {'file': 'B19_RRBRRBBR.gif'}, 32: {'file': 'B110_RRBRBBRB.gif'}, 
			33: {'file': 'B111_BRBRRRBR.gif'}, 34: {'file': 'B112_BRBBBRBR.gif'}, 35: {'file': 'B113_BRRRBBRB.gif'}, 36: {'file': 'B114_RRRBRBRB.gif'}, 
			37: {'file': 'B115_RBBBRBRB.gif'}, 38: {'file': 'B116_RRBBBRRB.gif'}, 39: {'file': 'B117_BBBBRRBR.gif'}, 40: {'file': 'B118_BRBRRRRB.gif'}, 
			41: {'file': 'B119_RBBBBRBR.gif'}, 42: {'file': 'B120_RRRRBBRB.gif'}, 43: {'file': 'B121_BRBBBBBR.gif'}, 44: {'file': 'B122_RRRRRBRB.gif'}, 
			45: {'file': 'B123_RBBBBBBR.gif'}, 46: {'file': 'B124_RRRRRRBR.gif'}
			}

	# analyst stimuli
	analysts = {1: {'file': 'A21_DUDDUDUU.gif'}, 2: {'file': 'A22_UDUUDUDD.gif'}, 3: {'file': 'A23_DUDUDUDD.gif'}, 4: {'file': 'A24_UDUDUDUU.gif'}, 
			5: {'file': 'A31_DUDUDUUU.gif'}, 6: {'file': 'A32_UDUDUDDD.gif'}, 7: {'file': 'A33_DUDUUDDD.gif'}, 8: {'file': 'A34_UDUDDUUU.gif'}, 
			9: {'file': 'A41_DDUDUUUU.gif'}, 10: {'file': 'A42_UUDUDDDD.gif'}, 11: {'file': 'A43_DUDUDDDD.gif'}, 12: {'file': 'A44_UDUDUUUU.gif'}, 
			13: {'file': 'A51_DDUDDDDD.gif'}, 14: {'file': 'A52_UUDUUUUU.gif'}, 15: {'file': 'A53_DUDUUUUU.gif'}, 16: {'file': 'A54_UDUDDDDD.gif'}, 
			17: {'file': 'A61_DUDDDDDD.gif'}, 18: {'file': 'A62_UDUUUUUU.gif'}, 19: {'file': 'A63_UUDDDDDD.gif'}, 20: {'file': 'A64_DDUUUUUU.gif'}, 
			21: {'file': 'A71_DUUUUUUU.gif'}, 22: {'file': 'A72_UDDDDDDD.gif'}, 23: {'file': 'A11_UDUDUDUD.gif'}, 24: {'file': 'A12_DUDUDUDU.gif'}, 
			25: {'file': 'A13_DUDUDDUD.gif'}, 26: {'file': 'A14_DUUDUDUD.gif'}, 27: {'file': 'A15_DDUUDUDU.gif'}, 28: {'file': 'A16_DDUUDUUD.gif'}, 
			29: {'file': 'A17_UDUDDUUD.gif'}, 30: {'file': 'A18_UUDDUUDU.gif'}, 31: {'file': 'A19_UUDUUDDU.gif'}, 32: {'file': 'A110_UUDUDDUD.gif'}, 
			33: {'file': 'A111_DUDUUUDU.gif'}, 34: {'file': 'A112_DUDDDUDU.gif'}, 35: {'file': 'A113_DUUUDDUD.gif'}, 36: {'file': 'A114_UUUDUDUD.gif'}, 
			37: {'file': 'A115_UDDDUDUD.gif'}, 38: {'file': 'A116_UUDDDUUD.gif'}, 39: {'file': 'A117_DDDDUUDU.gif'}, 40: {'file': 'A118_DUDUUUUD.gif'}, 
			41: {'file': 'A119_UDDDDUDU.gif'}, 42: {'file': 'A120_UUUUDDUD.gif'}, 43: {'file': 'A121_DUDDDDDU.gif'}, 44: {'file': 'A122_UUUUUDUD.gif'}, 
			45: {'file': 'A123_UDDDDDDU.gif'}, 46: {'file': 'A124_UUUUUUDU.gif'}
			}

	# stock stimuli
	stocks = {1: {'file': 'S21_DUDDUDUU.gif'}, 2: {'file': 'S22_UDUUDUDD.gif'}, 3: {'file': 'S23_DUDUDUDD.gif'}, 4: {'file': 'S24_UDUDUDUU.gif'}, 
			5: {'file': 'S31_DUDUDUUU.gif'}, 6: {'file': 'S32_UDUDUDDD.gif'}, 7: {'file': 'S33_DUDUUDDD.gif'}, 8: {'file': 'S34_UDUDDUUU.gif'}, 
			9: {'file': 'S41_DDUDUUUU.gif'}, 10: {'file': 'S42_UUDUDDDD.gif'}, 11: {'file': 'S43_DUDUDDDD.gif'}, 12: {'file': 'S44_UDUDUUUU.gif'}, 
			13: {'file': 'S51_DDUDDDDD.gif'}, 14: {'file': 'S52_UUDUUUUU.gif'}, 15: {'file': 'S53_DUDUUUUU.gif'}, 16: {'file': 'S54_UDUDDDDD.gif'}, 
			17: {'file': 'S61_DUDDDDDD.gif'}, 18: {'file': 'S62_UDUUUUUU.gif'}, 19: {'file': 'S63_UUDDDDDD.gif'}, 20: {'file': 'S64_DDUUUUUU.gif'}, 
			21: {'file': 'S71_DUUUUUUU.gif'}, 22: {'file': 'S72_UDDDDDDD.gif'}, 23: {'file': 'S11_UDUDUDUD.gif'}, 24: {'file': 'S12_DUDUDUDU.gif'}, 
			25: {'file': 'S13_DUDUDDUD.gif'}, 26: {'file': 'S14_DUUDUDUD.gif'}, 27: {'file': 'S15_DDUUDUDU.gif'}, 28: {'file': 'S16_DDUUDUUD.gif'}, 
			29: {'file': 'S17_UDUDDUUD.gif'}, 30: {'file': 'S18_UUDDUUDU.gif'}, 31: {'file': 'S19_UUDUUDDU.gif'}, 32: {'file': 'S110_UUDUDDUD.gif'}, 
			33: {'file': 'S111_DUDUUUDU.gif'}, 34: {'file': 'S112_DUDDDUDU.gif'}, 35: {'file': 'S113_DUUUDDUD.gif'}, 36: {'file': 'S114_UUUDUDUD.gif'}, 
			37: {'file': 'S115_UDDDUDUD.gif'}, 38: {'file': 'S116_UUDDDUUD.gif'}, 39: {'file': 'S117_DDDDUUDU.gif'}, 40: {'file': 'S118_DUDUUUUD.gif'}, 
			41: {'file': 'S119_UDDDDUDU.gif'}, 42: {'file': 'S120_UUUUDDUD.gif'}, 43: {'file': 'S121_DUDDDDDU.gif'}, 44: {'file': 'S122_UUUUUDUD.gif'}, 
			45: {'file': 'S123_UDDDDDDU.gif'}, 46: {'file': 'S124_UUUUUUDU.gif'}
			}


class Subsession(BaseSubsession):
	def creating_session(self):
		treatments = itertools.cycle(['bingo', 'analyst', 'stock'])

		# assigns treatment at the participant level so that same treatment
		# persists across rounds
		if self.round_number == 1:
			for p in self.get_players():
				if 'treatment' in self.session.config:
					# demo mode
					treatment = self.session.config['treatment']
					p.participant.vars['treatment'] = treatment
					p.treatment = treatment
				else: 
					# live experiment mode
					treatment = next(treatments)
					p.participant.vars['treatment'] = treatment
					p.treatment = treatment
		else:
			for p in self.get_players():
				treatment = p.participant.vars['treatment']
				p.treatment = treatment


		image_index = self.round_number - 1

		if self.round_number == 1:
			for p in self.get_players():
				# these are placeholders for dictionary keys {} we pull out of the dictionaries above, 
				# and then convert to lists [] of key values to control randomization of stimuli
				two_streak = {}
				two_keys = []
				three_streak = {}
				three_keys = []
				four_streak = {}
				four_keys = []
				five_streak = {}
				five_keys = []
				six_streak = {}
				six_keys = []
				seven_streak = {}
				seven_keys = []
				filler_streak = {}

				# copy in the stimuli and construct key lists
				if p.treatment == 'bingo':
					bingos = Constants.bingos.copy()
					two_streak = {key:bingos[key] for key in [1, 2, 3, 4]}
					two_keys = list(two_streak.keys())
					three_streak = {key:bingos[key] for key in [5, 6, 7, 8]}
					three_keys = list(three_streak.keys())
					four_streak = {key:bingos[key] for key in [9, 10, 11, 12]}
					four_keys = list(four_streak.keys())
					five_streak = {key:bingos[key] for key in [13, 14, 15, 16]}
					five_keys = list(five_streak.keys())
					six_streak = {key:bingos[key] for key in [17, 18, 19, 20]}
					six_keys = list(six_streak.keys())
					seven_streak = {key:bingos[key] for key in [21, 22]}
					seven_keys = list(seven_streak.keys())
					filler_streak = {key:bingos[key] for key in [23, 24, 25, 26, 27, 28, 29, 30, 31, 
																32, 33, 34, 35, 36, 37, 38, 39, 40,
																41, 42, 43, 44, 45, 46]}
				elif p.treatment == 'analyst':
					analysts = Constants.analysts.copy()
					two_streak = {key:analysts[key] for key in [1, 2, 3, 4]}
					two_keys = list(two_streak.keys())
					three_streak = {key:analysts[key] for key in [5, 6, 7, 8]}
					three_keys = list(three_streak.keys())
					four_streak = {key:analysts[key] for key in [9, 10, 11, 12]}
					four_keys = list(four_streak.keys())
					five_streak = {key:analysts[key] for key in [13, 14, 15, 16]}
					five_keys = list(five_streak.keys())
					six_streak = {key:analysts[key] for key in [17, 18, 19, 20]}
					six_keys = list(six_streak.keys())
					seven_streak = {key:analysts[key] for key in [21, 22]}
					seven_keys = list(seven_streak.keys())
					filler_streak = {key:analysts[key] for key in [23, 24, 25, 26, 27, 28, 29, 30, 31, 
																32, 33, 34, 35, 36, 37, 38, 39, 40,
																41, 42, 43, 44, 45, 46]}
				else: 
					stocks = Constants.stocks.copy()
					two_streak = {key:stocks[key] for key in [1, 2, 3, 4]}
					two_keys = list(two_streak.keys())
					three_streak = {key:stocks[key] for key in [5, 6, 7, 8]}
					three_keys = list(three_streak.keys())
					four_streak = {key:stocks[key] for key in [9, 10, 11, 12]}
					four_keys = list(four_streak.keys())
					five_streak = {key:stocks[key] for key in [13, 14, 15, 16]}
					five_keys = list(five_streak.keys())
					six_streak = {key:stocks[key] for key in [17, 18, 19, 20]}
					six_keys = list(six_streak.keys())
					seven_streak = {key:stocks[key] for key in [21, 22]}
					seven_keys = list(seven_streak.keys())
					filler_streak = {key:stocks[key] for key in [23, 24, 25, 26, 27, 28, 29, 30, 31, 
																32, 33, 34, 35, 36, 37, 38, 39, 40,
																41, 42, 43, 44, 45, 46]}

				# this section picks 1) one opening sequence, 2) one stimulus from each set of sequences
				# having terminal streaks of lengths 2-7, 3) and 12 filler sequences that end in reversal
				random.shuffle(two_keys)
				two_key = two_keys[0]
				two_sequence = two_streak[two_key]['file'] 

				random.shuffle(three_keys)
				three_key = three_keys[0]
				three_sequence = three_streak[three_key]['file']

				random.shuffle(four_keys)
				four_key = four_keys[0]
				four_sequence = four_streak[four_key]['file']

				random.shuffle(five_keys)
				five_key = five_keys[0]
				five_sequence = five_streak[five_key]['file']

				random.shuffle(six_keys)
				six_key = six_keys[0]
				six_sequence = six_streak[six_key]['file']

				random.shuffle(seven_keys)
				seven_key = seven_keys[0]
				seven_sequence = seven_streak[seven_key]['file']

				# pull objects out of fillers list
				fillers = []
				fillers.extend((filler_streak[23]['file'], filler_streak[24]['file'], filler_streak[25]['file'], 
					filler_streak[26]['file'], filler_streak[27]['file'], filler_streak[28]['file'], filler_streak[29]['file'],
					filler_streak[30]['file'], filler_streak[31]['file'], filler_streak[32]['file'], filler_streak[33]['file'],
					filler_streak[34]['file'], filler_streak[35]['file'], filler_streak[36]['file'], filler_streak[37]['file'],
					filler_streak[38]['file'], filler_streak[39]['file'], filler_streak[40]['file'], filler_streak[41]['file'],
					filler_streak[42]['file'], filler_streak[43]['file'], filler_streak[44]['file'], filler_streak[45]['file'],
					filler_streak[46]['file']))

				# shuffle filler sequences and select training sequence plus 11 other fillers to mix with targets 
				random.shuffle(fillers)
				training_sequence = fillers[0]
				eleven_fillers = fillers[1:12]

				# append targets to list of 11 fillers
				all_sequences = eleven_fillers
				all_sequences.extend((two_sequence, three_sequence, four_sequence, five_sequence, six_sequence, seven_sequence))

				# shuffle targets and fillers
				random.shuffle(all_sequences)

				# add training sequence to start of list
				all_sequences.insert(0, training_sequence)

				p.participant.vars['all_sequences'] = all_sequences
				stimuli_list = p.participant.vars['all_sequences']
				p.sequence_name = stimuli_list[image_index]
		else:
			for p in self.get_players():
				stimuli_list = p.participant.vars['all_sequences']
				p.sequence_name = stimuli_list[image_index]

class Group(BaseGroup):
	pass


class Player(BasePlayer):
	comprehension1 = models.IntegerField(
		choices=[8, 9, 5],
		widget=widgets.RadioSelect
		)
	comprehension2 = models.IntegerField(
		choices=[[1, 'Identify the first outcome in the sequence.'], 
				[2, 'Predict the next outcome in the sequence.'],
				[3, 'Describe what the sequence looks like.']],
		widget=widgets.RadioSelect
		)
	# bingo questions
	comprehension3b = models.IntegerField(
		choices=[[1, 'Each round I will see a new sequence of 8 draws made by a mechanical bingo machine.'],
				[2, 'Each round I will see a continuation of the draws made by the mechanical bingo machine last round.'],
				[3, 'Each round I will see a sequence of draws made by several different mechanical bingo machines.']],
		widget=widgets.RadioSelect
		)
	comprehension4b = models.IntegerField(
		choices=[[1, 'Each sequence shows the outcomes of 8 draws made by 8 different mechanical bingo machines.'], 
				[2, 'Each sequence shows the outcomes of 8 consecutive draws made by 1 mechanical bingo machine.'],
				[3, 'Each sequence shows a sample of various draws made by 1 mechanical bingo machine across a number of rounds.']],
		widget=widgets.RadioSelect
		)
	# analyst questions
	comprehension3a = models.IntegerField(
		choices=[[1, 'Each round I will see a sequence from a different analyst than the round before.'], 
				[2, 'Each round I will see a sequence from the same analyst as the round before.'],
				[3, 'Each round I will see a sequence from several analysts at the same time.']],
		widget=widgets.RadioSelect
		)
	comprehension4a = models.IntegerField(
		choices=[[1, 'Each sequence shows the outcomes from 8 quarters for 8 different analysts.'], 
				[2, 'Each sequence shows the outcomes from 8 consecutive quarters for 1 analyst.'],
				[3, 'Each sequence shows a sample of 8 outcomes from various times over the career of 1 analyst.']],
		widget=widgets.RadioSelect
		)
	# stock questions
	comprehension3s = models.IntegerField(
		choices=[[1, 'Each round I will see a new sequence from a different company than the round before.'], 
				[2, 'Each round I will see a sequence from the same company as the round before.'],
				[3, 'Each round I will see a sequence from several different companies at the same time.']],
		widget=widgets.RadioSelect
		)
	comprehension4s = models.IntegerField(
		choices=[[1, 'Each sequence shows the outcomes from 8 quarters for 8 different companies.'], 
				[2, 'Each sequence shows the outcomes from 8 consecutive quarters for 1 company.'],
				[3, 'Each sequence shows a sample of 8 outcomes from various times over the history of 1 company.']],
		widget=widgets.RadioSelect
		)

	treatment = models.CharField()
	prediction = models.IntegerField(
		widget=widgets.Slider(attrs={'step': '1.00'},
			show_value=False))
	sequence_name = models.CharField()

