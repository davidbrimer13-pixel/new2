# Original upbeat pop-style loop for the BBC micro:bit (MakeCode Python).
# This is an original pattern, not a transcription of Coldplay's song.
#
# micro:bit V2 is required for the built-in microphone. The LEDs show the
# microphone's overall sound level; the top-left LED marks each bass beat.
# The microphone measures overall volume, not bass frequencies specifically.

STEP_MS = 240  # eighth-note pulse, about 125 BPM
SAMPLES_PER_STEP = 6
SAMPLE_MS = STEP_MS // SAMPLES_PER_STEP

# One original 16-step instrumental phrase. The bass notes mark the pulse;
# other notes make a simple upbeat accompaniment. Frequencies are in Hz.
PATTERN = [
    110, 392, 330, 392,
    147, 440, 392, 330,
    110, 392, 494, 440,
    147, 392, 330, 294,
]

while True:
    for step in range(len(PATTERN)):
        music.stop_all_sounds()
        music.ring_tone(PATTERN[step])

        # Sample while the note plays so the display reacts to the sound.
        for sample in range(SAMPLES_PER_STEP):
            level = input.sound_level()  # 0..255; requires micro:bit V2
            led.plot_bar_graph(level, 255)

            # Mark the four bass beats in each bar. This is a timed beat
            # marker; the microphone itself does not separate bass from treble.
            if step % 4 == 0:
                led.plot(0, 0)
            else:
                led.unplot(0, 0)
            basic.pause(SAMPLE_MS)

    music.stop_all_sounds()
    basic.clear_screen()
    basic.pause(250)
