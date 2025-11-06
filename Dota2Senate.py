class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)  # convert to list so we can append banned senators to the end
        cnt = i = 0  # cnt: net advantage (R positive, D negative); i: current index
        while i < len(senate):  # iterate over evolving queue
            c = senate[i]
            if c == 'R':
                if cnt < 0:
                    senate.append('D')  # D had bans waiting, so this R is banned -> schedule a D later
                cnt += 1  # R increases net advantage
            else:
                if cnt > 0:
                    senate.append('R')  # R had bans waiting, so this D is banned -> schedule an R later
                cnt -= 1  # D decreases net advantage
            i += 1  # move to next senator in queue
        return "Radiant" if cnt > 0 else "Dire"  # positive cnt -> Radiant wins, else Dire