class Solution:
    
    def encode(self, strs: List[str]) -> str:
        # Encode each string with its length followed by a delimiter (e.g., ':')
        return ''.join(f'{len(s)}:{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        # Decode by splitting based on the lengths and the delimiter
        i, result = 0, []
        while i < len(s):
            # Find the delimiter to extract the length
            j = s.find(':', i)
            length = int(s[i:j])  # Extract the length of the next string
            result.append(s[j+1:j+1+length])  # Extract the string based on length
            i = j + 1 + length  # Move to the next encoded part
        return result