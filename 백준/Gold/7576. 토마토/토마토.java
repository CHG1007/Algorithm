// BOJ 7576 - 토마토
// 문제 요약:
//  - 상자(격자)에 담긴 토마토들의 익음 상태가 주어질 때,
//    모든 토마토가 익을 때까지의 최소 일수를 구하는 문제
//  - 인접(상,하,좌,우)한 익은 토마토는 다음 날에 익지 않은 토마토를 익게 만든다
//  - 이미 모두 익어있으면 0, 끝까지 익지 못하면 -1 출력
//
// 풀이 개요(정석):
//  - "여러 시작점에서 동시에 확산"하는 전형적인 BFS
//  - 초기에 익은 토마토(1)들을 모두 큐에 넣고, level-by-level로 확산
//  - 방문/일수 관리는 day[r][c] 배열로 수행(해당 칸이 익은 '날짜')
//  - 확산 과정에서 익힐 때마다 미익 개수(unripeCount)를 감소 → 최종 검사 용이
//
// 구현 포인트:
//  - 입력: 첫 줄 M(열), N(행) / 이후 N줄에 걸쳐 M개의 정수
//  - 자료구조: ArrayDeque<int[]> (r, c) 좌표 저장
//  - 경계/장애: -1은 비어있는 칸(확산 불가), 0은 미익, 1은 이미 익음
//  - 정답: 마지막에 익은 칸의 day 최댓값(모두 익었을 때만), 일부 남으면 -1

import java.io.*;
import java.util.*;

public class Main {

    static int N, M;                 // N: 행(row), M: 열(col)
    static int[][] box;              // 토마토 상태: -1(없음), 0(안익음), 1(익음)
    static int[][] day;              // 해당 칸이 익은 날짜(day)
    static int[] dr = {-1, 1, 0, 0}; // 상, 하, 좌, 우
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        // ===== 입력 =====
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken()); // 열
        N = Integer.parseInt(st.nextToken()); // 행

        box = new int[N][M];
        day = new int[N][M];

        ArrayDeque<int[]> q = new ArrayDeque<>();
        int unripeCount = 0; // 아직 익지 않은(0) 토마토 개수

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < M; c++) {
                box[r][c] = Integer.parseInt(st.nextToken());
                day[r][c] = 0; // 기본값 0 (익은 날짜가 0일일 수도 있으니 구분은 box로)

                // 초기 익은 토마토는 모두 큐에 삽입 (다중 시작점)
                if (box[r][c] == 1) {
                    q.add(new int[]{r, c});
                } else if (box[r][c] == 0) {
                    unripeCount++;
                }
            }
        }

        // 이미 모두 익어있다면 0일
        if (unripeCount == 0) {
            System.out.println(0);
            return;
        }

        // ===== BFS 확산 =====
        int maxDay = 0; // 최종 답(마지막으로 익은 날)

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0];
            int c = cur[1];

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                // 1) 격자 범위 체크
                if (nr < 0 || nr >= N || nc < 0 || nc >= M) {
                    continue;
                }
                // 2) 비어있는 칸(-1)은 확산 불가
                if (box[nr][nc] == -1) {
                    continue;
                }
                // 3) 이미 익은 칸(1)은 스킵, 익지 않은 칸(0)만 익힌다
                if (box[nr][nc] != 0) {
                    continue;
                }

                // nr,nc 토마토를 익힘
                box[nr][nc] = 1;
                day[nr][nc] = day[r][c] + 1; // 이전 칸의 날 + 1
                if (day[nr][nc] > maxDay) {
                    maxDay = day[nr][nc];
                }
                unripeCount--;

                q.add(new int[]{nr, nc});
            }
        }

        // ===== 결과 판단 =====
        // BFS 후에도 미익 토마토가 남아있으면 -1, 아니면 maxDay
        if (unripeCount > 0) {
            System.out.println(-1);
        } else {
            System.out.println(maxDay);
        }
    }
}
