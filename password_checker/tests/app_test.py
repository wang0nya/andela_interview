from app import app

def test_password(capsys):
    u_inp = ["$h0rT", "Veryveryvery1ongpa$s", "Nonumb#r",
                "NO10W@R", "n0upp@r", "N0specia1", "V@1idP"]
    output = []

    def mock_input(s):
        output.append(s)
        return u_inp.pop(0)

    app.input = mock_input
    app.print = lambda s : output.append(s)

    app.check_password() 

    assert output == ["Enter password: ",
                        "Password length has to be between 6 and 12 characters",
                        "Enter password: ",
                        "Password length has to be between 6 and 12 characters",
                        "Enter password: ",
                        "Password must have atleast one number",
                        "Enter password: ",
                        "Password must have atleast one lower case character",
                        "Enter password: ",
                        "Password must have atleast one upper case character",
                        "Enter password: ",
                        "Password must have at least 1 character from [$#@]",
                        "Enter password: ",
                        "Valid Password"
                        ]