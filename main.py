import tkinter as tk
from tkinter import ttk

class CalculadoraAliquotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Alíquotas")
        self.root.geometry("500x700")
        self.root.configure(bg="#A9A9A9")  # Cinza padrão
        self.root.resizable(False, False)
        
        style = ttk.Style()
        style.configure("TLabel", foreground="black", background="#A9A9A9", font=("Arial", 11))
        style.configure("TButton", font=("Arial", 12, "bold"), padding=10, background="#4CAF50", foreground="black")
        style.configure("TEntry", padding=5, fieldbackground="white", foreground="black")
        
        ttk.Label(root, text="Valor Bruto:", font=("Arial", 12, "bold"), background="#A9A9A9").pack(pady=5)
        self.valor_bruto = tk.DoubleVar()
        ttk.Entry(root, textvariable=self.valor_bruto, font=("Arial", 12), width=25).pack(pady=5)
        
        ttk.Label(root, text="Valor Recebido:", font=("Arial", 12, "bold"), background="#A9A9A9").pack(pady=5)
        self.valor_recebido = tk.DoubleVar()
        ttk.Entry(root, textvariable=self.valor_recebido, font=("Arial", 12), width=25).pack(pady=5)
        
        self.aliquotas = {
            "IRPJ": tk.DoubleVar(value=4.8),
            "PIS": tk.DoubleVar(value=0.65),
            "COFINS": tk.DoubleVar(value=3.0),
            "CSLL": tk.DoubleVar(value=1.0),
            "INSS": tk.DoubleVar(value=11.0),
            "ISS": tk.DoubleVar(value=5.0),
            "PCC": tk.DoubleVar(value=4.65),
        }
        
        self.resultados = {}
        frame_impostos = ttk.Frame(root)
        frame_impostos.pack(pady=10, padx=10, fill='both', expand=True)
        
        for imposto, var in self.aliquotas.items():
            frame = ttk.Frame(frame_impostos)
            frame.pack(fill='x', padx=10, pady=3)
            ttk.Label(frame, text=f"{imposto} (%):", background="#A9A9A9").pack(side='left')
            ttk.Entry(frame, textvariable=var, width=5, font=("Arial", 10)).pack(side='left', padx=5)
            self.resultados[imposto] = ttk.Label(frame, text="R$ 0.00", font=("Arial", 10, "bold"), background="#A9A9A9")
            self.resultados[imposto].pack(side='right')
        
        ttk.Button(root, text="Calcular", command=self.calcular).pack(pady=20)
        
        self.resultado_liquido = ttk.Label(root, text="Valor Líquido: R$ 0.00", font=("Arial", 14, "bold"), background="#A9A9A9")
        self.resultado_liquido.pack(pady=10)
        
        self.resultado_diferenca = ttk.Label(root, text="", font=("Arial", 12, "bold"), background="#A9A9A9", foreground="red")
        self.resultado_diferenca.pack(pady=10)
        
    def calcular(self):
        bruto = self.valor_bruto.get()
        recebido = self.valor_recebido.get()
        total_deducoes = 0
        
        for imposto, var in self.aliquotas.items():
            valor_imposto = bruto * (var.get() / 100)
            self.resultados[imposto].config(text=f"R$ {valor_imposto:.2f}")
            if imposto not in ["PCC"]:  # PCC não deduz do bruto
                total_deducoes += valor_imposto
        
        liquido = bruto - total_deducoes
        self.resultado_liquido.config(text=f"Valor Líquido: R$ {liquido:.2f}")
        
        if recebido > liquido:
            diferenca = recebido - liquido
            self.resultado_diferenca.config(text=f"Diferença recebida: R$ {diferenca:.2f}")
        else:
            self.resultado_diferenca.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraAliquotas(root)
    root.mainloop()
