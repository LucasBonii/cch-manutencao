"""Testes unitários - Manutenção Preventiva."""

from BFS_manutencao import Graph


def test_grafo_vazio_start_0():
    """BFS em grafo totalmente vazio ---> Vértice inicial é sempre visitado {0}"""
    g = Graph()
    result = g.bfs(0)
    assert 0 in result  


def test_vertice_isolado():
    """Vértice sem vizinhos em grafo com outras arestas ---> BFS retorna só ele mesmo {2}"""
    g = Graph()
    g.add_edge(0, 1)
    result = g.bfs(2)
    assert result == {2} 


def test_self_loop():
    """Aresta para si mesmo ---> Não entra em loop infinito, retorna {0}"""
    g = Graph()
    g.add_edge(0, 0)
    result = g.bfs(0)
    assert result == {0}

