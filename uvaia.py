#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot

bot = InstaBot(
    login="uvaiaoficial",
    password="amandalinda",
    like_per_day=1500,
    comments_per_day=0,
    tag_list=['alimentacaosaudavel',
              'frutasnopote',
              'frutasfrescas',
              'frutafresca',
              'comidaboa',
              'alimentacao',
              'habitossaudaveis',
              'ineex',
              'l:1806951',
              'l:1779922605659559',
              'l:719665800',
              'l:216132271',
              'l:465151',
              'l:214840985',
              'l:3059300',
              'l:1781041',
              'l:215269605',
              'l:228501865',
              'l:1027110065',
              'l:325644692',
              'l:288448914514602',
              'l:875288125920032',
              'l:1025496196',
              'l:72222545',
              'l:190058111840185',
              'l:54429001',
              'l:894688496',
              'l:1164826946960716',
              'l:1722313848065978',
              'l:218784799',
              'l:1401663589929018',
              'l:748113105363982',
              'l:281403607',
              'l:286673672',
              'l:2188275',
              'l:711541803',
              'l:1913384',
              'l:910633749008804',
              'l:861502609',
              'l:246356359',
              'l:214243051',
              'l:1029791784',
              'l:8473203',
              'l:213627299',
              'l:324038848008137',
              'l:214597752730809',
              'l:213783727',
              'l:225223317828719',
              ],
    tag_blacklist=[],
    user_blacklist={},
    max_like_for_one_tag=5000,
    follow_per_day=1000,
    follow_time= 1 * 60,
    unfollow_per_day= 900,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    # comment_list=[["😍"]],
    comment_list=[[""]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[],
    unfollow_whitelist=[])

while True:
    
    mode = 0

    if mode == 0:
        bot.new_auto_mod()
