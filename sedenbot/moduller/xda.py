# Copyright (C) 2020 TeamDerUntergang.
#
# SedenUserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SedenUserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Credits: Quotes taken from friendly-telegram (https://gitlab.com/friendly-telegram)
#

from random import choice

from sedenbot import CMD_HELP
from sedenbot.events import sedenify

# ================= CONSTANT =================
XDA_STRINGS = [
    "sur",
    "Sir",
    "bro", 
    "yes",
    "no",
    "bolte",
    "bolit",
    "bholit",
    "volit",    
    "mustah",
    "fap",
    "lit",
    "lmao",
    "iz",
    "jiosim",
    "ijo",
    "nut",
    "workz",
    "workang",
    "flashabl zip",
    "bateri",
    "bacup",
    "bad englis",
    "sar",
    "treble wen",
    "gsi",
    "fox bag",
    "bag fox",
    "fine",
    "bast room",
    "fax",
    "trable",
    "kenzo",
    "plz make room",
    "andreid pai",
    "when",
    "port",
    "mtk",
    "send moni",
    "bad rom",
    "dot",
    "xd",
    "linage",
    "arrows",
    "kernal",
]

@sedenify(outgoing=True, pattern="^.xda$")
async def xda(xdaboi):
    await xdaboi.edit(choice(XDA_STRINGS))

CMD_HELP.update({
    "xda":
    ".xda veya .xda ile birinin metnine cevap verin.\
    \nKullanım: XDA'nın meşhur sözleri."
})
