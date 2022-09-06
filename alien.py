"""
List of different stages for the alien made with
ASCII art. File will be imported to run.py
User will get 6 guesses before the alien is fully formed
and the game is lost.
Alien art taken from https://ascii.co.uk/art/aliens
"""
def alien_stages(remaining_attempts):
    max_attempts = 6
    ALIENS = ["""
         .--.   
        /    \ 
        q .. p 
         \--/  
        __||__ 
    """, """
         .--.   |V|
        /    \ _| /
        q .. p \ /
         \--/  //
        __||__//
        /.    _/ 
    """, """
         .--.   |V|
        /    \ _| /
        q .. p \ /
         \--/  //
        __||__//
       /.    _/
      // \  /
     //   ||
     \\  
      )\
     / |
     |/\
    """, """
         .--.   |V|
        /    \ _| /
        q .. p \ /
         \--/  //
        __||__//
       /.    _/
      // \  /
     //   ||
     \\  /  \
      )\|    |
     / || || |
     |/\
    """, """
         .--.   |V|
        /    \ _| /
        q .. p \ /
         \--/  //
        __||__//
       /.    _/
      // \  /
     //   ||
     \\  /  \
      )\|    |
     / || || |
     |/\| || |
        | || |
        \ |
      __/ |
     \____/
    """, """
         .--.   |V|
        /    \ _| /
        q .. p \ /
         \--/  //
        __||__//
       /.    _/
      // \  /
     //   ||
     \\  /  \
      )\|    |
     / || || |
     |/\| || |
        | || |
        \ || /
      __/ || \__
     \____/\____/
    """]
    return ALIENS[max_attempts - remaining_attempts]