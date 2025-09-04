#Fabio Leandro Lapuinka 04/09/2025 STL File
#pip install numpy-stl numpy

import numpy as np
from stl import mesh
import math

def create_f22_stl(filename="f22_raptor.stl"):
    """
    Cria um modelo STL simplificado de um F-22 Raptor
    """
    
    # Definir os vértices do modelo
    vertices = np.array([
        # Fuselagem principal
        [-20, 0, 0],   # 0: Nariz traseiro
        [20, 0, 0],    # 1: Cauda
        [-15, -2, 0],  # 2: Baixo nariz
        [-15, 2, 0],   # 3: Alto nariz
        [15, -2, 0],   # 4: Baixo cauda
        [15, 2, 0],    # 5: Alto cauda
        
        # Asas
        [-5, -15, 0],  # 6: Ponta asa esquerda
        [-5, 15, 0],   # 7: Ponta asa direita
        [5, -15, 0],   # 8: Ponta asa traseira esq
        [5, 15, 0],    # 9: Ponta asa traseira dir
        
        # Estabilizadores verticais
        [10, -8, 8],   # 10: Topo estab. esquerdo
        [10, 8, 8],    # 11: Topo estab. direito
        [15, -5, 0],   # 12: Base estab. esquerdo
        [15, 5, 0],    # 13: Base estab. direito
        
        # Canards
        [-10, -6, 2],  # 14: Ponta canard esq
        [-10, 6, 2],   # 15: Ponta canard dir
        [-15, -3, 0],  # 16: Base canard esq
        [-15, 3, 0],   # 17: Base canard dir
        
        # Entrada de ar
        [-8, -4, -2],  # 18: Entrada ar esq
        [-8, 4, -2],   # 19: Entrada ar dir
    ])
    
    # Definir as faces (triângulos)
    faces = []
    
    # Fuselagem superior
    faces.append([0, 3, 1])
    faces.append([1, 3, 5])
    
    # Fuselagem inferior
    faces.append([0, 1, 2])
    faces.append([1, 4, 2])
    
    # Laterais fuselagem
    faces.append([0, 2, 3])
    faces.append([1, 5, 4])
    
    # Asa esquerda
    faces.append([2, 6, 8])
    faces.append([2, 8, 4])
    faces.append([2, 4, 8])
    
    # Asa direita
    faces.append([3, 9, 7])
    faces.append([3, 5, 9])
    faces.append([3, 7, 5])
    
    # Estabilizador vertical esquerdo
    faces.append([4, 10, 12])
    faces.append([4, 12, 10])
    
    # Estabilizador vertical direito
    faces.append([5, 13, 11])
    faces.append([5, 11, 13])
    
    # Canard esquerdo
    faces.append([16, 14, 2])
    faces.append([2, 14, 16])
    
    # Canard direito
    faces.append([17, 3, 15])
    faces.append([3, 17, 15])
    
    # Entradas de ar
    faces.append([2, 18, 16])
    faces.append([3, 17, 19])
    
    # Criar o mesh
    faces = np.array(faces)
    f22_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    
    for i, face in enumerate(faces):
        for j in range(3):
            f22_mesh.vectors[i][j] = vertices[face[j]]
    
    # Escrever para arquivo STL
    f22_mesh.save(filename)
    print(f"Modelo F-22 salvo como {filename}")
    
    return f22_mesh

def create_detailed_f22_stl(filename="f22_detailed.stl"):
    """
    Versão mais detalhada do F-22
    """
    vertices = []
    faces = []
    
    # Parâmetros do modelo
    length = 40
    wingspan = 30
    height = 8
    
    # Gerar pontos para fuselagem
    fuselage_points = []
    for i in range(10):
        x = -length/2 + i * length/9
        radius = 3 * math.exp(-0.5 * ((x + 5)/10)**2)
        fuselage_points.append([x, 0, 0])
        fuselage_points.append([x, radius, 0])
        fuselage_points.append([x, -radius, 0])
        fuselage_points.append([x, 0, radius])
        fuselage_points.append([x, 0, -radius])
    
    vertices.extend(fuselage_points)
    
    # Gerar asas
    wing_points = []
    wing_start = -length/4
    for i in range(5):
        x = wing_start + i * length/8
        y_span = wingspan/2 * (1 - abs(x)/length)
        wing_points.append([x, y_span, -1])
        wing_points.append([x, -y_span, -1])
    
    vertices.extend(wing_points)
    
    # Gerar estabilizadores
    tail_points = []
    for i in range(3):
        x = length/2 - i * 3
        tail_points.append([x, 5, height])
        tail_points.append([x, -5, height])
    
    vertices.extend(tail_points)
    
    vertices = np.array(vertices)
    
    # Criar mesh básico (simplificado para exemplo)
    # Na prática, você precisaria definir faces mais complexas
    
    simple_mesh = mesh.Mesh(np.zeros(12, dtype=mesh.Mesh.dtype))
    
    # Fuselagem básica
    simple_mesh.vectors[0] = [[-20, 0, 0], [20, 0, 0], [-20, 3, 0]]
    simple_mesh.vectors[1] = [[20, 0, 0], [20, 3, 0], [-20, 3, 0]]
    
    # Asas
    simple_mesh.vectors[2] = [[-5, -15, 0], [-5, 15, 0], [5, -15, 0]]
    simple_mesh.vectors[3] = [[-5, 15, 0], [5, 15, 0], [5, -15, 0]]
    
    # Cauda vertical
    simple_mesh.vectors[4] = [[15, 0, 0], [15, 0, 8], [10, 5, 8]]
    simple_mesh.vectors[5] = [[15, 0, 0], [10, -5, 8], [15, 0, 8]]
    
    simple_mesh.save(filename)
    print(f"Modelo detalhado F-22 salvo como {filename}")
    
    return simple_mesh

if __name__ == "__main__":
    # Instalar a biblioteca necessária: pip install numpy-stl
    
    try:
        # Criar versão simples
        create_f22_stl("f22_simple.stl")
        
        # Criar versão mais detalhada
        create_detailed_f22_stl("f22_detailed.stl")
        
        print("Modelos F-22 criados com sucesso!")
        print("Use um visualizador STL para ver os resultados")
        
    except ImportError:
        print("Erro: Instale a biblioteca numpy-stl primeiro:")
        print("pip install numpy-stl")
    except Exception as e:
        print(f"Erro ao criar modelo: {e}")
