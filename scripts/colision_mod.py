from scripts.colision import Colision
from scripts.vector2 import Vector2


class Colision_mod:
 
    def __init__(self,objs) -> None:
        """Returns colision events
        Args:
            objs (list): list with all objects with colision
        """
        self._objs = objs

    @property
    def objs(self):
        return self._objs

    def check_colision(self) -> list:
        """Check all colisions in objs 
        Returns:
            list:  colision list with colision pairs
        """
        objs = self.objs
        events = []
        for i in range(len(self.objs)):
            for j in range(i+1,len(self.objs)):
                if ( ( (objs[i].x + (objs[i].w) ) >= (objs[j].x) ) and ( (objs[i].x) <= (objs[j].x) ) ) or ( (objs[i].x) <= (objs[j].x + objs[j].w) and ( (objs[i].x + (objs[i].w)) >= (objs[j].x + objs[j].w))  ):
                    if ( ( (objs[i].y + (objs[i].h) ) >= (objs[j].y) ) and ( (objs[i].y + (objs[i].h) <= (objs[j].y + objs[j].h) ) ) ) or ( ( (objs[i].y) <= (objs[j].y + objs[j].h) ) and ( (objs[i].y) >= (objs[j].y) ) ):
                        vectro2 = Vector2(1,0)  # Just for test
                        colision = Colision(objs[i],objs[j],vectro2)
                        events.append(colision) 
        
        return events



