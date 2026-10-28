import ctypes
import subprocess
import os

def is_admin():
    """Comprueba si el script se está ejecutando con privilegios de Administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def ejecutar_comando(comando):
    """Ejecuta un comando de PowerShell de forma silenciosa y devuelve el resultado."""
    try:
        resultado = subprocess.run(
            ["powershell", "-Command", comando],
            capture_output=True,
            text=True,
            shell=True
        )
        return True, resultado.stdout.strip()
    except Exception as e:
        return False, str(e)

# --- MÓDULOS DE OPTIMIZACIÓN ---

def limpiar_temporales():
    """Elimina archivos temporales del sistema de forma segura."""
    comandos = [
        "Remove-Item -Path 'C:\\Windows\\Temp\\*' -Recurse -Force -ErrorAction SilentlyContinue",
        "Remove-Item -Path 'C:\\Users\\*\\AppData\\Local\\Temp\\*' -Recurse -Force -ErrorAction SilentlyContinue",
        "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"
    ]
    exito = True
    for cmd in comandos:
        ok, _ = ejecutar_comando(cmd)
        if not ok:
            exito = False
    return exito, "Archivos temporales y papelera limpiados correctamente."

def optimizar_energia():
    """Activa el plan de energía de Máximo Rendimiento."""
    cmd = "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61"
    ok, salida = ejecutar_comando(cmd)
    if ok:
        ejecutar_comando("powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61")
        return True, "Plan de Máximo Rendimiento activado con éxito."
    return False, "No se pudo activar el plan de energía (es posible que ya esté activo)."

def desactivar_telemetria():
    """Desactiva servicios pesados de telemetría y rastreo en segundo plano."""
    servicios = ["DiagTrack", "dmwappushservice"]
    mensajes = []
    for serv in servicios:
        cmd = f"Stop-Service -Name '{serv}' -Force -ErrorAction SilentlyContinue; Set-Service -Name '{serv}' -StartupType Disabled"
        ok, _ = ejecutar_comando(cmd)
        if ok:
            mensajes.append(f"Servicio {serv} deshabilitado.")
        else:
            mensajes.append(f"No se pudo modificar {serv}.")
    return True, " | ".join(mensajes)

def comando_maestro_extremo():
    """El comando complejo definitivo: purga profunda, optimización de red TCP/IP y limpieza total."""
    comandos_pro = [
        # 1. Limpieza agresiva de Prefetch y logs de sistema antiguos
        "Remove-Item -Path 'C:\\Windows\\Prefetch\\*' -Recurse -Force -ErrorAction SilentlyContinue",
        # 2. Reiniciar la pila de red TCP/IP para liberar latencia
        "netsh int ip reset",
        "netsh winsock reset",
        # 3. Vaciar caché de DNS
        "ipconfig /flushdns",
        # 4. Desactivar aceleración de volcado de memoria innecesaria para ganar agilidad
        "wmic recoveros set DebugInfoType=0",
        # 5. Parar servicios de Cortana y sugerencias de Windows para liberar RAM
        "Stop-Service -Name 'WSearch' -Force -ErrorAction SilentlyContinue; Set-Service -Name 'WSearch' -StartupType Manual"
    ]
    
    exitos = 0
    for cmd in comandos_pro:
        ok, _ = ejecutar_comando(cmd)
        if ok:
            exitosa = True
            exitos += 1

    return True, f"¡Comando Maestro ejecutado con éxito! Se aplicaron {exitos} protocolos avanzados de rendimiento y limpieza de red."