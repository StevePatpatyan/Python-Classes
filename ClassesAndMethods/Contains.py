from graphics import*
def contains(coord,rec):
    if (coord.getX()>rec.getP1().getX() and coord.getX()<rec.getP2().getX() and coord.getY()>rec.getP1().getY() and coord.getY()<rec.getP2().getY()):
        return True
    else:
        return False
