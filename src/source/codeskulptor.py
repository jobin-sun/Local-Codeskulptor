# Local-Codeskulptor is a tool to make Codeskulptor works offline .
# If it is useful to you , fork on github(https://github.com/jobin-sun/Local-Codeskulptor) .
# See Online Codeskulptor http://www.codeskulptor.com/.

# Click the upper left button to run this simple demo.

import simplegui
message = "Welcome!"
sound = simplegui.load_sound('test.ogg')
isPlaying = 0


# Handler for mouse click
def click():
    global message
    message = "Good job!"
def play():
	global isPlaying
	if isPlaying == 0:
		sound.play()
		isPlaying = 1
		music_btn.set_text("Pause music")
	else:
		sound.pause()
		isPlaying = 0
		music_btn.set_text("Play music")

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
music_btn=frame.add_button("Play music", play)
frame.set_draw_handler(draw)
# Start the frame animation
frame.start()
