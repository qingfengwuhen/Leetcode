# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/3/18
-------------------------------------------------
   File Name：     solution22
   Description :
   Author :       zhaobx
   date：          12/3/18
-------------------------------------------------
   Change Activity:
                   12/3/18:
-------------------------------------------------
"""
"""
class Solution {
public:
    void dfs(int level, int l, int r, vector<string> &solution, string s, int n){
        if(2*n==level) solution.push_back(s);
        if(l<=n-1) 
            dfs(level+1, l+1, r, solution, s+'(', n);
        if(l>=r+1 && r<=n-1) 
            dfs(level+1, l, r+1, solution, s+')', n);
    }
    
    vector<string> generateParenthesis(int n) {
        vector<string>solution;
        dfs(0, 0, 0, solution, "", n);
        return solution;
    }
};
--------------------- 
作者：关关的刷题日记 
来源：CSDN 
原文：https://blog.csdn.net/Scarlett_Guan/article/details/79925151 
版权声明：本文为博主原创文章，转载请附上博文链接！

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string>re;
        if(n==0) return re;
        re.push_back("");
        for(int i=0; i<2*n; ++i){
            vector<string>temp;
            for(int i=0; i<re.size(); ++i){
                int l=0, r=0;
                for(char x: re[i]){
                    if(x=='(') ++l;
                    if(x==')') ++r;
                }
                if(l<n) temp.push_back(re[i]+'(');
                if(r+1<=l) temp.push_back(re[i]+')');
            }
            re=temp;
        }
        return re;
    }
};
--------------------- 
作者：关关的刷题日记 
来源：CSDN 
原文：https://blog.csdn.net/Scarlett_Guan/article/details/79925151 
版权声明：本文为博主原创文章，转载请附上博文链接！

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        queue<string>re;
        re.push("");
        int  level=0;
        while (level++!=2*n){
            int length=re.size();
            for (int i=0; i<length; ++i){
                string temp=re.front();
                re.pop();
                int l = 0, r = 0;
                for (auto y : temp){
                    if (y == '(') ++l;
                    if (y == ')') ++r;
                }
                if (l<n) re.push(temp + '(');
                if (r<l) re.push(temp + ')');
            }
        }
        vector<string>ans;
        while(!re.empty()){
            ans.push_back(re.front());
            re.pop();
        }
        return ans;
    }
};
--------------------- 
作者：关关的刷题日记 
来源：CSDN 
原文：https://blog.csdn.net/Scarlett_Guan/article/details/79925151 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def shiftRightPart(pre, l, nn):
            if nn == 1:
                return pre.append(l)
            else:
                result.append(pre + l)
                for i in range(nn-1):
                    temp = l[:]
                    # temp[nn+i], temp[nn-1-i] = temp[nn-1-i], temp[nn+i]
                    temp.pop(nn)
                    temp.insert(nn-i-1, ')')
                    result.append(pre+temp)
                    # for j in
                l = temp[2:]
                nn -= 1
                pre += ['(', ')']
                shiftRightPart(pre, l, nn)
        if n == 0:
            return []
        if n == 1:
            return ['()']
        l = []

        for i in range(2*n):
            if i < n:
                l.append('(')
            else:
                l.append(')')
        # print(l)
        shiftRightPart([], l, n)
        print(len(result))
        for i in range(len(result)):
            result[i] = ''.join(result[i])
        return result
    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.dfs('', [], 0, 0, n)

    def dfs(self, now_res, res, open, close, n):
        if len(now_res) == n * 2:
            res.append(now_res)
        if open < n:
            self.dfs(now_res + '(', res, open + 1, close, n)
        if close < open:
            self.dfs(now_res + ')', res, open, close + 1, n)
        return res

    def bfs(self, now_res, res, open, close, n):
        if len(now_res) == n * 2:
            res.append(now_res)
        if open < n:
            now_res += '('




s = Solution()
print(s.generateParenthesis2(1))
print(s.generateParenthesis2(2))
print(s.generateParenthesis2(3))
print(s.generateParenthesis2(4))
print(len(s.generateParenthesis2(4)))
