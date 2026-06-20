class Solution(object):
    def mostWordsFound(self, sentences):
        space_num=0
        for i in sentences:
            count=0
            for j in i:
                if j.isspace():
                    count+=1
            if count>space_num:
                space_num=count
        word_num=space_num+1
        return word_num