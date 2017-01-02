import tkinter
from tkinter import *
import os
import sys
from tcpgecko import TCPGecko

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        self.button2.config(state=DISABLED)
        self.button3.config(state=DISABLED)
        self.button4.config(state=DISABLED)
        self.button5.config(state=DISABLED)
        self.button6.config(state=DISABLED)
        self.button7.config(state=DISABLED)
        self.button8.config(state=DISABLED)
        self.button9.config(state=DISABLED)
        self.button10.config(state=DISABLED)
        self.button11.config(state=DISABLED)
        self.button12.config(state=DISABLED)
        self.button13.config(state=DISABLED)
        self.button14.config(state=DISABLED)
        self.button15.config(state=DISABLED)
        self.button16.config(state=DISABLED)
        self.button17.config(state=DISABLED)
        self.button18.config(state=DISABLED)
        self.button19.config(state=DISABLED)
        self.button20.config(state=DISABLED)
        self.button21.config(state=DISABLED)
        self.button22.config(state=DISABLED)
        self.button23.config(state=DISABLED)
        self.button24.config(state=DISABLED)

    def create_widgets(self):

        self.labela = Label(self)
        self.labela["text"] = 'ASH-AIO'
        self.labela.grid(row = 0, column = 0)

        self.labelb = Label(self)
        self.labelb["text"] = 'Hack responsibly.'
        self.labelb.grid(row = 1, column = 1)

        self.labelc = Label(self)
        self.labelc["text"] = 'Your Wii U IP:'
        self.labelc.grid(row = 3, column = 0)

        self.labeld = Label(self)
        self.labeld["text"] = 'Current Status:'
        self.labeld.grid(row = 4, column = 0)

        self.labele = Label(self)
        self.labele["text"] = 'Ready'
        self.labele.grid(row = 4, column = 1)

        self.labelf = Label(self)
        self.labelf["text"] = 'By Hexexpeck'
        self.labelf.grid(row = 13, column = 1)

        self.labelg = Label(self)
        self.labelg["text"] = 'Version 1.0'
        self.labelg.grid(row = 13, column = 2)

        self.labelh = Label(self)
        self.labelh["text"] = 'Hacks by the ASH Team'
        self.labelh.grid(row = 12, column = 1)

        self.labeli = Label(self)
        self.labeli["text"] = 'For Splatoon 2.12.0'
        self.labeli.grid(row = 12, column = 2)

        # each button will run a hack which are all placed in defs below, i tried to make this AIO a true AIO by requiring as little files as possible
        self.button1 = Button(self)
        self.button1["text"] = "Connect to Wii U"
        self.button1["command"] = self.tcpconnect
        self.button1.grid(row = 3, column = 2)

        self.button2 = Button(self)
        self.button2["text"] = "Disconnect"
        self.button2["command"] = self.tcpdisconnect
        self.button2.grid(row = 3, column = 3)

        self.button3 = Button(self)
        self.button3["text"] = "Big Inkling Hack"
        self.button3["command"] = self.biginkling
        self.button3.grid(row = 5, column = 0)

        self.button4 = Button(self)
        self.button4["text"] = "Darker Ink"
        self.button4["command"] = self.darkerink
        self.button4.grid(row = 5, column = 1)

        self.button5 = Button(self)
        self.button5["text"] = "Giant Inkling"
        self.button5["command"] = self.giantinkling
        self.button5.grid(row = 5, column = 2)

        self.button6 = Button(self)
        self.button6["text"] = "Glowing Stage"
        self.button6["command"] = self.glowingstage
        self.button6.grid(row = 5, column = 3)

        self.button7 = Button(self)
        self.button7["text"] = "Lighter Ink"
        self.button7["command"] = self.lighterink
        self.button7.grid(row = 6, column = 0)

        self.button8 = Button(self)
        self.button8["text"] = "Make Everything Big"
        self.button8["command"] = self.makeeverythingbig
        self.button8.grid(row = 6, column = 1)

        self.button9 = Button(self)
        self.button9["text"] = "Make Everything Small"
        self.button9["command"] = self.makeeverythingsmall
        self.button9.grid(row = 6, column = 2)

        self.button10 = Button(self)
        self.button10["text"] = "No Inkling"
        self.button10["command"] = self.noinkling
        self.button10.grid(row = 6, column = 3)

        self.button11 = Button(self)
        self.button11["text"] = "Small Inkling"
        self.button11["command"] = self.smallinkling
        self.button11.grid(row = 7, column = 0)

        self.button12 = Button(self)
        self.button12["text"] = "Transparent Inkling"
        self.button12["command"] = self.transparentinkling
        self.button12.grid(row = 7, column = 1)

        self.button13 = Button(self)
        self.button13["text"] = "White/Blind Ink"
        self.button13["command"] = self.whiteblindink
        self.button13.grid(row = 7, column = 2)

        self.button14 = Button(self)
        self.button14["text"] = "WIP-Flyhax"
        self.button14["command"] = self.wipfly
        self.button14.grid(row = 7, column = 3)

        self.button15 = Button(self)
        self.button15["text"] = "Speed/SpeedyRoller"
        self.button15["command"] = self.speedhax
        self.button15.grid(row = 8, column = 0)

        self.button16 = Button(self)
        self.button16["text"] = "Sustained Jump"
        self.button16["command"] = self.sustained
        self.button16.grid(row = 8, column = 1)

        self.button17 = Button(self)
        self.button17["text"] = "Stance Angle"
        self.button17["command"] = self.stance
        self.button17.grid(row = 8, column = 2)

        self.button18 = Button(self)
        self.button18["text"] = "Faceplant"
        self.button18["command"] = self.faceplant
        self.button18.grid(row = 8, column = 3)

        self.button19 = Button(self)
        self.button19["text"] = "Glide"
        self.button19["command"] = self.glider
        self.button19.grid(row = 9, column = 0)

        self.button20 = Button(self)
        self.button20["text"] = "Cinema Mode"
        self.button20["command"] = self.movies
        self.button20.grid(row = 9, column = 1)

        self.button21 = Button(self)
        self.button21["text"] = "Tentacle Mod"
        self.button21["command"] = self.tentacle
        self.button21.grid(row = 9, column = 2)

        self.button22 = Button(self)
        self.button22["text"] = "Bouncy Walk"
        self.button22["command"] = self.bounce
        self.button22.grid(row = 9, column = 3)

        self.button23 = Button(self)
        self.button23["text"] = "AlphaHax"
        self.button23["command"] = self.alpha
        self.button23.grid(row = 10, column = 0)

        self.button24 = Button(self)
        self.button24["text"] = "Revert hacks"
        self.button24["command"] = self.tcprevert
        self.button24.grid(row = 11, column = 2)

        self.ip = Entry(self)
        self.ip.grid(row = 3, column = 1)

    def tcpconnect(self):
        global tcp
        try:
            tcp = tcp = TCPGecko(self.ip.get())
        except:
            self.labele["text"] = 'Failed to connect to Wii U.'
        else:
            self.button1.config(state=DISABLED)
            self.button2.config(state=NORMAL)
            self.button3.config(state=NORMAL)
            self.button4.config(state=NORMAL)
            self.button5.config(state=NORMAL)
            self.button6.config(state=NORMAL)
            self.button7.config(state=NORMAL)
            self.button8.config(state=NORMAL)
            self.button9.config(state=NORMAL)
            self.button10.config(state=NORMAL)
            self.button11.config(state=NORMAL)
            self.button12.config(state=NORMAL)
            self.button13.config(state=NORMAL)
            self.button14.config(state=NORMAL)
            self.button15.config(state=NORMAL)
            self.button16.config(state=NORMAL)
            self.button17.config(state=NORMAL)
            self.button18.config(state=NORMAL)
            self.button19.config(state=NORMAL)
            self.button20.config(state=NORMAL)
            self.button21.config(state=NORMAL)
            self.button22.config(state=NORMAL)
            self.button23.config(state=NORMAL)
            self.button24.config(state=NORMAL)
            self.ip.config(state=DISABLED)
            self.button1["text"] = 'Connected!'
            self.labele["text"] = 'Connected!'

    def tcpdisconnect(self):
        global tcp
        try:
            tcp.s.close()
        except:
            self.labele["text"] = 'Failed to disconnect.'
        else:
            self.ip.config(state=NORMAL)
            self.button1.config(state=NORMAL)
            self.button2.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button5.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.button10.config(state=DISABLED)
            self.button11.config(state=DISABLED)
            self.button12.config(state=DISABLED)
            self.button13.config(state=DISABLED)
            self.button14.config(state=DISABLED)
            self.button15.config(state=DISABLED)
            self.button16.config(state=DISABLED)
            self.button17.config(state=DISABLED)
            self.button18.config(state=DISABLED)
            self.button19.config(state=DISABLED)
            self.button20.config(state=DISABLED)
            self.button21.config(state=DISABLED)
            self.button22.config(state=DISABLED)
            self.button23.config(state=DISABLED)
            self.button24.config(state=DISABLED)
            self.labele["text"] = 'Disconnected.'
            self.button1["text"] = "Connect to Wii U"

    def biginkling(self):
        try:
            tcp.pokemem(0x105EF2B0,0x3FC00000)
        except:
            self.labele["text"] = 'BigInkling Hack fail.'
        else:
            self.labele["text"] = 'BigInkling Hack success.'

    def darkerink(self):
        try:
            tcp.pokemem(0x106D37A8,0x3FF00000)
        except:
            self.labele["text"] = 'DarkerInk Hack fail.'
        else:
            self.labele["text"] = 'DarkerInk Hack success.'

    def giantinkling(self):
        try:
            tcp.pokemem(0x105EF2B0,0x40000000)
        except:
            self.labele["text"] = 'GiantInkling Hack fail.'
        else:
            self.labele["text"] = 'GiantInkling Hack success.'

    def glowingstage(self):
        try:
            tcp.pokemem(0x10633774,0x3F830000)
        except:
            self.labele["text"] = 'GlowingStage Hack fail.'
        else:
            self.labele["text"] = 'GlowingStage Hack success.'

    def lighterink(self):
        try:
            tcp.pokemem(0x106D37A8,0x3F100000)
        except:
            self.labele["text"] = 'LighterInk Hack fail.'
        else:
            self.labele["text"] = 'LighterInk Hack success.'

    def makeeverythingbig(self):
        try:
            tcp.pokemem(0x106D3858,0x3FF00000)
        except:
            self.labele["text"] = 'MakeEverythingBig Hack fail.'
        else:
            self.labele["text"] = 'MakeEverythingBig Hack success.'

    def makeeverythingsmall(self):
        try:
            tcp.pokemem(0x106D3858,0x3F100000)
        except:
            self.labele["text"] = 'MakeEverythingSmall Hack fail.'
        else:
            self.labele["text"] = 'MakeEverythingSmall Hack success.'

    def noinkling(self):
        try:
            tcp.pokemem(0x105EF2B0,0x30000000)
        except:
            self.labele["text"] = 'NoInkling Hack fail.'
        else:
            self.labele["text"] = 'NoInkling Hack success.'

    def smallinkling(self):
        try:
            tcp.pokemem(0x105EF2B0,0x3F000000)
        except:
            self.labele["text"] = 'SmallInkling Hack fail.'
        else:
            self.labele["text"] = 'SmallInkling Hack success.'

    def transparentinkling(self):
        try:
            tcp.pokemem(0x105EBE34,0x3F100000)
            tcp.pokemem(0x105EBE40,0x3F100000)
        except:
            self.labele["text"] = 'TransparentInkling Hack fail.'
        else:
            self.labele["text"] = 'TransparentInkling Hack success.'

    def whiteblindink(self):
        try:
            tcp.pokemem(0x106D37A8,0x30000000)
        except:
            self.labele["text"] = 'White/Blind Ink Hack fail.'
        else:
            self.labele["text"] = 'White/Blind Ink Hack success.'

    def wipfly(self):
        try:
            tcp.pokemem(0x105EBE34,0x3FEF0000)
        except:
            self.labele["text"] = 'WIP Fly Hack fail.'
        else:
            self.labele["text"] = 'WIP Fly Hack success.'

    def speedhax(self):
        try:
            tcp.pokemem(0x105EBE40, 0x3F100000)
        except:
            self.labele["text"] = 'SpeedHack fail.'
        else:
            self.labele["text"] = 'SpeedHax success.'

    def sustained(self):
        try:
            tcp.pokemem(0x105EBE34, 0x3FC00000)
        except:
            self.labele["text"] = 'SustainedJump Hax fail.'
        else:
            self.labele["text"] = 'SustainedJump Hax success.'

    def stance(self):
        try:
            tcp.pokemem(0x105EC944, 0x3F100000)
        except:
            self.labele["text"] = 'StanceHax fail.'
        else:
            self.labele["text"] = 'StanceHax success.'

    def faceplant(self):
        try:
            tcp.pokemem(0x105EC944, 0x30F00000)
        except:
            self.labele["text"] = 'FaceplantHax fail.'
        else:
            self.labele["text"] = 'FaceplantHax success.'

    def glider(self):
        try:
            tcp.pokemem(0x105EC944, 0x30A00000)
        except:
            self.labele["text"] = 'GliderHax fail.'
        else:
            self.labele["text"] = 'GliderHax success.'

    def movies(self):
        try:
            tcp.pokemem(0x105ECA40, 0x3F400000)
        except:
            self.labele["text"] = 'Cinema Mode fail.'
        else:
            self.labele["text"] = 'Cinema Mode success.'

    def tentacle(self):
        try:
            tcp.pokemem(0x105EEBC4, 0x3F300000)
        except:
            self.labele["text"] = 'TentacleHax fail.'
        else:
            self.labele["text"] = 'TentacleHax success.'

    def bounce(self):
        try:
            tcp.pokemem(0x105F14EC, 0x3FF00000)
        except:
            self.labele["text"] = 'BounceHax fail.'
        else:
            self.labele["text"] = 'BounceHax success.'

    def alpha(self):
        try:
            tcp.pokemem(0x105F14EC, 30000000)
        except:
            self.labele["text"] = 'AlphaHax fail.'
        else:
            self.labele["text"] = 'AlphaHax success.'

    def tcprevert(self):
        global tcp
        try:
            tcp.pokemem(0x105EF2B0,0x3F800000)
            tcp.pokemem(0x106D37A8,0x3F800000)
            tcp.pokemem(0x10633774,0x3F800000)
            tcp.pokemem(0x106D3858,0x3F800000)
            tcp.pokemem(0x105EBE40,0x3F000000)
            tcp.pokemem(0x105EBE34,0x3F800000)
            tcp.pokemem(0x105EC944,0x3F800000)
            tcp.pokemem(0x105ECA40,0x3F000000)
            tcp.pokemem(0x105EEBC4,0x3F000000)
            tcp.pokemem(0x105F14EC,0x3F800000)
        except:
            self.labele["text"] = 'Revert failed.'
        else:
            self.labele["text"] = 'Revert success.'
            

root = Tk()
root.title("ASH-AIO for Splatoon 2.12.0")
root.geometry("520x320")

app = Application(root)

root.mainloop()
