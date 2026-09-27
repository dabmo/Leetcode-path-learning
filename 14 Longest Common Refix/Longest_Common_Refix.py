class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        
        primera = strs[0]
        ultima = strs[-1]
        prefijo = []
        
        for i in range(min(len(primera), len(ultima))):
            if primera[i] == ultima[i]:
                prefijo.append(primera[i])
            else:
                break
                
        return "".join(prefijo)

# --- CÓDIGO PARA PROBAR EN LOCAL ---
solucion = Solution()

# Caso 1: común "fl"
print("Resultado 1:", solucion.longestCommonPrefix(["flower", "flow", "flight"]))

# Caso 2: sin prefijo común ""
print("Resultado 2:", solucion.longestCommonPrefix(["dog", "racecar", "car"]))