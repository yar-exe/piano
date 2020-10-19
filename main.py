myImage = images.create_image("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)
myImage.show_image(0)

def on_forever():
    if WSTouchPiano.TP_Press(TP_PIANO.C):
        WSTouchPiano.TP_PlayMusic(131, music.beat(BeatFraction.WHOLE))
    if WSTouchPiano.TP_Press(TP_PIANO.D):
        WSTouchPiano.TP_PlayMusic(147, music.beat(BeatFraction.WHOLE))
    if WSTouchPiano.TP_Press(TP_PIANO.E):
        WSTouchPiano.TP_PlayMusic(165, music.beat(BeatFraction.WHOLE))
    if WSTouchPiano.TP_Press(TP_PIANO.F):
        WSTouchPiano.TP_PlayMusic(175, music.beat(BeatFraction.WHOLE))
    if WSTouchPiano.TP_Press(TP_PIANO.G):
        WSTouchPiano.TP_PlayMusic(196, music.beat(BeatFraction.WHOLE))
    if WSTouchPiano.TP_Press(TP_PIANO.A):
        WSTouchPiano.TP_PlayMusic(220, music.beat(BeatFraction.WHOLE))
    if WSTouchPiano.TP_Press(TP_PIANO.B):
        WSTouchPiano.TP_PlayMusic(247, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever)
