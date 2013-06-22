from labs.DisplayMaze import Maze

map = ['*S**********',
       '* *    * * *',
       '* * * **   *',
       '*   *  * * *',
       '** *** * * *',
       '*        * *',
       '* * ****** *',
       '* * * *    *',
       '***** * ****',
       '*          *',
       '**********E*',
       ]

m = Maze()
m.setMaze(map)
m.display()
m.game()