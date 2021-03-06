import turtle


screen = turtle.Screen()
screen.setup(400, 400)

# Everytime you click the square screen "canvas" area, 
# that square will change color to either RED or GREEN via ALTERNATION.

# This variable (storage box) contains a number that we call the "decision number".
# This number is "incremented" (increased by exactly one) each time 
# the user clicks on the screen.
# The "paint_screen_based_on_current_color_number" function will use this 
# to figure out which color to use!
CURRENT_COLOR_NUMBER = 1 



def paint_screen_based_on_current_color_number():
  # As I promised in a comment above, this function will use the 
  # "decision number" to determine what color to use.
  # If the decision number is an EVEN number, it will use RED.
  # If it's ODD, it will use GREEN.
  #
  # OK so how do you figure out whether the decision number is ODD or EVEN?
  # Well, the easiest way: divide by 2 and then look at the REMAINDER.
  # In python, you compute the "division remainder" of two whole numbers 
  # by using '%'

  # The remainder will be either 0, 1, or 2
  if (CURRENT_COLOR_NUMBER % 2) == 0:
    # In this case, the remainder was 0, so the number is EVEN.
    color_to_change_to = 'RED'
  else: 
    color_to_change_to = 'GREEN'
  
  # So we have decided what color to change the screen to.  So... let's DO IT!
  screen.bgcolor(color_to_change_to)
#
#^^^^^^ END OF THE paint_screen_based_on_current_color_number FUNCTION.





def respond_to_user_click_on_screen(x, y):
  global CURRENT_COLOR_NUMBER   
  # See my comment about this word "global" just a couple of lines below...
  CURRENT_COLOR_NUMBER = CURRENT_COLOR_NUMBER + 1
  print("New value of the global is:")
  print(CURRENT_COLOR_NUMBER)
  paint_screen_based_on_current_color_number()
  # OK, so this function works but.. 
  # what is this word "global" doing at the top of the function?
  # This is a complex topic that we'll talk about at length later.
  # For now, just think this way:  
  # if your function wants to CHANGE a variable that was created
  # "outside" of itself, then it needs to ask for permission 
  # to use that "global variable".
  # In this program, CURRENT_COLOR_NUMBER is a "global variable" 
  # because it was created
  # "outside" of the scope of any particular function.
  # So this function, because it wants the ability to change its value,
  # has to ask for permission,
  # so I had to write:   global CURRENT_COLOR_NUMBER
  # as the first line of this function.






###### Now that we've set up the screen and 
###### we've given birth to Tina and we've defined the functions that we need,
###### we're ready to start the actual program:

print("CLICK anywhere on the colored square to ALTERNATE the screen color.")

paint_screen_based_on_current_color_number()
screen.listen()
screen.onclick(respond_to_user_click_on_screen)
