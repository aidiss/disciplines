"""Usage: print.py --count=N [--caps] TEXT...

Arguments:
    TEXT  Message to be printed

Options:
    --disciplines list all disciplines from examples
    --name  prints "This module is named disciplines"
"""

# Docopt is a library for parsing command line arguments
import docopt

if __name__ == '__main__':
    print ("This example demonstrates basic usage of docopt")
    print ("You can run this script manually by using:")

    try:
        # Parse arguments, use file docstring as a parameter definition
        arguments = docopt.docopt(__doc__)

        # Count is a mandatory option, caps is optional
        disciplines = int(arguments['--disciplines'])
        name = arguments['--name']

        for i in range(count):
            # In the definition, we expect one or more TEXT parameters
            # Each parameter is a word, or a text in quotes: "something like this"
            # If the user forgets about the quote, the program would print only "something"
            # Thus, we merge all the specified parameters with space
            text = ' '.join(arguments['TEXT'])
            if(caps):
                print (text.upper())
            else:
                print (text)

    # Handle invalid options
    except docopt.DocoptExit as e:
        print (e.message)
