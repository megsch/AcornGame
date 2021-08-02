import subprocess
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_game_parser import run_tests as test_game_parser

print("###########################")
print("### Running unit tests! ###")
print("###########################\n")

test_game()
test_grid()
test_parser()
test_game_parser()

# Run the e2e script
subprocess.call(['./test_e2e.sh'])
