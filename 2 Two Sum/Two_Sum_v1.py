class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #Arreglo para identificar la ubicación de los números que suman el target
        for i in range(len(nums)):
            #Arreglo para tomar el segundo número y verificar si la suma es igual al target
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# --- CÓDIGO PARA PROBAR EN LOCAL ---

solucion = Solution()
nums_prueba = [2, 7, 11, 15]
target_prueba = 9
resultado = solucion.twoSum(nums_prueba, target_prueba)
print(f"El resultado es: {resultado}")