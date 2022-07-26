from pystyle import Write, Colors

name = Write.Input("Enter your name -> ", Colors.red_to_purple, interval=0.0025)
Write.Print(f"Nice to meet you, {name}!", Colors.blue_to_green, interval=0.05)
from pystyle import Colors, Colorate
print(Colorate.Horizontal(Colors.yellow_to_red, "Hello, Welcome to Pystyle.", 1))
from pystyle import Colors, Colorate
text = "Hello world!"
print((Colors.red + text, True))
# or
print(Colorate.Color(Colors.blue, text, True))
from pystyle import Center
print(Center.XCenter("Hello, Welcome to Pystyle."))
from pystyle import Add
banner1 = '''
    .--.
  .'_\/_'.
  '. /\ .'
    "||"
     || /\
  /\ ||//\)
 (/\\||/
____\||/____'''

text = "This is a beautiful banner\nmade with pystyle"

print(Add.Add(banner1, text, 4))
from pystyle import Box
print(Box.Lines("Hello, Welcome to Pystyle."))
print(Box.DoubleCube("Hello, Welcome to Pystyle."))
from pystyle import Colors, Colorate
print(Colorate.Horizontal(Colors.yellow_to_red, "Hello, Welcome to Pystyle.", 1))
from pystyle import Write, Colors

name = Write.Input("Enter your name -> ", Colors.red_to_purple, interval=0.0025)
Write.Print(f"Nice to meet you, {name}!", Colors.blue_to_green, interval=0.05)
from pystyle import Center
print(Center.XCenter("Hello, Welcome to Pystyle."))
from pystyle import Box
print(Box.Lines("Hello, Welcome to Pystyle."))
print(Box.DoubleCube("Hello, Welcome to Pystyle."))




