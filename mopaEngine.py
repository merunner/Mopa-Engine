#!/usr/bin/env python

class MopaEngine(object):

    def __init__(self):
        self.game = None

    def load(self):
        pass
    
    def listen(self):
        pass
        
    def update(self):
        print 'Update!'
        
    def render(self):
        print 'Render!'
        
    def flush(self):
        print 'Flush!'

    def run(self):
        while True:
            try:
                self.load()
                self.listen()
                self.update()
                self.render()
                self.flush()
            
            except Exception, e:
                break


if __name__ == '__main__':
    mopaEngine = MopaEngine()
    mopaEngine.run()
