class Solution {
public:
    string countAndSay(int n) {
        if(n==0)return "";
        if(n==1)return "1";
        if(n==2)return "11";
        string str="11";
        for(int i=3;i<=n;i++){
            str=str+'&';
            string temp="";
            int c=1;
            int len=str.length();
            for(int j=1;j<len;j++){
                if(str[j]!=str[j-1]){

                    temp=temp+to_string(c);
                    temp=temp+str[j-1];
           c=1;
                }
                else c++;

            }
            str=temp;
        }
     return str;

    }
};
