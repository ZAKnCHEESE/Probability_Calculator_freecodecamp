# #made by Zakariya Boukhezza
from random import choices,randint


class Hat():
    def __init__(self,**kwargs):
        
        self.hats = kwargs  
        self.contents = self._content_maker()


    def draw(self,balls_to_draw):
        drew = []
        if len(self.contents) >= balls_to_draw:
            for i in range(balls_to_draw):
                drew.append(self.contents.pop(randint(1,len(self.contents))-1))
        return drew

    def __append__(self,to_add):
        self.contents.append(to_add)
        return

    def _content_maker(self):
        
        hats = []

        for key in self.hats:
            
            for i in range(self.hats[key]):
                hats.append(key)


        return hats


def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    '''
    hat:  Hat object

    expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. 
    For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat
    
    num_balls_drawn: amount of balls to draw

    num_experiments: how many experiments to run. my denominator.

    '''
    balls = []
    n = 0   
    for key in expected_balls:
        
        for i in range(expected_balls[key]):
            balls.append(key)

    
    #print(balls,1)

    for experience in range(num_experiments):
        balls_drawn = hat.draw(num_balls_drawn)
        hat.contents.extend(balls_drawn)
        
        #print(balls_drawn)
        i = 0
        while i < len(balls):
            if balls_drawn.count(balls[i]) >= balls.count(balls[i]):
                i += 1
                if i == len(balls):
                    n+= 1
                    print(n)
            else:
                i = len(balls)
    
    return n / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2)


print(probability)




