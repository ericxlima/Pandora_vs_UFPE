class Colision:
    def __init__(self,_gameobject1,_gameobject2,vector):
        self._go1 = _gameobject1
        self._go2 = _gameobject2
        self._vector2 = vector
    
    @property
    def go1(self):
        return self._go1
    
    @property
    def go2(self):
        return self._go2 
    
    @property
    def vector2(self):
        return self._vector2