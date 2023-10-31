>>> text_indentation = __import__('5-text_indentation').text_indentation

# There goes the test cases

>>> text_indentation("hi.")
hi.
<BLANKLINE>

>>> text_indentation(9)
Traceback (most recent call last):
TypeError: text must be a string

>>> text_indentation(str(65))
65

>>> text_indentation("I love solving problems!")
I love solving problems!

>>> text_indentation("Hello.     World")
Hello.
<BLANKLINE>
World

<BLANKLINE>
>>> text_indentation('koech.Gideon')
koech.
<BLANKLINE>
Gideon

>>> text_indentation()
Traceback (most recent call last):
TypeError: text_indentation() missing 1 required positional argument: 'text'
