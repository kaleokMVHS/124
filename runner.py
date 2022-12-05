import turtle as trtl
import random as rand

#-------------- setup --------------#
maze_painter = trtl.Turtle()
maze_painter.pu()
maze_painter.speed(0)
maze_painter.setheading(270)
maze_painter.pd()

walls = 24
path_width = 10

curr_wall_len = 75

runner = trtl.Turtle()
runner.pu()
runner.goto(50, -25)
runner.pd()
movement_amount = 10

writer = trtl.Turtle()
writer.hideturtle()
writer.pu()
writer.goto(50, 250)
font_setup = ('Arial', 8, 'normal')

Running = False
Timer = 0

#-------------- function definitions --------------#

def feature_position(wall_len):
  return rand.randint(0, wall_len)

def rand_bool():
  return rand.randint(1, 2) % 2 == 0

def doorway():
  maze_painter.pu()
  maze_painter.forward(path_width*2)
  maze_painter.pd()

def barrier():
  maze_painter.left(90)
  maze_painter.forward(path_width*2)
  maze_painter.right(180)
  maze_painter.forward(path_width*2)
  maze_painter.left(90)

def door_first_wall(curr_wall_len, wall_num):
  remaining_wall_len = curr_wall_len
  remaining_wall_len -= path_width*4

  maze_painter.forward(path_width*2)

  # doorway
  if (wall_num < 20):
    dist_to_first_feature = feature_position(remaining_wall_len)
    maze_painter.forward(dist_to_first_feature)
    remaining_wall_len -= dist_to_first_feature
    doorway()
  else:
    maze_painter.forward(path_width*2)
  

  # barrier
  if (wall_num > 4):
    dist_to_second_feature = feature_position(remaining_wall_len)
    maze_painter.forward(dist_to_second_feature)
    remaining_wall_len -= dist_to_second_feature
    barrier()
    
  maze_painter.forward(remaining_wall_len)
  maze_painter.forward(path_width*2)

  maze_painter.left(90)

def barrier_first_wall(curr_wall_len, wall_num):
  remaining_wall_len = curr_wall_len
  remaining_wall_len -= path_width*4

  maze_painter.forward(path_width*2)

  # barrier
  if (wall_num > 4):
    dist_to_first_feature = feature_position(remaining_wall_len)
    maze_painter.forward(dist_to_first_feature)
    remaining_wall_len -= dist_to_first_feature
    barrier()
  

  # doorway
  if (wall_num < 20):
    dist_to_second_feature = feature_position(remaining_wall_len)
    maze_painter.forward(dist_to_second_feature)
    remaining_wall_len -= dist_to_second_feature
    doorway()
  else:
    maze_painter.forward(path_width*2)
    
  maze_painter.forward(remaining_wall_len)
  maze_painter.forward(path_width*2)

  maze_painter.left(90)

def face_east():
  runner.setheading(0)

def face_west():
  runner.setheading(180)

def face_north():
  runner.setheading(90)

def face_south():
  runner.setheading(270)

def move_runner():
  runner.forward(movement_amount)

def refresh_clock():
  global Timer
  writer.clear()
  writer.write(Timer, font=font_setup)


def countup():
  global Running
  global Timer

  if (Running):
    trtl.ontimer(countup, 1000)
    Timer += 1
    refresh_clock()


#-------------- function calls ---------------#

for i in range(1, walls):
  if (rand_bool()):
    barrier_first_wall(curr_wall_len, i)
  else:
    door_first_wall(curr_wall_len, i)
    
  curr_wall_len += path_width
maze_painter.hideturtle()
  
wn = trtl.Screen()

wn.onkeypress(face_south, "Down")
wn.onkeypress(face_east, "Right")
wn.onkeypress(face_north, "Up")
wn.onkeypress(face_west, "Left")
wn.onkeypress(move_runner, "g")

wn.listen()

Running = True
countup()

wn.mainloop()