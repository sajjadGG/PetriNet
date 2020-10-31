
class Petri_Net():
    
    def __init__(self , places , transitions , transition_weights , inhabitant_weight , initial_marking):
        """
        palces : tuple of places
        transitions : tuple of transitions
        transition_weight : list of elements each elements in format ((intuple),(outtupe)) 
        e.g. ((0,1,0,2),(1,0,0,0)) first element showing weight on in arc and second
        weight of out arc to places
        inhabitant_weight : for each transition have tuple of size places showing inhabitant weights
        e.g. (None , 3 , None , 2)
        """
        self.places = places
        self.transitions = transitions
        self.transition_weights = transition_weights
        self.inhabitant_weight = inhabitant_weight
        self.marking = initial_marking
    
    def force_makring(self , m):
        self.marking = m

    def check_condition(self  , tw , iw):
        """check if transition given with input transition weights as tw
            and inhabitant weight as iw is enabled under self.marking"""
        for i,p in enumerate(self.places):
            if(self.marking[i]<tw[i]):
                return False
            if(iw[i]!=None and self.marking[i]>=iw[i]):
                return False
        return True

    def enabled_transition(self):
        enabled = []
        for i , t in enumerate(self.transitions):
            if(self.check_condition(self.transition_weights[i][0] , self.inhabitant_weight[i])):
                enabled.append((i,t))                        
        return enabled

    def get_next_marking(self , i):
        """get future marking if transition i is fired
        transition i should be fireable"""
        inp = self.transition_weights[i][0]
        out = self.transition_weights[i][1]
        new_marking = tuple(m-inp[i]+out[i] for i ,m in enumerate(self.marking))
        return new_marking

    def fire_transition(self , i):
        """i : index of transition transition should be enabled"""
        inp = self.transition_weights[i][0]
        out = self.transition_weights[i][1]
        new_marking = tuple(m-inp[i]+out[i] for i ,m in enumerate(self.marking))
        self.marking = new_marking
        return new_marking

    def select_transition(self , enabled):
        """transition priority policy
            enabled should not be empty"""
        return 0
    
    def next(self):
        enabled = self.enabled_transition()
        if(enabled==[]):
            return False
        self.fire_transition(self.select_transition(enabled))

    def reachability_set(self):
        """return the reachability set of this petri net"""
        q = [self.marking,]
        reach_set = {self.marking }
        while(q!=[]):
            m = q.pop(0)
            reach_set.add(m)
            self.force_makring(m)
            enabled_trans = self.enabled_transition()
            for t in enabled_trans:
                next_marking = self.get_next_marking(t[0])
                if next_marking not in reach_set:
                    q.append(next_marking)
        return reach_set

    def __str__(self):
        return self.marking.__str__()
    

def test_petrinet():        
    # net = Petri_Net(("Plegs" , "Pfaces" , "Ptables") , ("t") , (((4,1,0) , (0,0,1)),) , ((None , None ,None),) , (19,9,3))
    # print(net)
    # net.next()
    # print(net)
    # net.next()
    # print(net)
    # net.next()
    # print(net)
    # net.next()
    # print(net)
    # print(net.reachability_set())
    net = Petri_Net(("p1" , "p2" , "p3" , "p4") , ("t1" , "t2" , "t3" , "t4") , 
    (((1,0,0,0) , (0,1,0,0)) , ((0,1,0,0) , (1,0,0,0)) , ((0,1,0,1) , (0,0,1,0)) , ((0,0,1,0) , (0,0,0,1))) , 
    ((None , None ,None,None),(None , None ,None,None),(None , None ,None,None),(None , None ,None,None)) , 
    (1,0,0,1))
    print(net.reachability_set())

test_petrinet()
        