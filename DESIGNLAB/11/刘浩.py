import lib601.dist as dist
import lib601.sm as sm
import lib601.ssm as ssm
import lib601.util as util

class StateEstimator(sm.SM):
    def __init__(self, model):
        self.model = model
        self.startState = model.startDistribution
    def getNextValues(self, state, inp):
        (o, i) = inp
        sGo = self.NewBayesEvidence(state, o)
        dSPrime = self.transitionUpdate(sGo)
        return (dSPrime, dSPrime)
    def NewBayesEvidence(self,state,observation):
        dict_final = {}
        state_name = state.support()
        Pr_sum = 0
        for name in state_name:
            dist.incrDictEntry(dict_final,name,self.model.observationDistribution(name).prob(observation)*state.prob(name))
            Pr_sum += dict_final[name]
        for i in dict_final.keys():#归一化
            dict_final[i] = dict_final[i] / Pr_sum
        print dict_final
        # print '归一化后的字典',dict_final
        return dist.DDist(dict_final)
    def transitionUpdate(self,belief):
        '''
        belief是Bays后的
        DDist(bad: 0.013699, good: 0.986301)
        DDist(bad: 0.757212, good: 0.242788)
        DDist(bad: 0.277355, good: 0.722645)
        '''
        dic_final = {}
        state_name = belief.support()
        for name in state_name:
            for name2 in state_name:
                dist.incrDictEntry(dic_final,name2,belief.prob(name)*self.model.transitionDistribution(0)(name).prob(name2))
        return dist.DDist(dic_final)



# Test

transitionTable = \
   {'good': dist.DDist({'good' : 0.7, 'bad' : 0.3}),
    'bad' : dist.DDist({'good' : 0.1, 'bad' : 0.9})}
observationTable = \
   {'good': dist.DDist({'perfect' : 0.8, 'smudged' : 0.1, 'black' : 0.1}),
    'bad': dist.DDist({'perfect' : 0.1, 'smudged' : 0.7, 'black' : 0.2})}

copyMachine = \
 ssm.StochasticSM(dist.DDist({'good' : 0.9, 'bad' : 0.1}),
                # Input is irrelevant; same dist no matter what
                lambda i: lambda s: transitionTable[s],
                lambda s: observationTable[s])
obs = [('perfect', 'step'), ('smudged', 'step'), ('perfect', 'step')]

cmse = StateEstimator(copyMachine)

print cmse.transduce(obs)


