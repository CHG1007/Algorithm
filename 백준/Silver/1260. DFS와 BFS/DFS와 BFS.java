// BOJ 1260 - DFS와 BFS
//
// 문제 요약
//  - 정점 N, 간선 M, 시작 정점 V 가 주어짐 (1-indexed).
//  - 간선은 무방향.
//  - DFS 방문 순서 출력, 그 다음 줄에 BFS 방문 순서 출력.
//  - 인접 정점이 여러 개면 "번호가 작은 정점"부터 방문.
//
// 템플릿 포인트
//  - 그래프: ArrayList<Integer>[] (1-indexed)
//  - 정렬: 각 정점의 인접 리스트를 오름차순 정렬
//  - DFS: 재귀 (방문 즉시 출력 버퍼에 추가)
//  - BFS: ArrayDeque<int> 큐 사용
//  - 출력: StringBuilder로 모아서 한 번에 출력 (마지막 공백은 trim)
//
// 시간 복잡도
//  - 정렬 O(Σ deg log deg) ≈ O(M log M) 수준
//  - 탐색 O(N + M)

import java.io.*;
import java.util.*;

public class Main {

    static int N, M, V;
    static ArrayList<Integer>[] graph; // 인접 리스트 (1-indexed)
    static boolean[] visited;
    static StringBuilder outDFS = new StringBuilder();
    static StringBuilder outBFS = new StringBuilder();

    public static void main(String[] args) throws Exception {
        // ===== 입력 =====
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        buildGraph(br);

        // 인접 정점 "번호 작은 것부터" 방문을 위해 정렬
        for (int i = 1; i <= N; i++) {
            Collections.sort(graph[i]);
        }

        // ===== DFS =====
        visited = new boolean[N + 1];
        dfs(V);
        // 줄바꿈
        outDFS.append('\n');

        // ===== BFS =====
        visited = new boolean[N + 1];
        bfs(V);

        // ===== 출력 =====
        // 마지막 공백을 제거(trim)하여 출력 형식 맞춤
        System.out.print(outDFS.toString().trim());
        System.out.print('\n');
        System.out.print(outBFS.toString().trim());
    }

    // 그래프 생성 (무방향)
    static void buildGraph(BufferedReader br) throws Exception {
        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }
    }

    // 깊이 우선 탐색 (재귀)
    static void dfs(int v) {
        visited[v] = true;
        outDFS.append(v).append(' ');

        // 번호가 작은 정점부터 방문 (이미 정렬되어 있음)
        for (int next : graph[v]) {
            if (!visited[next]) {
                dfs(next);
            }
        }
    }

    // 너비 우선 탐색 (큐)
    static void bfs(int start) {
        ArrayDeque<Integer> q = new ArrayDeque<>();
        visited[start] = true;
        q.add(start);

        while (!q.isEmpty()) {
            int cur = q.poll();
            outBFS.append(cur).append(' ');

            for (int next : graph[cur]) {
                if (!visited[next]) {
                    visited[next] = true; // 큐에 넣을 때 방문 표시 (중복 방지)
                    q.add(next);
                }
            }
        }
    }
}
