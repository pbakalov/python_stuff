class Triangle(object):
    def __init__(self, angle1, angle2):
        self.angle1=angle1
        self.angle2=angle2
    number_of_sides=3
    def angle3(self):
        return 180-self.angle1-self.angle2
    def check_angles(self):
        if (self.angle1+self.angle2+self.angle3()==180):
            return True
        else:
            return False

bob=Triangle(40,60)

print bob.angle3()
print bob.check_angles()
