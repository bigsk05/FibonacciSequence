public class MainClass {
    public static void main(String[] args) {
        long startTime=System.nanoTime();
        for (int counter = 0; counter < 30; counter++){
            calc(counter);
            //System.out.printf("%d\n", calc(counter));
        }
        long endTime=System.nanoTime();
        System.out.printf("[%f]\n",(endTime-startTime)/1000000000.0);
    }

    public static long calc(long n) {
        if (n <= 1)
            return n;
        else
            return (calc(n - 1) + calc(n - 2));
    }
}