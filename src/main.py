from src.analyzer import analyze_physics_problem
from src.retriever import retrieve_knowledge
from src.assembler import assemble_prompt
from src.solver import execute_solver
import os

# Input Soal
soal = "Sebuah balok bermassa 4 kg ditarik ke atas bidang miring licin (sudut 30 derajat) dengan gaya 50 N."
api_key = os.getenv("GEMINI_API_KEY") 

# Alur DFS
m2_data = analyze_physics_problem(soal)
konteks = retrieve_knowledge(m2_data)
prompt = assemble_prompt(soal, konteks)
solusi = execute_solver(prompt, api_key)

print(solusi)
