// BOJ 2630 - 색종이 만들기
//
// 문제 요약
//  - N x N (N은 2의 거듭제곱) 종이에 0(하양), 1(파랑)이 채워져 있다.
//  - 다음 규칙으로 색종이를 최소 개수의 하얀/파란 종이로 분할한다.
//    1) 현재 종이(정사각형)가 전부 같은 색이면 더 이상 자르지 않는다.
//    2) 색이 섞여 있으면 정확히 4등분(정사각형)하여 같은 규칙을 재귀적으로 적용한다.
//  - 최종적으로 얻는 하얀 종이 수와 파란 종이 수를 출력한다.
//
// 풀이 개요 (분할정복)
//  - 구간(정사각형)이 단색인지 확인한다.
//    - 단색이면 해당 색 카운트를 1 증가.
//    - 단색이 아니면 4등분하여 각각 재귀 처리.
//  - 시간복잡도: 각 칸은 어떤 호출에서 최대 한 번씩만 검사 → O(N^2).
//
// 구현 포인트
//  - 입력: BufferedReader + StringTokenizer
//  - 상태: paper[r][c] (0/1), 전역 카운터 white, blue
//  - 재귀: cut(sr, sc, size)

import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int[][] paper;
    static int white = 0; // 하얀 색종이 개수
    static int blue = 0;  // 파란 색종이 개수

    public static void main(String[] args) throws Exception {
        // ===== 입력 =====
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine().trim());

        paper = new int[N][N];
        for (int r = 0; r < N; r++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                paper[r][c] = Integer.parseInt(st.nextToken()); // 0 또는 1
            }
        }

        // ===== 분할정복 시작 =====
        cut(0, 0, N);

        // ===== 결과 출력 =====
        // 출력 형식: 하얀 색종이 개수, 파란 색종이 개수
        StringBuilder sb = new StringBuilder();
        sb.append(white).append('\n').append(blue);
        System.out.println(sb);
    }

    /**
     * 정사각형 구간 [sr, sc]에서 시작하여 한 변 길이가 size인 영역을 처리.
     * 단색이면 해당 색 카운트를 증가, 아니면 4등분하여 재귀 호출.
     */
    static void cut(int sr, int sc, int size) {
        // 현재 구간이 단색인지 확인
        if (isUniform(sr, sc, size)) {
            if (paper[sr][sc] == 0) {
                white++;
            } else {
                blue++;
            }
            return;
        }

        // 섞여 있으면 4등분해서 재귀 호출
        int half = size / 2;

        // 1사분면 (좌상)
        cut(sr, sc, half);
        // 2사분면 (우상)
        cut(sr, sc + half, half);
        // 3사분면 (좌하)
        cut(sr + half, sc, half);
        // 4사분면 (우하)
        cut(sr + half, sc + half, half);
    }

    /**
     * [sr, sc] 시작, 한 변 길이 size인 정사각형이 모두 같은 색인지 검사.
     * 모두 같으면 true, 아니면 false.
     */
    static boolean isUniform(int sr, int sc, int size) {
        int color = paper[sr][sc];
        for (int r = sr; r < sr + size; r++) {
            for (int c = sc; c < sc + size; c++) {
                if (paper[r][c] != color) {
                    return false;
                }
            }
        }
        return true;
    }
}
