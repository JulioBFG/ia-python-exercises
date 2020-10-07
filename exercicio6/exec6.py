from UninformedSearch import UninformedSearch
from UninformedSearch import algorithms

city = {
    'ARAD': ['arad', 366],
    'SIBIU': ['sibiu', 253],
    'TIMISUARA': ['timisuara', 329],
    'ZERIND': ['zerind', 374],
    'FAGARAS': ['fagaras', 176],
    'ORADEA': ['oradea', 380],
    'RIMNICU': ['rimnicu', 193],
    'BUCHAREST': ['bucharest', 0],
    'PITESTI': ['pitesti', 100],
    'CRAIOVA': ['craiova', 160],
    'LUGOJ': ['lugoj', 244],
    'MEHADIA': ['mehadia', 241],
    'DOBRETA': ['dobreta', 242]
}

actions = {
    'MOVETOARAD': 'move-to-arad',
    'MOVETOSIBIU': 'move-to-sibiu',
    'MOVETOTIMISUARA': 'move-to-timisuara',
    'MOVETOZERIND': 'move-to-zerind',
    'MOVETOFAGARAS': 'move-to-fagaras',
    'MOVETOORADEA': 'move-to-radea',
    'MOVETORIMNICU': 'move-to-rimnicu',
    'MOVETOBUCHAREST': 'move-to-bucharest',
    'MOVETOPITESTI': 'move-to-pitesti',
    'MOVETOCRAIOVA': 'move-to-craiova',
    'MOVETOLUGOJ': 'move-to-lugoj',
    'MOVETOMEHADIA': 'move-to-mehadia',
    'MOVETODOBRETA': 'move-to-dobreta',
}

effort = {
  'ARADTOZERIND': 75,
  'ARADTOSIBIU': 140,
  'ARADTOTIMISUARA': 118
}

class Astar:
  def __init__(self, localCity, effort=0):
    self.localCity = localCity
    self.effort = effort
  
  def getActions(self):
    list = []
    
    if (self.localCity == city['ARAD']):
      list.append(actions["MOVETOSIBIU"])
      list.append(actions["MOVETOTIMISUARA"])
      list.append(actions["MOVETOZERIND"])
    elif (self.localCity == city["ZERIND"]):
      list.append(actions["MOVETOARAD"])
      list.append(actions["MOVETOORADEA"])
    elif (self.localCity == city["TIMISUARA"]):
      list.append(actions["MOVETOARAD"])
      list.append(actions["MOVETOLUGOJ"])
    elif (self.localCity == city["SIBIU"]):
      list.append(actions["MOVETOARAD"])
      list.append(actions["MOVETOFAGARAS"])
      list.append(actions["MOVETOORADEA"])
      list.append(actions["MOVETORIMNICU"])
    elif (self.localCity == city["ORADEA"]):
      list.append(actions["MOVETOZERIND"])
      list.append(actions["MOVETOSIBIU"])
    elif (self.localCity == city["FAGARAS"]):
      list.append(actions["MOVETOSIBIU"])
      list.append(actions["MOVETOBUCHAREST"])
    elif (self.localCity == city["RIMNICU"]):
      list.append(actions["MOVETOSIBIU"])
      list.append(actions["MOVETOPITESTI"])
      list.append(actions["MOVETOCRAIOVA"])
    elif (self.localCity == city["PITESTI"]):
      list.append(actions["MOVETORIMNICU"])
      list.append(actions["MOVETOBUCHAREST"])
      list.append(actions["MOVETOCRAIOVA"])
    elif (self.localCity == city["CRAIOVA"]):
      list.append(actions["MOVETORIMNICU"])
      list.append(actions["MOVETOPITESTI"])
      list.append(actions["MOVETODOBRETA"])
    elif (self.localCity == city["LUGOJ"]):
      list.append(actions["MOVETOTIMISUARA"])
      list.append(actions["MOVETOMEHADIA"])
    elif (self.localCity == city["MEHADIA"]):
      list.append(actions["MOVETOLUGOJ"])
      list.append(actions["MOVETODOBRETA"])
    elif (self.localCity == city["DOBRETA"]):
      list.append(actions["MOVETOCRAIOVA"])
      list.append(actions["MOVETOMEHADIA"])

    return list

  def doAction(self, action):    
    state = self.clone()

    if (action == actions["MOVETOARAD"]):
      if(state.localCity == city["SIBIU"]):
        state.effort = 140 g() --> custo h() --> heuristica/estimativa
       elif(state.localCity == city["TIMISUARA"]):
        state.effort = 118
      elif(state.localCity == city["ZERIND"]):
        state.effort = 75

      state.localCity = city["ARAD"]
    elif (action == actions["MOVETOSIBIU"]):
      if(state.localCity == city["ARAD"]):
        state.effort = 140
      elif(state.localCity == city["FAGARAS"]):
        state.effort = 99
      elif(state.localCity == city["RIMNICU"]):
        state.effort = 80
      elif(state.localCity == city["ORADEA"]):
        state.effort = 151

      state.localCity = city["SIBIU"]
    elif (action == actions["MOVETOTIMISUARA"]):
      if(state.localCity == city["ARAD"]):
        state.effort = 118
      elif(state.localCity == city["LUGOJ"]):
        state.effort = 111
      
      state.localCity = city["TIMISUARA"]
    elif (action == actions["MOVETOZERIND"]):
      if(state.localCity == city["ARAD"]):
        state.effort = 75
      elif(state.localCity == city["ORADEA"]):
        state.effort = 71
      
      state.localCity = city["ZERIND"]
    elif (action == actions["MOVETOFAGARAS"]):
      if(state.localCity == city["SIBIU"]):
        state.effort = 99
      
      state.localCity = city["FAGARAS"]
    elif (action == actions["MOVETOORADEA"]):
      if(state.localCity == city["SIBIU"]):
        state.effort = 151
      elif(state.localCity == city["ZERIND"]):
        state.effort = 71
      
      state.localCity = city["ORADEA"]
    elif (action == actions["MOVETORIMNICU"]):
      if(state.localCity == city["SIBIU"]):
        state.effort = 80

      state.localCity = city["RIMNICU"]
    elif (action == actions["MOVETOBUCHAREST"]):
      if(state.localCity == city["FAGARAS"]):
        state.effort = 211
      
      state.localCity = city["BUCHAREST"]
    elif (action == actions["MOVETOPITESTI"]):
      if(state.localCity == city["RIMNICU"]):
        state.effort = 97
      
      state.localCity = city["PITESTI"]
    elif (action == actions["MOVETOCRAIOVA"]):
      if(state.localCity == city["RIMNICU"]):
        state.effort = 146

      state.localCity = city["CRAIOVA"]
    elif (action == actions["MOVETOLUGOJ"]):
      if(state.localCity == city["TIMISUARA"]):
        state.effort = 111
      
      state.localCity = city["LUGOJ"]
    elif (action == actions["MOVETOMEHADIA"]):
      if(state.localCity == city["LUGOJ"]):
        state.effort = 70
      
      state.localCity = city["MEHADIA"]
    elif (action == actions["MOVETODOBRETA"]):
      
      state.localCity = city["DOBRETA"]
    
    return state

  def equals(self, o):
    return o.localCity == self.localCity

  def clone(self):
    return Astar(
      self.localCity)

  def __str__(self):
    return '<local city: {}>'.format(self.localCity)

initial = Astar(city["ARAD"])
finals = [
  Astar(city["BUCHAREST"])
]

problem = UninformedSearch(initial, finals)
result = problem.search(algorithms["DSF"])

if (result):
  for r in result:
    print(r)