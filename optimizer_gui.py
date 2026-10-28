import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
import optimizer_core

class OptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows Light Optimizer - Ultimate Edition")
        self.root.geometry("680x550")
        self.root.config(bg="#0f172a") # Fondo oscuro moderno estilo terminal pro
        self.root.resizable(False, False)

        # Verificar permisos de administrador al iniciar
        if not optimizer_core.is_admin():
            messagebox.showwarning(
                "Atención", 
                "Ejecuta esta aplicación como Administrador para que los comandos avanzados surtan efecto real."
            )

        # --- TÍTULO ---
        titulo = tk.Label(root, text="⚡ WINDOWS LIGHT OPTIMIZER ⚡", font=("Segoe UI", 16, "bold"), bg="#0f172a", fg="#38bdf8")
        titulo.pack(pady=15)

        # --- CONTENEDOR DE BOTONES ESTÁNDAR ---
        frame_botones = tk.Frame(root, bg="#0f172a")
        frame_botones.pack(pady=5)

        btn_temp = tk.Button(frame_botones, text="🧹 Limpiar Temporales", bg="#334155", fg="#ffffff", font=("Segoe UI", 10, "bold"), width=25, relief="flat", command=self.ejecutar_limpieza)
        btn_temp.grid(row=0, column=0, padx=8, pady=8)

        btn_energia = tk.Button(frame_botones, text="🚀 Máximo Rendimiento", bg="#334155", fg="#ffffff", font=("Segoe UI", 10, "bold"), width=25, relief="flat", command=self.ejecutar_energia)
        btn_energia.grid(row=0, column=1, padx=8, pady=8)

        btn_telemetria = tk.Button(frame_botones, text="🛡️ Desactivar Telemetría", bg="#334155", fg="#ffffff", font=("Segoe UI", 10, "bold"), width=54, relief="flat", command=self.ejecutar_telemetria)
        btn_telemetria.grid(row=1, column=0, columnspan=2, pady=5)

        # --- BOTÓN DEL COMANDO MAESTRO (DESTACADO Y ÉPICO) ---
        self.btn_maestro = tk.Button(root, text="🔥 EJECUTAR COMANDO MAESTRO EXTREMO 🔥", bg="#dc2626", fg="#ffffff", font=("Segoe UI", 11, "bold"), width=58, relief="flat", command=self.ejecutar_maestro)
        self.btn_maestro.pack(pady=12)

        # --- CONSOLA DE REGISTRO (LOG) ---
        lbl_log = tk.Label(root, text="Consola de Estado en Directo:", font=("Segoe UI", 9, "bold"), bg="#0f172a", fg="#94a3b8")
        lbl_log.pack(anchor="w", padx=25)

        self.consola = scrolledtext.ScrolledText(root, width=76, height=12, state="disabled", bg="#020617", fg="#22c55e", font=("Consolas", 9), insertbackground="white")
        self.consola.pack(padx=20, pady=5)

    def log(self, mensaje):
        """Añade mensajes a la consola gráfica de forma segura."""
        self.consola.config(state="normal")
        self.consola.insert(tk.END, mensaje + "\n")
        self.consola.see(tk.END)
        self.consola.config(state="disabled")

    def ejecutar_en_hilo(self, funcion, *args):
        """Ejecuta tareas pesadas en segundo plano para que la ventana no se congele."""
        def tarea():
            exito, mensaje = funcion(*args)
            self.log(f"[✔] {mensaje}" if exito else f"[✖] {mensaje}")
        threading.Thread(target=tarea).start()

    def ejecutar_limpieza(self):
        self.log("[*] Limpiando archivos temporales y papelera...")
        self.ejecutar_en_hilo(optimizer_core.limpiar_temporales)

    def ejecutar_energia(self):
        self.log("[*] Configurando plan de energía de Máximo Rendimiento...")
        self.ejecutar_en_hilo(optimizer_core.optimizar_energia)

    def ejecutar_telemetria(self):
        self.log("[*] Desactivando servicios de telemetría y rastreo...")
        self.ejecutar_en_hilo(optimizer_core.desactivar_telemetria)

    def ejecutar_maestro(self):
        self.log("[🔥] INICIANDO SECUENCIA MAESTRA: Purgando red, DNS, Prefetch y optimizando servicios...")
        self.ejecutar_en_hilo(optimizer_core.comando_maestro_extremo)

if __name__ == "__main__":
    root = tk.Tk()
    app = OptimizerApp(root)
    root.mainloop()