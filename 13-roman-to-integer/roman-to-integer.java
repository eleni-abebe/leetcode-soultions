class Solution {
    public int romanToInt(String s) {
        int answer =0,num =0,prev =0;
        for(int j=s.length()-1;j>=0;j--){
            switch(s.charAt(j)) {
                case 'M' : num=1000;
                    break;
                case 'D':num=500;
                    break;
                case 'C' :num=100;
                    break;
                case 'L' :num=50;
                    break;
                case 'X' :num=10;
                    break;
                case 'V' :num=5;
                    break;
                case 'I' :num=1;
            }
            if(num <prev){
                answer-=num;
            }
            else{
                answer+=num;
            }
            prev=num;
        }
        return answer;
    }









            }
   