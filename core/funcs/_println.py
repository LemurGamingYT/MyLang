from sys import stdout


def _println(args: list):
    stdout.write(str(args[0].value) + "\n")
