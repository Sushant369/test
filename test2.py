class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        elif len(strs)==1:
            return strs[0]
        else:
            lengths=[]
            for s in strs:
                lengths.append(len(s))
            min_str_index=lengths.index(min(lengths))
            
            dict={}
            for s in strs[min_str_index]:
                dict[s]=0

            for i in range(len(strs)):
                if i == min_str_index:
                    continue

                k=0
                for s in strs[min_str_index]:
                    # print(s)
                    # print(strs[i][k])
                    if s==strs[i][k]:
                        dict[s]+=1
                    k=k+1
            print(dict)
            list=[]
            count=0
            for val in dict:
                list.append(dict[val])
            for i in range(1,len(list)):
                if list[0]==list[i]:
                    count=count+1
                
            output_str=""
            # if count==1:
            #     return strs[min_str_index]

            # if count>0:


            if count !=0:
                for i in range(count+1):
                    output_str+=strs[min_str_index][i]
            print(output_str)

            return output_str
sol=Solution()
sol.longestCommonPrefix(["aa","aa","aa"])







        
