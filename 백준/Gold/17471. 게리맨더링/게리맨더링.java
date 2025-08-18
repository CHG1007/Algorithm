// BOJ 17471 - 게리맨더링
// 부분집합으로 두 선거구로 나누고, 각 선거구가 연결인지 BFS로 확인.
// 연결이면 인구수 차이 최소값 갱신. 불가능하면 -1 출력.

import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int[] pop;                 // 인구수 (1-indexed)
    static ArrayList<Integer>[] g;    // 인접 리스트 (1-indexed)
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine().trim());
        pop = new int[N + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            pop[i] = Integer.parseInt(st.nextToken());
        }

        g = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) g[i] = new ArrayList<>();

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            for (int k = 0; k < m; k++) {
                int v = Integer.parseInt(st.nextToken());
                g[i].add(v);
                g[v].add(i); // 무방향
            }
        }

        // 모든 분할 시도: bitmask (1..(1<<N)-2), 공집합/전집합 제외
        int totalMasks = 1 << N;
        for (int mask = 1; mask <= totalMasks - 2; mask++) {
            // 그룹 A: bit가 1인 정점들, B: 나머지
            if (isConnected(mask, true) && isConnected(mask, false)) {
                int diff = Math.abs(sumPopulation(mask, true) - sumPopulation(mask, false));
                if (diff < answer) {
                    answer = diff;
                }
            }
        }

        if (answer == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }
    }

    // 해당 mask 기준으로 그룹(A 또는 B)의 연결 여부를 BFS로 확인
    static boolean isConnected(int mask, boolean groupA) {
        boolean[] inGroup = new boolean[N + 1];
        int count = 0;

        for (int i = 1; i <= N; i++) {
            boolean inA = ((mask & (1 << (i - 1))) != 0);
            if (groupA) {
                if (inA) {
                    inGroup[i] = true;
                    count++;
                }
            } else {
                if (!inA) {
                    inGroup[i] = true;
                    count++;
                }
            }
        }

        if (count == 0) return false; // 그룹 비어있음

        // BFS 시작점 찾기
        int start = -1;
        for (int i = 1; i <= N; i++) {
            if (inGroup[i]) {
                start = i;
                break;
            }
        }

        // 연결 카운트
        boolean[] visited = new boolean[N + 1];
        ArrayDeque<Integer> q = new ArrayDeque<>();
        visited[start] = true;
        q.add(start);
        int visitCnt = 1;

        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int nxt : g[cur]) {
                if (inGroup[nxt] && !visited[nxt]) {
                    visited[nxt] = true;
                    visitCnt++;
                    q.add(nxt);
                }
            }
        }

        return visitCnt == count;
    }

    // 해당 mask 기준으로 그룹(A 또는 B)의 인구 합계
    static int sumPopulation(int mask, boolean groupA) {
        int sum = 0;
        for (int i = 1; i <= N; i++) {
            boolean inA = ((mask & (1 << (i - 1))) != 0);
            if (groupA) {
                if (inA) sum += pop[i];
            } else {
                if (!inA) sum += pop[i];
            }
        }
        return sum;
    }
}
