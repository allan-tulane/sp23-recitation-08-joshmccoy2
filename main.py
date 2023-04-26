
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
           # return(1 + min(MED(S, T[1:]), MED(S[1:], T)))
          inser = MED(S,T[1:]) + 1
          delet = MED(S[1:], T) + 1
          substi = MED(S[1:], T[1:]) + 1
          return min(inser,delet,substi)


def fast_MED(S, T, MED={}):
  if(S, T) in MED:
    return MED[(S,T)]
    
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S)) 
    else:
      if (S[0] == T[0]): 
        return(fast_MED(S[1:], T[1:])) 
      else:
        inser = fast_MED(S,T[1:]) + 1
        delet = fast_MED(S[1:], T) + 1
        substi = fast_MED(S[1:],T[1:]) + 1
        result = min(inser,delet,substi)
           
  MED[(S,T)] = result 
  return result

def fast_align_MED(S, T, MED={}):
  return fast_align_MED_helper(S, T, MED={})[1][0], fast_align_MED_helper(S, T, MED={})[1][1]

def fast_align_MED_helper(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]
    
  if S == "":
    alignment = ["-" * len(T), T]
    return len(T), alignment
  elif T == "":
    alignment = [S, "-" * len(S)]
    return len(S), alignment
  else:
    if S[0] == T[0]:
      sub_dist, sub_alignment = fast_align_MED_helper(S[1:], T[1:], MED)
      alignment = [S[0] + sub_alignment[0], T[0] + sub_alignment[1]]
      return sub_dist, alignment
    else:
      ins_dist, ins_alignment = fast_align_MED_helper(S, T[1:], MED)
      sub_dist, sub_alignment = fast_align_MED_helper(S[1:], T[1:], MED)
      del_dist, del_alignment = fast_align_MED_helper(S[1:], T, MED)
      
    
    if ins_dist <= del_dist and ins_dist <= sub_dist:
      alignment = ["-" + ins_alignment[0], T[0] + ins_alignment[1]]
      return ins_dist + 1, alignment
    elif del_dist <= sub_dist:
      alignment = [S[0] + del_alignment[0], "-" + del_alignment[1]]
      return del_dist + 1, alignment
    else:
      alignment = [S[0] + sub_alignment[0], T[0] + sub_alignment[1]]
      return sub_dist + 1, alignment


def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        print(align_S, align_T)
        print(alignments[i][0],alignments[i][1])
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

