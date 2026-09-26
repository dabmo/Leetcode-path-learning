class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vistos = {}  # Este es el diccionario {numero: posicion}
        
        # enumerate te da la posición (i) y el valor (num) al mismo tiempo
        for i, num in enumerate(nums):
            diferencia = target - num  # Calculamos qué número nos falta
            
            # Si el número que nos falta ya está en nuestro diccionario...
            if diferencia in vistos:
                return [vistos[diferencia], i]  # Devolvemos ambas posiciones
            
            # Si no está, guardamos el número actual y su posición en el diccionario
            vistos[num] = i

# --- CÓDIGO PARA PROBAR EN LOCAL ---

solucion = Solution()
nums_prueba = [2, 7, 11, 15]
target_prueba = 9
resultado = solucion.twoSum(nums_prueba, target_prueba)
print(f"El resultado es: {resultado}")