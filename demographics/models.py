from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = '© Kariyushi Rao, 2018'

doc = """
Participants respond to basic demographics questions, self-report their relative knowledge of the stock
market and their gambling frequency, describe the strategy they used in the experiment, report whether
they find the stimuli suspicious, and provide open response comments about their experience.  
"""


class Constants(BaseConstants):
    name_in_url = 'last_page'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField()
    gender = models.IntegerField(
        choices=[[0, 'Male'],[1, 'Female'], [2, 'Other']],
        widget=widgets.RadioSelect
        )
    highest_degree = models.IntegerField(
        choices=[[1, 'No Degree'],[2, 'High School Diploma'], 
                [3, '2-Year College Degree or Skilled Trade Program'], [4, '4-year College Degree'],
                # NOTE: Masters + value was miscoded as 4 in "A" versions of the experiments.  
                # Error was fixed in "B" versions, but all Masters + responses were coded as "4"
                # in the analyses to allow for comparison between "A" and "B" experimental data.
                [5, 'Masters Degree or Higher']],
        widget=widgets.RadioSelect
        )
    stocks = models.IntegerField(
        choices=[[1, 'Better Than Average'],[0, 'About Average'], [-1, 'Worse Than Average']],
        widget=widgets.RadioSelect
        )
    gambling = models.IntegerField(
        choices=[[1, 'More Than Average'],[0, 'About Average'], [-1, 'Less Than Average']],
        widget=widgets.RadioSelect
        )
    strategy = models.TextField()
    suspicion = models.TextField()
    comments = models.TextField()
