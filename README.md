# 🚀 3 RPS - Simulator
Erik Y. Goto, 2025

Projeto feito como trabalho de conclusão de curso da Engenharia de Controle e Automação
Construção de uma plataforma paralela com 3 graus de liberdade para simular as acelerações longitudinais e laterais de um carro simulado no Assetto Corsa.

## Principais Tecnologias Usadas
- Python
	- PyAccSharedMemory: https://github.com/rrennoir/PyAccSharedMemory
	- Serial
- Arduino
	- Servo Motores
- Asseto Corsa

## Estrutura do projeto
🖥️ /Script/Python Shared Memory/cinematica_inversa_PS >> Biblioteca com a implementação da cinemática inversa da plataforma 3RPS;

🖥️ /Script/Python Shared Memory/Plataforma de Stewart - Prototipo >> Arquivo que faz a comunicação com o Assetto Corsa por meio da memória compartilhada, faz uso da biblioteca de cinemática inversa e envia os comandos para o Arduino;

🖥️ /Script/script_arduino >> Controle dos servo motores;

🛠️ /Desenhos/idw >> Desenhos da estrtura mecânica no formato de folha de desenho;

🛠️ /Desenhos/ipt >> Desenhos da estrtura mecânica no formato ipt, Inventor 2025;

🛠️ /Desenhos/Step >> Desenhos da estrtura mecânica no formato step.

## Funcionamento
*imagem
