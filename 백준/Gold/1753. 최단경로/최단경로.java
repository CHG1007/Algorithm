// BOJ 1753 - 최단경로
//
// 문제 요약
//  - 방향 그래프에서 시작 정점 K로부터 각 정점까지의 최단 거리를 구한다.
//  - 간선 가중치는 양수.
//  - 도달 불가 정점은 "INF" 출력.
//
// 풀이 개요 (Dijkstra + PriorityQueue)
//  - 가중치가 모두 양수이므로 다익스트라 알고리즘을 사용한다.
//  - 인접 리스트로 그래프를 표현하고, PQ는 (현재까지의 거리, 정점)으로 구성한다.
//  - PQ에서 뽑힌 거리(curDist)가 dist[now]보다 크면 "오래된 항목"이므로 건너뛴다.
//  - dist 배열은 int로 충분하며, 초기값은 큰 수(INF)로 채운다.
//
// 구현 포인트
//  - 입력: BufferedReader + StringTokenizer (V ≤ 20,000, E ≤ 300,000 → 대량 I/O)
//  - 그래프: ArrayList<Edge>[] (1-indexed)
//  - PQ: 최단 거리 기준 오름차순 정렬
//  - 시간 복잡도: O(E log V)

import java.io.*;
import java.util.*;

public class Main {

    static class Edge {
        int to;
        int w;
        Edge(int to, int w) {
            this.to = to;
            this.w = w;
        }
    }

    static class Node implements Comparable<Node> {
        int v;      // 정점 번호
        int dist;   // 시작점으로부터의 현재까지 최단 후보 거리
        Node(int v, int dist) {
            this.v = v;
            this.dist = dist;
        }
        @Override
        public int compareTo(Node other) {
            if (this.dist < other.dist) return -1;
            if (this.dist > other.dist) return 1;
            return 0;
        }
    }

    static final int INF = 1_000_000_000; // 충분히 큰 값(10^9)
    static int V, E, K;
    static ArrayList<Edge>[] graph;
    static int[] dist;

    public static void main(String[] args) throws Exception {
        // ===== 입력 =====
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        K = Integer.parseInt(br.readLine().trim()); // 시작 정점

        graph = new ArrayList[V + 1];
        for (int i = 1; i <= V; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()); // from
            int v = Integer.parseInt(st.nextToken()); // to
            int w = Integer.parseInt(st.nextToken()); // weight
            graph[u].add(new Edge(v, w));
        }

        // ===== 다익스트라 =====
        dist = new int[V + 1];
        Arrays.fill(dist, INF);
        dijkstra(K);

        // ===== 출력 =====
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= V; i++) {
            if (dist[i] == INF) {
                sb.append("INF").append('\n');
            } else {
                sb.append(dist[i]).append('\n');
            }
        }
        System.out.print(sb);
    }

    /**
     * 시작 정점 start로부터 모든 정점까지의 최단 거리를 dist[]에 채운다.
     */
    static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        dist[start] = 0;
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            int now = cur.v;
            int nowDist = cur.dist;

            // PQ에서 꺼낸 값이 최신 최단거리보다 크면 스킵(오래된 항목)
            if (nowDist > dist[now]) {
                continue;
            }

            // 인접 정점 완화(relaxation)
            for (Edge e : graph[now]) {
                int nxt = e.to;
                int cand = nowDist + e.w;
                if (cand < dist[nxt]) {
                    dist[nxt] = cand;
                    pq.add(new Node(nxt, cand));
                }
            }
        }
    }
}
