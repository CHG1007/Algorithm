import java.util.Scanner;


public class Main {
    static final int MOD = 1000000007;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] dp = new int[n+1];

        if (m<=n) {
            for (int i = 1; i <= m; i++) {
                dp[i] = 1;
            }
            dp[m] = dp[m]+1;

            for (int i = m+1; i <= n; i++) {
                dp[i] = (dp[i-1] + dp[i-m])%MOD;
            }

            System.out.println(dp[n]);

        } else {
            System.out.println(1);
        }
    }
}
