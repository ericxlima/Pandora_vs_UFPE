class Vector2:
    def __init__(self,pos_x,pos_y):
        """
          x   y     Moviment:
         (1 , 0) -> Right
         (-1, 0) -> Left
         (0 , 1) -> Down
         (0 ,-1) -> Up 
        """
        self._x = pos_x
        self._y = pos_y
    
    @property
    def x(self):
        return self._X
    
    @property
    def y(self):
        return self._y