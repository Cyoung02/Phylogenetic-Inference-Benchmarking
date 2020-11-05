# Phylogenetic Inference Benchmarking
This repository contains molecular epidemiological analyses of data simulated from real-world Ebolavirus, HIV, and HCV viral sequence data. 

## Simulating Data
The Ebolavirus dataset obtained from the [Los Alamos National Laboratory (LANL) HFV Sequence Database](https://hfv.lanl.gov/content/sequence/NEWALIGN/align.html) as follows:

* **Alignment type:** Whole set
* **Year:** 2015-07
* **Genus:** Ebolavirus
* **DNA/Protein:** DNA
* **Region:** genome
* **Number of sequences:** 710

The HCV dataset was obtained from the [Los Alamos National Laboratory (LANL) HCV Sequence Database](https://hcv.lanl.gov/content/sequence/NEWALIGN/align.html) as follows:

* **Alignment type:** Web alignment (all complete sequences)
* **Year:** 2008
* **Organism:** HCV
* **DNA/Protein:** DNA
* **Region:** genome
* **Number of sequences:** 471

The HIV-1 dataset obtained from the [Los Alamos National Laboratory (LANL) HIV Sequence Database](https://www.hiv.lanl.gov/content/sequence/NEWALIGN/align.html) as follows:

* **Alignment type:** Web alignment (all complete sequences)
* **Year:** 2018
* **Organism:** HIV-1/SIVcpz
* **DNA/Protein:** DNA
* **Region:** genome
* **Subtype:** All
* **Number of sequences:** 4004

From each curated alignment, we used [IQ-TREE](https://github.com/Cibiv/IQ-TREE) to infer a phylogeny under the General Time Reversible model of sequence evolution with invariable sites and gamma-distributed site-rate heterogeneity with 20 categories. From the IQ-TREE results, we obtained the phylogeny, the GTR substitution model parameters, the proportion of invariable sites, and the shape of the gamma distribution. The phylogeny was subsequently rooted using [FastRoot minimum variance rooting](https://github.com/uym2/MinVar-Rooting), and a tree with 100 leaves was subsampled from it. These parameters were then used to simulate sequence alignments from the subsample of the inferred phylogeny using [INDELible](https://github.com/kloetzl/indelible). 10 replicate datasets were generated for each virus.

## Running Multiple Sequence Alignment
[Clustal Omega](http://www.clustal.org/omega/) was run as follows:
`clustalo -v --auto -i unalignedSequences -o Clustal.aln`

[MUSCLE](https://www.drive5.com/muscle/downloads.htm) was run as follows:
`muscle -in unalignedSequences -out MUSCLE.aln`

[MAFFT](https://mafft.cbrc.jp/alignment/software/) was run as follows:
`mafft --reorder --auto unaligedSequences > MAFFT.aln`

## Running Phylogenetic Inference
[FastTree](http://microbesonline.org/fasttree/) was run as follows:  
`cat alignedSequences | FastTree -gamma -nt -gtr -out fast.tre`

[IQ-TREE](https://github.com/Cibiv/IQ-TREE) was run as follows:
`iqtree -m GTR+I+R -s alignedSequences -nt AUTO`

IQ-TREE (MFP) was run as follows:
`iqtree -m MFP -s alignedSequences -nt AUTO`

[RAxML-NG](https://github.com/amkozlov/raxml-ng) was run as follows:
`raxml-ng --msa alignedSequences --model GTR+FO+I+R4`

[PhyML](https://github.com/stephaneguindon/phyml) was run as follows:
`phyml -i alignedSequences -a e -d nt -m GTR`  
Note: PhyML only takes sequences in PHYLIP format. A script has been included in [helperScripts](https://github.com/Cyoung02/SimulatedEvaluationFramework/tree/master/helperScripts) which converts FASTA to PHYLIP.

## Optimizing Branch Lengths along FastTree Topology
[IQ-TREE](https://github.com/Cibiv/IQ-TREE) was run as follows:
`iqtree -m GTR+I+R -s alignedSequences -nt AUTO -te fastTreeFile`

IQ-TREE (MFP) was run as follows:
`iqtree -m MFP -s MAFFT.aln -nt AUTO -te fastTreeFile`

[RAxML-NG](https://github.com/amkozlov/raxml-ng) was run as follows:
`raxml-ng --msa alignedSequences --model GTR+FO+I+R4 --evaluate --tree resolvedFastTreeFile`  
Note: RAxML only accepts trees which are strictly bifurcating. A script has been included in [helperScripts](https://github.com/Cyoung02/SimulatedEvaluationFramework/tree/master/helperScripts) which resolves polytomies.

[PhyML](https://github.com/stephaneguindon/phyml) was run as follows:
`phyml -i alignedSequences -a e -d nt -m GTR -o lr -u resolvedFastTreeFile`  
Note: PhyML only accepts trees which are strictly bifurcating. A script has been included in [helperScripts](https://github.com/Cyoung02/SimulatedEvaluationFramework/tree/master/helperScripts) which resolves polytomies.