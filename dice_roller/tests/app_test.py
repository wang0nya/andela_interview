from app import app

def test_dice_roller():
    assert app.dice_roller() in range(1,7)


"""only testing for invalid input and quit since 'y' is already
covered under test_dice_roller"""
def test_roll_again_invalid_quit(capsys):
    u_inp = ["w", "q"]
    output = []

    def mock_input(s):
        output.append(s) # input also has some output
        return u_inp.pop(0)

    app.input = mock_input
    app.print = lambda s : output.append(s) # rest of prints

    app.roll_again()

    assert output == ["Play again? Press (y)es / (q)uit.\n",
                        "Please enter a valid input. 'y' to continue, 'q' to quit.",
                        "Play again? Press (y)es / (q)uit.\n"] 