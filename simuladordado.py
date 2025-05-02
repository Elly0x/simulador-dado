import random
import tkinter as tk
from tkinter import messagebox

class DadoApp:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Dado")
        master.configure(bg="black")

        self.faces_num = 6
        self.historico = []
        self.contador = 0

        self.label = tk.Label(master, text="Quantas faces terá o dado?", fg="white", bg="black")
        self.label.pack(pady=5)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)
        self.entry.insert(0, "6")

        self.btn_iniciar = tk.Button(master, text="Iniciar", command=self.iniciar, bg="gray")
        self.btn_iniciar.pack(pady=5)

        self.resultado_label = tk.Label(master, text="", font=("Arial", 20), fg="cyan", bg="black")
        self.resultado_label.pack(pady=10)

        self.btn_rolar = tk.Button(master, text="Rolar Dado", command=self.rolar_dado, state=tk.DISABLED, bg="green")
        self.btn_rolar.pack(pady=5)

        self.btn_hist = tk.Button(master, text="Ver Histórico", command=self.mostrar_historico, state=tk.DISABLED, bg="blue")
        self.btn_hist.pack(pady=5)

        self.btn_limpar = tk.Button(master, text="Limpar Histórico", command=self.limpar_historico, state=tk.DISABLED, bg="red")
        self.btn_limpar.pack(pady=5)

        self.btn_salvar = tk.Button(master, text="Salvar Histórico", command=self.salvar_historico, state=tk.DISABLED, bg="orange")
        self.btn_salvar.pack(pady=5)

        self.btn_reiniciar = tk.Button(master, text="Reiniciar", command=self.reiniciar, bg="purple", fg="white")
        self.btn_reiniciar.pack(pady=5)

        self.contador_label = tk.Label(master, text="Total de Rolagens: 0", fg="white", bg="black")
        self.contador_label.pack(pady=5)

    def iniciar(self):
        try:
            faces = int(self.entry.get())
            if faces < 2:
                raise ValueError
            self.faces_num = faces
            self.btn_rolar.config(state=tk.NORMAL)
            self.btn_hist.config(state=tk.NORMAL)
            self.btn_limpar.config(state=tk.NORMAL)
            self.btn_salvar.config(state=tk.NORMAL)
            messagebox.showinfo("Iniciado", f"Dado com {faces} faces pronto para uso!")
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido (mínimo 2).")

    def rolar_dado(self):
        self.btn_rolar.config(state=tk.DISABLED)
        self.resultado_label.config(text="Rolando...")
        self.master.after(100, self.animar_rolagem, 0)

    def animar_rolagem(self, etapa):
        if etapa < 10:
            resultado_temp = random.randint(1, self.faces_num)
            self.resultado_label.config(text=f"... {resultado_temp}")
            self.master.after(100, self.animar_rolagem, etapa + 1)
        else:
            resultado = random.randint(1, self.faces_num)
            self.historico.append(resultado)
            self.contador += 1
            self.resultado_label.config(text=f"Você rolou: {resultado}")
            self.contador_label.config(text=f"Total de Rolagens: {self.contador}")
            self.btn_rolar.config(state=tk.NORMAL)

    def mostrar_historico(self):
        if not self.historico:
            messagebox.showinfo("Histórico", "Nenhum resultado ainda.")
        else:
            msg = ", ".join(str(x) for x in self.historico)
            messagebox.showinfo("Histórico", f"Resultados: {msg}")

    def limpar_historico(self):
        self.historico.clear()
        self.contador = 0
        self.contador_label.config(text="Total de Rolagens: 0")
        messagebox.showinfo("Limpo", "Histórico limpo.")

    def salvar_historico(self):
        if not self.historico:
            messagebox.showinfo("Salvar Histórico", "Nenhum dado para salvar.")
        else:
            try:
                with open("historico_dado.txt", "w") as file:
                    file.write(", ".join(str(x) for x in self.historico))
                messagebox.showinfo("Salvo", "Histórico salvo em 'historico_dado.txt'")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

    def reiniciar(self):
        self.faces_num = 6
        self.historico.clear()
        self.contador = 0
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "6")
        self.resultado_label.config(text="")
        self.contador_label.config(text="Total de Rolagens: 0")
        self.btn_rolar.config(state=tk.DISABLED)
        self.btn_hist.config(state=tk.DISABLED)
        self.btn_limpar.config(state=tk.DISABLED)
        self.btn_salvar.config(state=tk.DISABLED)
        messagebox.showinfo("Reiniciado", "O simulador foi reiniciado.")

# Executar o app
root = tk.Tk()
app = DadoApp(root)
root.mainloop()
