// BOJ 14503 - 로봇 청소기
//
// 문제 요약
//  - N x M 격자에서 로봇이 주어진 규칙에 따라 방을 청소한다.
//  - 0: 빈 칸(청소 가능), 1: 벽(이동 불가)
//  - 방향: 0 북, 1 동, 2 남, 3 서
//  - 규칙
//    1) 현재 칸이 아직 청소되지 않았다면 청소한다.
//    2) 현재 방향을 기준으로 왼쪽 방향부터 차례로 탐색하여,
//       아직 청소하지 않은 빈 칸이 있으면 그 방향으로 회전 후 한 칸 전진한다(그리고 1부터 반복).
//       왼쪽 방향에 청소할 칸이 없으면 그 방향으로 회전만 하고 다시 탐색(총 4회 시도).
//    3) 네 방향 모두 청소할 수 없다면, 바라보는 방향을 유지한 채 한 칸 후진한다.
//       후진이 벽으로 막혀 있으면 작동을 멈춘다.
//
// 풀이 개요
//  - 완전한 시뮬레이션 문제. 규칙을 그대로 구현한다.
//  - 청소 여부는 별도 visited 또는 map에 2로 마킹하여 관리할 수 있다.
//  - 방향 전환: 왼쪽 회전은 (d+3)%4, 후진 방향은 (d+2)%4 사용.
//  - 시간복잡도: 각 칸을 최대 한 번 청소하므로 O(N*M).
//
// 구현 포인트
//  - 입력 최적화: BufferedReader + StringTokenizer
//  - 자료형: 좌표는 int로 충분
//  - 상태: (r, c, d), map[r][c] == 0(미청소), 1(벽), 2(청소 완료)

import java.io.*;
import java.util.*;

public class Main {

    // 방향: 0 북, 1 동, 2 남, 3 서
    // dr/dc는 해당 방향으로 한 칸 이동 시의 증분
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        // ===== 입력 =====
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 행
        int M = Integer.parseInt(st.nextToken()); // 열

        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken()); // 시작 행
        int c = Integer.parseInt(st.nextToken()); // 시작 열
        int d = Integer.parseInt(st.nextToken()); // 시작 방향(0:북,1:동,2:남,3:서)

        int[][] map = new int[N][M]; // 0:빈칸, 1:벽, 2:청소완료
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // ===== 시뮬레이션 =====
        int cleaned = 0;

        while (true) {
            // 1) 현재 칸 청소
            if (map[r][c] == 0) {
                map[r][c] = 2; // 청소 완료 마킹
                cleaned++;
            }

            // 2) 왼쪽부터 4방향 탐색
            boolean moved = false;
            for (int i = 0; i < 4; i++) {
                // 왼쪽 회전
                d = (d + 3) % 4;
                int nr = r + dr[d];
                int nc = c + dc[d];

                // 범위 내부 && 아직 청소하지 않은 빈 칸(=0)인지 확인
                if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
                    if (map[nr][nc] == 0) {
                        // 전진
                        r = nr;
                        c = nc;
                        moved = true;
                        break; // 전진했으면 다음 루프에서 1단계부터 반복
                    }
                }
            }

            // 왼쪽 4방향 모두 이동 불가
            if (!moved) {
                // 3) 후진 시도 (방향 유지)
                int backDir = (d + 2) % 4;
                int brR = r + dr[backDir];
                int brC = c + dc[backDir];

                // 후진이 벽이면 종료
                if (brR < 0 || brR >= N || brC < 0 || brC >= M) {
                    break;
                }
                if (map[brR][brC] == 1) {
                    break;
                }

                // 후진 가능하면 한 칸 후진 (방향 d는 그대로 유지)
                r = brR;
                c = brC;
            }
        }

        // ===== 결과 출력 =====
        System.out.println(cleaned);
    }
}
