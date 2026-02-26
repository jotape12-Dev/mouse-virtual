# 🖐️ AI Virtual Mouse (Computer Vision)

> Controle o cursor do mouse e realize cliques usando apenas gestos manuais e uma webcam. Projeto de Visão Computacional rodando em Python.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![OpenCV](https://img.shields.io/badge/CV-OpenCV-green)
![MediaPipe](https://img.shields.io/badge/AI-MediaPipe-orange)


## 📖 Sobre o Projeto

Este projeto elimina a necessidade de um mouse físico, utilizando a câmera do computador para rastrear a mão do usuário em tempo real. Através de modelos de **Deep Learning (MediaPipe)**, o sistema mapeia 21 pontos da mão e traduz gestos específicos em comandos do sistema operacional.

### ✨ Funcionalidades
* **👆 Navegação:** Mova o cursor apontando com o dedo indicador.
* **🤏 Clique:** Realize cliques juntando o dedo indicador e o médio (gesto de pinça).
* **Smoothness:** Algoritmo de suavização para evitar que o mouse fique "tremendo".
* **Action Zone:** Área delimitada na câmera para melhorar a precisão do movimento.

---

## 🛠️ Tecnologias

* **Python 3.11**: Linguagem base (Otimizada para Apple Silicon).
* **OpenCV (cv2)**: Captura de vídeo e processamento de imagem.
* **MediaPipe**: Framework do Google para detecção de mãos (Hand Tracking) com alta performance.
* **PyAutoGUI**: Automação de controle de mouse e teclado.
* **NumPy**: Cálculos matemáticos para converter coordenadas da câmera para a tela.

---

## 🚀 Como Rodar

### Pré-requisitos
* Webcam funcional.
* Python 3.11 instalado.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/jotape12-Dev/mouse-virtual.git](https://github.com/jotape12-Dev/mouse-virtual.git)
    cd mouse-virtual
    ```

2.  **Crie o ambiente virtual (Importante usar Python 3.11):**
    ```bash
    python3.11 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências (Versões compatíveis com Mac M1/M2):**
    ```bash
    pip install mediapipe==0.10.9 protobuf==3.20.3 opencv-python pyautogui
    ```

4.  **Execute:**
    ```bash
    python main.py
    ```

*(Nota: No macOS, conceda permissão de Acessibilidade ao terminal/IDE para controlar o mouse)*.

## 📄 Licença
Este projeto está sob a licença MIT.
