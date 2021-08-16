class Vector2:
    def __init__(self,pos_x,pos_y):
        """
         (1,0) cima
         (-1,0) baixo
         (0,1) direita
         (0,-1) esquerda 
         eu acho
        """
        self._x = pos_x
        self._y = pos_y
    
    @property
    def x(self):
        return self._X
    
    @property
    def y(self):
        return self._y