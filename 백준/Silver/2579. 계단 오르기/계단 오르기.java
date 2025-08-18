// BOJ 2579 - 계단 오르기
//
// 문제 요약
//  - 각 계단(1..N)에 점수가 있고, 계단을 밟으면 그 점수를 획득함.
//  - 한 번에 1칸 또는 2칸 오를 수 있음.
//  - "세 칸 연속으로" 밟을 수 없음(= 연속 3계단 금지).
//  - 반드시 마지막 계단(N)을 밟아야 함.
//  - 최대 점수를 구하라.
//
// 풀이 개요 (동적 계획법 - DP)
//  - 상태 정의(2차원 DP, 연속 밟은 횟수 관점):
//    dp[i][0] : i번째 계단을 밟으며 도착했을 때의 최대 점수, 직전 계단(i-1)을 밟지 않고 i-2에서 바로 온 경우
//               → "연속 1칸 밟기 아님"(끊고 온 상태)
//    dp[i][1] : i번째 계단을 밟으며 도착했을 때의 최대 점수, 직전 계단(i-1)도 밟은 경우
//               → "연속 2칸째" (i-2 → i-1 → i)
//
//  - 점화식:
//    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + score[i]
//      (i-2에서 건너와 i만 밟으므로 연속이 끊김 → i-2에서 어떤 방식으로 왔든 상관없음)
//    dp[i][1] = dp[i-1][0] + score[i]
//      (i-1도 밟았으므로 그 전(i-2)은 반드시 끊겨야 함 → dp[i-1]의 "연속 아님" 상태에서만 올 수 있음)
//
//  - 초기값(기저):
//    dp[1][0] = score[1], dp[1][1] = 불가(0으로 두고 사용 안 함)
//    dp[2][0] = score[2]                  (0 → 2)
//    dp[2][1] = score[1] + score[2]       (1 → 2)
//    (N=1, N=2는 별도 처리)
//  - 정답: max(dp[N][0], dp[N][1])
//
//  - 시간 복잡도: O(N)
//  - 메모리: O(N)

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        // ===== 입력 =====
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        int[] score = new int[N + 1]; // 1-indexed
        for (int i = 1; i <= N; i++) {
            score[i] = Integer.parseInt(br.readLine().trim());
        }

        // 예외 처리: N이 1 또는 2인 경우 바로 계산하여 출력
        if (N == 1) {
            System.out.println(score[1]);
            return;
        }
        if (N == 2) {
            int ans2 = score[1] + score[2];
            if (score[2] > ans2) {
                // 논리상 발생하진 않지만, 이해를 돕기 위해 if 형태 유지
                ans2 = score[2];
            }
            System.out.println(ans2);
            return;
        }

        // ===== DP 테이블 =====
        int[][] dp = new int[N + 1][2];
        // i=1
        dp[1][0] = score[1];   // 0→1
        dp[1][1] = 0;          // 불가 상태(사용하지 않음)

        // i=2
        dp[2][0] = score[2];           // 0→2 (i-2에서 바로 i로)
        dp[2][1] = score[1] + score[2]; // 1→2 (연속 2칸째)

        // i=3..N
        for (int i = 3; i <= N; i++) {
            int fromI2Max = dp[i - 2][0];
            if (dp[i - 2][1] > fromI2Max) {
                fromI2Max = dp[i - 2][1];
            }
            dp[i][0] = fromI2Max + score[i];   // i-2에서 끊고 i 밟기

            dp[i][1] = dp[i - 1][0] + score[i]; // i-1도 밟으므로 직전은 반드시 끊긴 상태
        }

        // ===== 정답 =====
        int ans = dp[N][0];
        if (dp[N][1] > ans) {
            ans = dp[N][1];
        }
        System.out.println(ans);
    }
}
