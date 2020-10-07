class CandidateState:

  def __init__(self, state, parent=None, action=None):
    self.state = state
    self.parent = parent
    self.action = action
    self.children = []

  def getSuccessors(self):
    actions = self.state.getActions()
    successors = []
    #clone = []

    for ac in actions:
      state = self.state.doAction(ac)
      success = CandidateState(state, self, ac)
      self.children.append(success)

      successors.append(success)
    return successors

  def __str__(self):
    if(self.action):
      return '<{} - {}>\n'.format(self.action, self.state)
    else:
      return '<start - {}>\n'.format(self.state)