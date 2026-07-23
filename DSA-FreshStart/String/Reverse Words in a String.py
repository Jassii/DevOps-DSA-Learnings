class Solution:
    def reverseWords(self, s: str) -> str:
        #Brute force approach
        # s = s.strip()
        # list_words = s.split(" ")
        # start=0
        # end=len(list_words)-1
        # while(start<end):
        #     list_words[start],list_words[end]=list_words[end],list_words[start]
        #     start+=1
        #     end-=1
        # # res = " ".join(list_words)
        # res=""
        # for word in list_words:
        #     if(word!=""):
        #         res = res+word+" "
        # res = res.strip()
        # return res


        list_words=s.split()
        return " ".join(list_words[::-1])
