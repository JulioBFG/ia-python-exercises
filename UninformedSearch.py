from CandidateState import *
#import json
class algorithms(object):
    DSF = 'dsf'
    BSF = 'bsf'

class UninformedSearch(object):
    algs = algorithms()

    def __init__(self, initialState, finalStates):
        self.initialState = initialState
        self.finalStates = finalStates

    def search(self, type=algs.BSF):
        
        visited = []

        candidate = CandidateState(self.initialState)
        pending = [candidate]

        i = 0

        while pending.count():
            candidate = type == algs.DSF if pending.pop() else pending.pop(0)
            i += 1

            if i % 1000 == 0:
                print(i)

            if self.finalStates.find(self.state.equals(candidate.state)):
                result = []

                while candidate:
                    result.append(candidate)
                    candidate = candidate.parent

                return result.reverse()

            else:
                visited.append(candidate.state)

                successors = candidate.getSuccessors

                for sucessor in successors:
                    if(not visited.find(self.state.equals(sucessor.state))):
                        pending.append(self.successor)

        return None

