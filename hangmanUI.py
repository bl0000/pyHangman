
def gui(count):
    global hangmanascii
    if count == 0:
        hangmanascii = """ 
 



        """
    elif count == 1:
        hangmanascii = """
         
 


==========
        """
    elif count == 2:
        hangmanascii = """       
       |
       |
       |
       |
       |
==========
        """
    elif count == 3:
        hangmanascii = """
  +----+
       |
       |
       |
       | 
       |
==========
         """
    elif count == 4:
        hangmanascii = """
  +----+
  |   \|
       |
       |
       | 
       |
==========
         """
    elif count == 5:
        hangmanascii = """
  +----+
  |   \|
  o    |
  |    |
       | 
       |
==========
         """
    elif count == 6:
        hangmanascii = """
  +----+
  |   \|
  o    |
 /|\   |
       | 
       |
==========
         """
    elif count == 7:
        hangmanascii = """
  +----+
  |   \|
  o    |
 /|\   |
 / \   | 
       |
==========
         """
    return hangmanascii




