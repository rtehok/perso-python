from collections import defaultdict
from typing import List

Trie = lambda: defaultdict(Trie)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            tmp = trie  # go back to first node
            for c in product:
                tmp = tmp[c]
                try:
                    tmp['products'].append(product)
                    tmp['products'].sort()
                    tmp['products'] = tmp['products'][:3]
                except:
                    tmp['products'] = [product]

        res = []
        # print(trie)

        for c in searchWord:
            trie = trie[c]
            curr_products = trie.get('products', [])
            res.append(curr_products)

        return res


if __name__ == "__main__":
    assert Solution().suggestedProducts(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
                                        searchWord="mouse") == [
               ["mobile", "moneypot", "monitor"],
               ["mobile", "moneypot", "monitor"],
               ["mouse", "mousepad"],
               ["mouse", "mousepad"],
               ["mouse", "mousepad"]
           ]
    assert Solution().suggestedProducts(products=["havana"], searchWord="havana") == [["havana"], ["havana"],
                                                                                      ["havana"], ["havana"],
                                                                                      ["havana"], ["havana"]]
    assert Solution().suggestedProducts(products=["bags", "baggage", "banner", "box", "cloths"], searchWord="bags") == [
        ["baggage", "bags", "banner"], ["baggage", "bags", "banner"],
        ["baggage", "bags"], ["bags"]]
