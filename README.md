#Bomber

Bomber is a two player game where each player has to conquer territory by placing bombs, until the opponent is trapped.  
Various powerups can appear when conquering territory, wich can enhance your bombs, speed and bomb capacity.

![screenshot](https://github.com/joaodelgado/bomber/raw/master/bomber.jpg "Game Screenshot")

This is my attempt to make a game in python, using [pygame modules](http://pygame.org).  
The game is heavily inspired by the awesome free game [Bomberjam](http://iamclaw.com/?page_id=235).

###How to play

To play just make sure you have [Python 2.7](http://www.python.org/) and [Pygame](http://pygame.org) installed and run:

    python bomber.py

#####Controls

    Player 1:
        WASD to move
        Space to place a bomb

    Player 2:
        Arrow keys to move
        P to place a bomb

###Change Log
* [Version 1.2](https://github.com/joaodelgado/Bomber/tree/v1.2)
	+ Game over is now detected correctly, even when the player isn't in the center of the conquered square.

* [Version 1.1](https://github.com/joaodelgado/Bomber/tree/v1.1)
	+ Collisions are now correctly detected (no more jumpy jump around corners)

* [Version 1.0](https://github.com/joaodelgado/Bomber/tree/v1.0)