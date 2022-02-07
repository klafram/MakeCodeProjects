def on_button_pressed_a():
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(415, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)
