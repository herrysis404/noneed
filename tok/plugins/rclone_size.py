#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) gautamajay52

import subprocess
import os
import asyncio

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def g_clearme(client, message):
    inline_keyboard = []
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton("Yes 🚫", callback_data=("fuckingdo").encode("UTF-8")))
    ikeyboard.append(InlineKeyboardButton("No 🤗", callback_data=("fuckoff").encode("UTF-8")))
    inline_keyboard.append(ikeyboard)
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text("Are you sure? 🚫 This will delete all your downloads locally 🚫", reply_markup=reply_markup, quote=True)
