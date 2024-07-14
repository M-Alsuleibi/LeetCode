class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Tc = O(n), Sc = O(1)

        return address.replace(".","[.]")
