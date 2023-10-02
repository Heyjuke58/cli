# Boilerplate CLI

Automation script that adds python boilerplate code for writing a comman line interface (cli).
The files ``argument_parser.py`` and ``main.py`` will be added to a target directory if they do not exist yet. Otherwise the script will fail.

## How to setup

How to setup the automation script on a unix machine:

1. Move all files into a ``bin`` folder in your home directory
2. Make ``cli`` executable: ``chmod +x ~/bin/cli``
3. Add ``export PATH=$PATH":$HOME/bin"`` to your ``.bashrc``
4. Reload bash settings ``source ~/.bashrc``

## How to run

1. Navigate to a directory where you want to add the boilerplate code
2. Run ``cli``
