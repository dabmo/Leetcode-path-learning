class Solution:
    def isValid(self, s: str) -> bool:
        mapa = {')': '(', '}': '{', ']': '['}
        pila = []
        
        n = len(s)
        texto = ''
        
        for i in range(n):
            if s[i] in mapa:
                if not pila or pila[-1] != mapa[s[i]]:
                    return False
                pila.pop()  
            else:
                pila.append(s[i])
            
        return not pila