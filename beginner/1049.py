vertebrado_tree = {	'ave': { 'carnivoro': 'aguia', 'onivoro': 'pomba' },
					'mamifero': { 'onivoro': 'homem', 'herbivoro': 'vaca' }}
invertebrado_tree = { 'inseto': { 'hematofago': 'pulga', 'herbivoro': 'lagarta' },
					  'anelideo': { 'hematofago': 'sanguessuga', 'onivoro': 'minhoca' }}
def tree_walk(tree, search_terms):
	tmp_tree = tree
	for term in search_terms:
		tmp_tree = tmp_tree[term]
	return tmp_tree

terms = [input() for _ in range(3)]
if terms[0] == 'invertebrado':
	print(tree_walk(invertebrado_tree, terms[1:]))
else:
	print(tree_walk(vertebrado_tree, terms[1:]))