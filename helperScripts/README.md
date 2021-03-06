# Helper Scripts
Collection of command-line tools used in our benchmarking of phylogenetic inference tools. 

### [errorSq.py](errorSq.py): Compute the mean square error between two tn93-format distance files
* For help message: `python errorSq.py -h`

### [fasta2phylip.py](fasta2phylip.py): Convert a FASTA multiple sequence alignment to PHYLIP
* For help message: `python fasta2phylip.py -h`
* Taken from https://github.com/niemasd/tools

### [mantel.py](mantel.py): Calculate the mantel correlation between two tn93-format distance files
* For help message: `python mantel.py -h`

### [nw_error.py](nw_error.py): Compute various error metrics on Newick trees
* For help message: `python nw_error.py -h`
* Taken from https://github.com/niemasd/tools

### [patristic_distances.py](patristic_distances.py): Compute all patristic distances from the given tree
* For help message: `python patristic_distances.py -h`
* Taken from https://github.com/niemasd/tools

### [phylip2fasta.py](phylip2fasta.py): Convert a PHYLIP multiple sequence alignment to FASTA
* For help message: `python phylip2fasta.py -h`

### [resolve_random.py](resolve_random.py): Randomly resolve a multifurcating tree
* Reads multifurcating tree from STDIN and writes resolved tree to STDOUT
* Usage: `resolve_random.R < UNRESOLVED.tre > RESOLVED.tre`
* Taken from https://github.com/niemasd/tools
