import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True


# don't share this with anybody.
SECRET_KEY = ''


DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# sentry account
SENTRY_DSN = ''

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = ''

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    The following are simplified versions of the experimental procedures 
    used in Studies 1A and 1B of "Predicting outcomes in binary sequences:  
    belief updating and gamblers fallacy reasoning."
</p>
"""

ROOMS = [
    {
        'name': 'WebLab',
        'display_name': 'Web Lab',
        # 'participant_label_file': '_rooms/room101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]


# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'brief', 'short', 'experiment', 'game', 'predictions', 'academic'],
    'title': '20-minute experiment about predictions',
    'description': 'A quick experiment about predictions. Less than 20 minutes to complete.',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 0.5*24, # 12 hours 
    # flag workers once they've completed the task by assigning the custom
    # qualifier that you've already set up in your MTurk account for this HIT
    'grant_qualification_id': '',
    'qualification_requirements': [
        # prevents workers from completing task again after being flagged
        # with custom qualifier
        {
            'QualificationTypeId': '',
            'Comparator': "DoesNotExist",
        },
        # requires workers be located in the US
        {
            'QualificationTypeId': '00000000000000000071',
            'Comparator': "EqualTo",
            'LocaleValues': [{'Country': "US"}],
        },
        # requires workers to have completed at least 5 HITs
        {
            'QualificationTypeId': '00000000000000000040',
            'Comparator': "GreaterThan",
            'IntegerValues': [5],
        },
        # requires workers to have HIT approval rate of at least 95 percent
        {
            'QualificationTypeId': '000000000000000000L0',
            'Comparator': "GreaterThanOrEqualTo",
            'IntegerValues': [95],
        },
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0,
    'participation_fee': ,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': 'study_1a',
        'display_name': "Study 1A",
        'num_demo_participants': 1,
        'app_sequence': ['predicting_outcomes_A', 'probability_financial', 'demographics'],
    },
    {
        'name': 'study_1b',
        'display_name': "Study 1B",
        'num_demo_participants': 1,
        'app_sequence': ['predicting_outcomes_B', 'probability_financial', 'demographics'],
    },
   

   
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())

