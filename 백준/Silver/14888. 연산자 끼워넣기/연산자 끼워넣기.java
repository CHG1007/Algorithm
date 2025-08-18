// BOJ 14888 - 연산자 끼워넣기
// 풀이 개요:
// 1) N개의 수와 4종류(+, -, *, /) 연산자의 개수가 주어진다.
// 2) 모든 수의 순서는 고정, 연산자의 배치 순서만 바꿀 수 있다.
// 3) 가능한 모든 연산자 배치를 완전탐색(백트래킹)하여 최댓값/최솟값을 구한다.
//
// 핵심 포인트:
// - DFS(백트래킹)로 연산자 개수를 소모해가며 다음 값으로 진행
// - 연산 결과는 오버플로우 방지를 위해 long 사용
// - Java의 정수 나눗셈은 음수에 대해 0을 기준으로 절삭(문제 조건과 일치)

import java.io.*;
import java.util.*;

public class Main {

    static int N;               // 숫자 개수
    static long[] A;            // 숫자 배열 (연산 중 안전을 위해 long 사용)
    static int[] ops = new int[4]; // 연산자 개수: [+, -, *, /] 순서

    static long maxVal = Long.MIN_VALUE; // 가능한 식의 최댓값
    static long minVal = Long.MAX_VALUE; // 가능한 식의 최솟값

    public static void main(String[] args) throws Exception {
        // ===== 입력 =====
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine().trim());

        A = new long[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(st.nextToken());
        }

        // 연산자 개수 입력: +, -, *, /
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            ops[i] = Integer.parseInt(st.nextToken());
        }

        // ===== 탐색 시작 =====
        // 시작 값은 첫 번째 수, 다음에 올 인덱스는 1 (두 번째 수부터 사용)
        dfs(1, A[0]);

        // ===== 출력 =====
        StringBuilder sb = new StringBuilder();
        sb.append(maxVal).append('\n').append(minVal);
        System.out.println(sb);
    }

    /**
     * 백트래킹 DFS
     * @param idx   현재 사용할 숫자의 인덱스 (A[idx]를 사용할 차례)
     * @param cur   지금까지의 계산 결과
     */
    static void dfs(int idx, long cur) {
        // 모든 숫자를 다 사용했다면 최댓값/최솟값 갱신
        if (idx == N) {
            if (cur > maxVal) {
                maxVal = cur;
            }
            if (cur < minVal) {
                minVal = cur;
            }
            return;
        }

        // 4종류 연산자를 하나씩 시도
        for (int op = 0; op < 4; op++) {
            // 해당 연산자가 남아있는지 확인
            if (ops[op] > 0) {
                // 사용(소모)
                ops[op]--;

                long next = apply(cur, A[idx], op);
                // 다음 숫자 인덱스로 진행
                dfs(idx + 1, next);

                // 복구(백트래킹)
                ops[op]++;
            }
        }
    }

    /**
     * 두 수 a, b에 대해 op 연산을 적용한 결과를 반환
     * op: 0(+) 1(-) 2(*) 3(/)
     * Java의 정수 나눗셈은 0을 기준으로 버림(음수 포함) -> 문제 규칙과 동일
     */
    static long apply(long a, long b, int op) {
        long result = 0;

        if (op == 0) {          // +
            result = a + b;
        } else if (op == 1) {   // -
            result = a - b;
        } else if (op == 2) {   // *
            result = a * b;
        } else if (op == 3) {   // /
            // 문제에서 0으로 나누는 입력은 주어지지 않는다고 가정 (BOJ 공식 테스트)
            // Java의 long 나눗셈은 0을 기준으로 절삭
            result = a / b;
        }

        return result;
    }
}
