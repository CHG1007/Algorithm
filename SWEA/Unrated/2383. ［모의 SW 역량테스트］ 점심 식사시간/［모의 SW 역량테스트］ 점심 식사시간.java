import java.io.*;
import java.util.*;


public class Solution {

    // 사람, 계단 좌표 및 계단 길이 보관용
    static class Pos {
        int r, c;
        Pos(int r, int c) { this.r = r; this.c = c; }
    }
    static class Stair {
        int r, c, k; // 위치 (r,c), 계단 길이 k
        Stair(int r, int c, int k) { this.r = r; this.c = c; this.k = k; }
    }

    static int N;
    static List<Pos> people;   // 사람 좌표 목록
    static Stair[] stairs;     // 계단 2개
    static int P;              // 사람 수
    static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine().trim());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine().trim());
            people = new ArrayList<>();
            stairs = new Stair[2];

            // 입력 파싱: 1=사람, 2~10=계단(값이 곧 K)
            int stairIdx = 0;
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    int v = Integer.parseInt(st.nextToken());
                    if (v == 1) people.add(new Pos(i, j));          // 사람 위치
                    else if (v >= 2) stairs[stairIdx++] = new Stair(i, j, v); // 계단 위치+길이
                }
            }

            P = people.size();
            answer = Integer.MAX_VALUE;

            // 모든 배정(부분집합) 탐색: bit가 0이면 stair0, 1이면 stair1로 보냄
            // P<=10 -> 최대 1024가지
            for (int mask = 0; mask < (1 << P); mask++) {
                List<Integer> arr0 = new ArrayList<>(); // 계단0 도착시간들
                List<Integer> arr1 = new ArrayList<>(); // 계단1 도착시간들

                for (int i = 0; i < P; i++) {
                    Pos p = people.get(i);
                    // 계단까지 맨해튼 거리 = 이동 시간
                    int d0 = Math.abs(p.r - stairs[0].r) + Math.abs(p.c - stairs[0].c);
                    int d1 = Math.abs(p.r - stairs[1].r) + Math.abs(p.c - stairs[1].c);

                    if ((mask & (1 << i)) == 0) arr0.add(d0); // stair0 선택
                    else arr1.add(d1);                        // stair1 선택
                }

                int time0 = simulate(arr0, stairs[0].k); // 계단0 완료 시간
                int time1 = simulate(arr1, stairs[1].k); // 계단1 완료 시간
                int finish = Math.max(time0, time1);     // 두 계단 모두 끝나는 시각

                if (finish < answer) answer = finish;
                // 가지치기: 이미 최소값보다 커지면 더 볼 필요 없음(하지만 여기서는 단순)
            }

            sb.append('#').append(tc).append(' ').append(answer).append('\n');
        }

        System.out.print(sb.toString());
    }

    /**
     * 한 계단에 배정된 사람들의 "입구 도착 시간 목록(arrivals)"과
     * 계단 길이 K가 주어질 때, 이 계단을 통해 모든 사람이 내려가
     * 이동을 완료하는 시간을 반환.
     */
    static int simulate(List<Integer> arrivals, int K) {
        if (arrivals.isEmpty()) return 0; // 배정된 사람이 없으면 0분

        // 도착 시간을 오름차순으로 처리
        Collections.sort(arrivals);

        // 현재 계단을 내려가는 사람들의 "종료 시각"을 담는 최소 힙
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int last = 0; // 이 계단에서 가장 늦게 끝나는 시각

        for (int a : arrivals) {
            // a 시각까지 이미 내려가 끝난 사람은 큐에서 제거
            while (!pq.isEmpty() && pq.peek() <= a) pq.poll();

            int start; // 이 사람이 계단에 발을 딛는 시각(첫 칸)
            if (pq.size() >= 3) {
                // 이미 3명이 내려가는 중 -> 가장 빨리 끝나는 사람의 종료 시각까지 대기
                int earliestFinish = pq.poll(); // 가장 이른 종료 시각
                // 도착 후 1분 대기 규칙과 자리가 비는 시각을 함께 고려
                start = Math.max(a + 1, earliestFinish);
            } else {
                // 자리 여유가 있으면 도착 1분 뒤 바로 진입
                start = a + 1;
            }

            int end = start + K; // 계단 길이 K만큼 이동 후 종료
            pq.offer(end);
            if (end > last) last = end;
        }

        // pq에 남은 종료 시각들 중 최대가 실제 완료 시각
        // (루프에서 last로 추적했으므로 바로 반환해도 무방)
        return last;
    }
}
