class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        diction = {}
        already_id = []
        for u_id, time in logs:
            if u_id in already_id:
                if time not in diction[u_id]["list"]:
                    diction[u_id]["uam"] +=1
                diction[u_id]["list"].append(time)
            else:
                diction[u_id] = {"list":[time]}
                diction[u_id]["uam"] = 1
                already_id.append(u_id)
        
        # # Finding UAM of each user
        # for u_id in diction:
        #     diction[u_id]["uam"] = len(set(diction[u_id]["list"]))
        ans = []
        for j in range(1,k+1):
            count=0
            for u_id in diction:
                if diction[u_id]["uam"] == j:
                    count+=1
            ans.append(count)
        return ans
# TLE
