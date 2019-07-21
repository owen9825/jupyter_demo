# -*- coding: utf-8 -*-

import dotenv
import os

dotenv.load_dotenv('.secrets')

# Please use your own key from http://developer.wolframalpha.com/portal/myapps/
WOLFRAM_KEY = os.getenv('WOLFRAM_ALPHA_KEY', "KK2J7A-69G6RELGRE")
