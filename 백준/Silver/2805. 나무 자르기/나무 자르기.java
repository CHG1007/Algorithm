// BOJ 2805 - 나무 자르기
//
// 문제 요약
//  - 각 나무 높이가 주어질 때, 절단기 높이 H를 정해 절단 위의 부분만 잘라 모은다.
//  - 모은 나무 길이의 합이 최소 M 이상이 되도록 하면서, 가능한 H의 최댓값을 구한다.
//
// 풀이 개요 (매개변수 탐색 / 이분 탐색)
//  - 판별 함수 isEnough(H): 절단 높이를 H로 했을 때 모을 수 있는 나무 합이 M 이상인가?
//  - H가 클수록 모이는 양은 감소(단조성) → 이분 탐색으로 가능한 H의 최대값을 찾는다.
//
// 경계 설계 (요청 패턴)
//  - lo = 0 (가장 작을 수 있는 값보다 1 작은 느낌의 경계로 사용)
//  - hi = maxHeight + 1 (가능한 최댓값보다 1 큰 값)
//  - while (lo + 1 < hi) 유지 → 항상 lo와 hi 사이에 1칸 이상의 간격
//  - isEnough(mid) == true → lo = mid (조건 만족 범위를 위로 확대)
//    isEnough(mid) == false → hi = mid (조건 불만족이 시작되는 지점을 아래로 당김)
//  - 반복 종료 시, 정답은 lo (조건을 만족하는 최댓값)
//
// 구현 포인트
//  - 누적 합/연산은 long 사용 (최대치 합이 매우 클 수 있음)
//  - 입력 최적화: BufferedReader + StringTokenizer
//  - mid 계산 시 overflow 방지: lo + (hi - lo) / 2

import java.io.*;
import java.util.*;

public class Main {

    static int N;               // 나무의 수
    static long M;              // 필요한 나무 길이
    static int[] trees;         // 각 나무의 높이
    static int maxH;            // 최댓값(hi 경계 설정에 사용)

    public static void main(String[] args) throws Exception {
        // ===== 입력 =====
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Long.parseLong(st.nextToken());

        trees = new int[N];
        st = new StringTokenizer(br.readLine());
        maxH = 0;
        for (int i = 0; i < N; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
            if (trees[i] > maxH) {
                maxH = trees[i];
            }
        }

        // ===== 이분 탐색 (요청한 경계/반복 패턴) =====
        int lo = 0;           // 조건을 만족하는 "최댓값"을 담아갈 쪽
        int hi = maxH + 1;    // 조건을 만족하지 않는 첫 지점(상한)

        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2; // overflow 방지형 mid

            if (isEnough(mid)) {
                // mid 높이로 잘라도 M 이상 모임 → 더 높여도 되는지 확인
                lo = mid;
            } else {
                // mid 높이는 부족 → 더 낮춰야 함
                hi = mid;
            }
        }

        // lo는 조건(M 이상)을 만족하는 최대 절단 높이
        System.out.println(lo);
    }

    /**
     * 절단 높이를 h로 했을 때 M 이상을 모을 수 있는가?
     * @param h 절단 높이
     * @return 모이는 나무 합 >= M 이면 true, 아니면 false
     */
    static boolean isEnough(int h) {
        long sum = 0L;
        for (int height : trees) {
            if (height > h) {
                sum += (height - h);
                // (선택) 조기 종료: 이미 M 이상이면 더 볼 필요 없음
                if (sum >= M) {
                    return true;
                }
            }
        }
        return sum >= M;
    }
}
