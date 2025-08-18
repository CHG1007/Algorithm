// BOJ 12865 - 평범한 배낭
//
// 문제 요약
//  - 각 물건 i는 (무게 w_i, 가치 v_i)를 가진다.
//  - 배낭이 버틸 수 있는 최대 무게 K를 넘지 않도록 물건을 골라,
//    담은 물건들의 "가치 합"의 최댓값을 구한다.
//  - 각 물건은 "최대 1번"만 담을 수 있다. (0/1 Knapsack)
//
// 풀이 개요 (정석 DP - 1차원 최적화)
//  - dp[w] := 배낭 용량이 정확히 w일 때 얻을 수 있는 최대 가치
//  - 각 물건 (weight, value)에 대해 w = K..weight (내림차순)으로 갱신:
//      dp[w] = max(dp[w], dp[w - weight] + value)
//    ※ 내림차순이 핵심: 같은 물건을 같은 라운드에 중복 사용하지 않도록 함.
//  - 정답은 dp[0..K] 중 최댓값이지만,
//    위 점화식 구조에서는 dp[K]가 "용량 K에서의 최대 가치"이므로 그대로 출력 가능.
//
// 시간 복잡도: O(N*K), 메모리: O(K)

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        // ===== 입력 =====
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 물건 개수
        int K = Integer.parseInt(st.nextToken()); // 배낭 최대 무게

        // 물건 정보를 저장할 배열
        int[] W = new int[N]; // 무게
        int[] V = new int[N]; // 가치

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken());
            V[i] = Integer.parseInt(st.nextToken());
        }

        // ===== DP 배열 =====
        int[] dp = new int[K + 1]; // 기본 0으로 초기화

        // ===== 0/1 Knapsack 점화식 적용 =====
        for (int i = 0; i < N; i++) {
            int weight = W[i];
            int value = V[i];

            // 역방향 순회가 핵심: 같은 라운드에서 동일 물건의 중복 사용 방지
            for (int w = K; w >= weight; w--) {
                int candidate = dp[w - weight] + value;
                if (candidate > dp[w]) {
                    dp[w] = candidate;
                }
            }
        }

        // ===== 결과 출력 =====
        // 용량 K에서의 최대 가치
        System.out.println(dp[K]);
    }
}
