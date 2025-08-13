import java.io.*;
import java.util.*;

/*
 *  장훈이의 높은 선반 D4
 */
public class Solution {

    static int ans;     	// 정답 (최소 높이)
    static int B;       	// 선반 높이 기준
    static int N;       	// 점원 수
    static int[] height; 	// 점원 키 배열

    public static void main(String[] args) throws Exception {
        // 입력 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine().trim());

        for (int tc = 0; tc < t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());

            height = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                height[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(height);

            int max_man = 0;  // 최대 가능 인원
            ans = (int)1e9;   // 정답
            int total = 0;    // 최대 가능 인원 판단 임시 누적값

            // 가장 작은 키부터 누적하여 B 이상이 되는 인원 수를 max_man으로 설정
            for (int i = 0; i < N; i++) {
                total += height[i];
                if (total >= B) {
                    max_man = i + 1;
                    break;
                }
            }
            // 1명부터 최대 가능 인원까지 탑을 쌓는 모든 경우에 대해
            for (int man = 1; man <= max_man; man++) {
                // start = 0, picked = 0, currentSum = 0 로 시작
                combine(0, 0, man, 0);
            }
            // 높이 b 감소 후 출력
            sb.append('#').append(tc + 1).append(' ').append(ans - B).append('\n');
        }
        System.out.print(sb.toString());
    }

    /**
     *   start: 조합에서 다음으로 고를 인덱스 시작 위치
     *   picked: 현재까지 고른 원소(점원) 수
     *   man: 이번에 만들 조합의 목표 인원 수 
     *   currentSum: 현재까지 고른 점원 키 합
     */
    static void combine(int start, int picked, int man, int currentSum) {
        // 조합이 완성되었다면 (picked == man)
        if (picked == man) {
            // 탑의 높이가 b 이상이면 정답 갱신
            if (currentSum >= B) {
                ans = Math.min(ans, currentSum);
            }
            return;
        }

        // 남은 원소 수가 부족하면 종료
        // (i가 선택 가능한 마지막 시작점은 N - (man - picked))
        for (int i = start; i <= N - (man - picked); i++) {
            // 다음 원소 선택
            combine(i + 1, picked + 1, man, currentSum + height[i]);
        }
    }
}
