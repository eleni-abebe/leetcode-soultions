class Solution {
    public static int reverse(int x) {
    long fnum=0;
    while(x!=0)   {
        int y=x%10;
        fnum+=y;
        fnum=fnum*10;
        x =x/10;
    } 
    
    fnum=fnum/10;
    if(x<0){
        return (int) (-1*fnum);
    }
    if(fnum> Integer.MAX_VALUE|| fnum<Integer.MIN_VALUE){
        return 0;
    }
    return(int)fnum;

}
    public static void main(String[]args){
        int x=123;
        System.out.println(reverse(x));

    }
    }