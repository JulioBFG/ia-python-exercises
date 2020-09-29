class CandidateState:
  def __init__(self, state, parent = None, action = None):
    self.state = state
    self.parent = parent
    self.action = action
    self.children = []

  def getSuccessors(self):
    list = self.state.getActions()
    successors = []

    for action in list:
      state = self.state.doAction(action)

      successor = CandidateState(state,self,action)
      self.children.append(successor)

      successors.append(successor)
  
  def toString(self):
    if(self.action):
      return f"{self.action} > {self.state.toString()}"
    else:
      return f"start > {self.state.toString()}"
