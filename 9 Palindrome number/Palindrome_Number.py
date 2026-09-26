class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        if num == num [:: -1]:
            return True
        else:
            return False 

# --- CÓDIGO PARA PROBAR EN LOCAL ---

solucion = Solution()
prueba_x = 1331
resultado = solucion.isPalindrome(prueba_x)
print(f"El resultado es: {resultado}")

solucion = Solution()
prueba_x = -1331
resultado = solucion.isPalindrome(prueba_x)
print(f"El resultado es: {resultado}")