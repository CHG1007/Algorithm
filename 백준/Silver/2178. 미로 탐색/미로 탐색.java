// BOJ 2178 - 미로 탐색
// 문제 요약:
//  - N x M 미로에서 (1,1) -> (N,M) 까지 이동할 때 지나야 하는 최소 칸 수를 구하는 문제
//  - 1: 이동 가능, 0: 이동 불가
//  - 상하좌우로 인접한 칸만 이동 가능
//
// 풀이 개요(정석):
//  - "가중치가 모두 동일(1칸 이동 = 1비용)"하므로 BFS로 최단 거리(=최소 칸 수)를 구한다.
//  - dist[r][c] := 시작점에서 (r,c)까지 도달하는 데 필요한 칸 수
//  - 시작 dist[0][0] = 1 로 시작하여, 인접한 방문 가능한 칸에 대해 dist = 이전 dist + 1 로 갱신
//
// 구현 포인트:
//  - 입력: BufferedReader, 첫 줄에 N, M, 이후 N줄의 미로(공백 없이 '0','1')
//  - 큐: ArrayDeque<int[]> 사용 (int[]{r, c})
//  - 방문 체크: boolean[][] visited
//  - 방향 벡터: 상/하/좌/우 4방 탐색
//  - 출력: dist[N-1][M-1]

import java.io.*;
import java.util.*;

public class Main {

    static int N, M;                   // 행(N), 열(M)
    static int[][] map;                // 미로 (1: 이동 가능, 0: 불가)
    static int[][] dist;               // 최단 거리(칸 수) 기록
    static boolean[][] visited;        // 방문 여부
    static int[] dr = {-1, 1, 0, 0};   // 상, 하, 좌, 우
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        // ===== 입력 =====
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        dist = new int[N][M];
        visited = new boolean[N][M];

        // 미로 입력 (공백 없이 '0'과 '1'로 이루어진 문자열)
        for (int i = 0; i < N; i++) {
            String line = br.readLine().trim();
            for (int j = 0; j < M; j++) {
                // 문자 '0' 또는 '1'을 정수로 변환
                map[i][j] = line.charAt(j) - '0';
            }
        }

        // ===== BFS로 최단 거리 계산 =====
        bfs(0, 0);

        // ===== 결과 출력 =====
        // dist[N-1][M-1]에는 시작점에서 도착점까지의 최소 칸 수가 저장됨
        System.out.println(dist[N - 1][M - 1]);
    }

    /**
     * 시작 좌표 (sr, sc)에서 BFS를 수행하여 dist를 채운다.
     * 도달 불가한 경우 dist는 기본값(0)으로 남지만, 본 문제는 도달 가능한 입력이 주어진다.
     */
    static void bfs(int sr, int sc) {
        ArrayDeque<int[]> q = new ArrayDeque<>();

        // 시작점 초기화
        visited[sr][sc] = true;
        dist[sr][sc] = 1; // 시작 칸도 카운트에 포함
        q.add(new int[]{sr, sc});

        // 큐가 빌 때까지 탐색
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0];
            int c = cur[1];

            // (선택) 도착점에 도달하면 더 이상 진행할 필요 없음 -> break
            // if (r == N - 1 && c == M - 1) break;

            // 4방향 이웃 탐색
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                // 1) 범위 내부인지
                if (nr < 0 || nr >= N || nc < 0 || nc >= M) {
                    continue;
                }
                // 2) 이동 가능한 칸(=1)인지
                if (map[nr][nc] == 0) {
                    continue;
                }
                // 3) 아직 방문하지 않았는지
                if (visited[nr][nc]) {
                    continue;
                }

                visited[nr][nc] = true;
                dist[nr][nc] = dist[r][c] + 1; // 최단 거리 갱신
                q.add(new int[]{nr, nc});
            }
        }
    }
}
