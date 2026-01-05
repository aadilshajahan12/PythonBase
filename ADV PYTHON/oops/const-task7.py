# Create a class *Movie* whose constructor accepts:
#
# * movie name
# * hero
# * rating
#
# Add a method to check:
#
# * If rating ≥ 7 → print “Hit movie”
# * Else → print “Average movie

class Movie:
    def __init__(self,moviename,hero,rating):
        self.moviename=moviename
        self.hero=hero
        self.rating=rating
    def disp(self):
        print('movie',self.moviename)
        print('hero',self.hero)
        print('rating',self.rating)
        if self.rating>=7:
            print('HIT')
        else:
            print("AVG")

c=Movie('eko','zandeep',8)
c.disp()