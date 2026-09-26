class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Creamos un mapa de valores
        valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        n = len(s)

        for i in range(n):
            # Si el valor actual es menor que el siguiente, restamos
            if i < n - 1 and valores[s[i]] < valores[s[i + 1]]:
                total -= valores[s[i]]
            else:
                # De lo contrario, sumamos
                total += valores[s[i]]

        return total
    
# --- CÓDIGO PARA PROBAR EN LOCAL ---

solucion = Solution()
prueba_s = "MCMXCIV"
resultado = solucion.romanToInt(prueba_s)
print(f"El resultado es: {resultado}")

