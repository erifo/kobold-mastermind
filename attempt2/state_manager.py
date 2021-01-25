class StateManager():
    def __init__(self):
        self._statestack = []
    
    def push(self, state):
        self._statestack.append(state)
    
    def pop(self):
        self._statestack.pop()
    
    def current(self):
        return self._statestack[-1]
