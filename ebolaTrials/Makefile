run: MAFFT FastTree IQTree IQTreeMFP RAxML PhyML FastRoot

MAFFT:
	cd ebola0/MAFFT && mafft --reorder --nomemsave --auto ../ebolaSeqs.fas > MAFFT.aln
	cd ebola1/MAFFT && mafft --reorder --nomemsave --auto ../ebolaSeqs.fas > MAFFT.aln
	cd ebola2/MAFFT && mafft --reorder --nomemsave --auto ../ebolaSeqs.fas > MAFFT.aln
	cd ebola3/MAFFT && mafft --reorder --nomemsave --auto ../ebolaSeqs.fas > MAFFT.aln
	cd ebola4/MAFFT && mafft --reorder --nomemsave --auto ../ebolaSeqs.fas > MAFFT.aln
	cd ebola5/MAFFT && mafft --reorder --nomemsave --auto ../ebolaSeqs.fas > MAFFT.aln
	cd ebola6/MAFFT && mafft --reorder --nomemsave --auto ../ebolaSeqs.fas > MAFFT.aln
	cd ebola7/MAFFT && mafft --reorder --nomemsave --auto ../ebolaSeqs.fas > MAFFT.aln
	cd ebola8/MAFFT && mafft --reorder --nomemsave --auto ../ebolaSeqs.fas > MAFFT.aln
	cd ebola9/MAFFT && mafft --reorder --nomemsave --auto ../ebolaSeqs.fas > MAFFT.aln

FastTree:
	cd ebola0/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd ebola1/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd ebola2/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd ebola3/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd ebola4/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd ebola5/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd ebola6/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd ebola7/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd ebola8/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd ebola9/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre

IQTree:
	cd ebola0/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd ebola1/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd ebola2/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd ebola3/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd ebola4/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd ebola5/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd ebola6/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd ebola7/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd ebola8/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd ebola9/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO

IQTreeMFP:
	cd ebola0/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd ebola1/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd ebola2/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd ebola3/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd ebola4/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd ebola5/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd ebola6/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd ebola7/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd ebola8/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd ebola9/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO

RAxML:
	cd ebola0/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd ebola1/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd ebola2/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd ebola3/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd ebola4/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd ebola5/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd ebola6/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd ebola7/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd ebola8/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd ebola9/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G

PhyML:
	cd ebola0/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd ebola1/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd ebola2/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd ebola3/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd ebola4/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd ebola5/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd ebola6/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd ebola7/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd ebola8/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd ebola9/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check

FastRoot:	
	cd ebola0/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd ebola1/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd ebola2/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd ebola3/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd ebola4/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd ebola5/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd ebola6/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd ebola7/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd ebola8/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd ebola9/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	
	cd ebola0/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd ebola1/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd ebola2/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd ebola3/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd ebola4/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd ebola5/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd ebola6/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd ebola7/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd ebola8/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd ebola9/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	
	cd ebola0/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola1/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola2/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola3/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola4/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola5/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola6/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola7/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola8/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola9/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	
	cd ebola0/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola1/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola2/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola3/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola4/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola5/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola6/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola7/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola8/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola9/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	
	cd ebola0/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola1/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola2/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola3/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola4/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola5/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola6/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola7/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola8/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd ebola9/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	
	cd ebola0/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola1/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola2/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola3/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola4/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola5/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola6/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola7/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola8/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd ebola9/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	
	cd ebola0/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd ebola1/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd ebola2/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd ebola3/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd ebola4/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd ebola5/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd ebola6/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd ebola7/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd ebola8/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd ebola9/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	
	cd ebola0/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd ebola1/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd ebola2/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd ebola3/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd ebola4/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd ebola5/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd ebola6/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd ebola7/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd ebola8/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd ebola9/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	
	cd ebola0/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd ebola1/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd ebola2/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd ebola3/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd ebola4/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd ebola5/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd ebola6/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd ebola7/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd ebola8/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd ebola9/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	
	cd ebola0/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd ebola1/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd ebola2/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd ebola3/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd ebola4/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd ebola5/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd ebola6/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd ebola7/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd ebola8/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd ebola9/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre

metrics: msa inference rooting

msa:	
	@mkdir msadists
	@./../helperScripts/fixFastaSpacing.py -i ebola0/MAFFT/MAFFT.aln
	@cat ebola0/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/ebola0_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i ebola0/trueData/ebolaTrueMSA.phy -o ebola0/trueData/ebolaTrueMSA.fasta
	@cat ebola0/trueData/ebolaTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/ebola0_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i ebola1/MAFFT/MAFFT.aln
	@cat ebola1/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/ebola1_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i ebola1/trueData/ebolaTrueMSA.phy -o ebola1/trueData/ebolaTrueMSA.fasta
	@cat ebola1/trueData/ebolaTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/ebola1_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i ebola2/MAFFT/MAFFT.aln
	@cat ebola2/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/ebola2_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i ebola2/trueData/ebolaTrueMSA.phy -o ebola2/trueData/ebolaTrueMSA.fasta
	@cat ebola2/trueData/ebolaTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/ebola2_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i ebola3/MAFFT/MAFFT.aln
	@cat ebola3/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/ebola3_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i ebola3/trueData/ebolaTrueMSA.phy -o ebola3/trueData/ebolaTrueMSA.fasta
	@cat ebola3/trueData/ebolaTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/ebola3_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i ebola4/MAFFT/MAFFT.aln
	@cat ebola4/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/ebola4_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i ebola4/trueData/ebolaTrueMSA.phy -o ebola4/trueData/ebolaTrueMSA.fasta
	@cat ebola4/trueData/ebolaTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/ebola4_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i ebola5/MAFFT/MAFFT.aln
	@cat ebola5/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/ebola5_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i ebola5/trueData/ebolaTrueMSA.phy -o ebola5/trueData/ebolaTrueMSA.fasta
	@cat ebola5/trueData/ebolaTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/ebola5_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i ebola6/MAFFT/MAFFT.aln
	@cat ebola6/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/ebola6_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i ebola6/trueData/ebolaTrueMSA.phy -o ebola6/trueData/ebolaTrueMSA.fasta
	@cat ebola6/trueData/ebolaTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/ebola6_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i ebola7/MAFFT/MAFFT.aln
	@cat ebola7/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/ebola7_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i ebola7/trueData/ebolaTrueMSA.phy -o ebola7/trueData/ebolaTrueMSA.fasta
	@cat ebola7/trueData/ebolaTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/ebola7_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i ebola8/MAFFT/MAFFT.aln
	@cat ebola8/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/ebola8_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i ebola8/trueData/ebolaTrueMSA.phy -o ebola8/trueData/ebolaTrueMSA.fasta
	@cat ebola8/trueData/ebolaTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/ebola8_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i ebola9/MAFFT/MAFFT.aln
	@cat ebola9/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/ebola9_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i ebola9/trueData/ebolaTrueMSA.phy -o ebola9/trueData/ebolaTrueMSA.fasta
	@cat ebola9/trueData/ebolaTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/ebola9_true > /dev/null 2>&1
	
	@echo "MAFFT ErrorSq"
	@./../helperScripts/errorSq.py -d1 msadists/ebola0_MAFFT -d2 msadists/ebola0_true
	@./../helperScripts/errorSq.py -d1 msadists/ebola1_MAFFT -d2 msadists/ebola1_true
	@./../helperScripts/errorSq.py -d1 msadists/ebola2_MAFFT -d2 msadists/ebola2_true
	@./../helperScripts/errorSq.py -d1 msadists/ebola3_MAFFT -d2 msadists/ebola3_true
	@./../helperScripts/errorSq.py -d1 msadists/ebola4_MAFFT -d2 msadists/ebola4_true
	@./../helperScripts/errorSq.py -d1 msadists/ebola5_MAFFT -d2 msadists/ebola5_true
	@./../helperScripts/errorSq.py -d1 msadists/ebola6_MAFFT -d2 msadists/ebola6_true
	@./../helperScripts/errorSq.py -d1 msadists/ebola7_MAFFT -d2 msadists/ebola7_true
	@./../helperScripts/errorSq.py -d1 msadists/ebola8_MAFFT -d2 msadists/ebola8_true
	@./../helperScripts/errorSq.py -d1 msadists/ebola9_MAFFT -d2 msadists/ebola9_true
	
	@echo "MAFFT Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 msadists/ebola0_MAFFT -d2 msadists/ebola0_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/ebola1_MAFFT -d2 msadists/ebola1_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/ebola2_MAFFT -d2 msadists/ebola2_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/ebola3_MAFFT -d2 msadists/ebola3_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/ebola4_MAFFT -d2 msadists/ebola4_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/ebola5_MAFFT -d2 msadists/ebola5_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/ebola6_MAFFT -d2 msadists/ebola6_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/ebola7_MAFFT -d2 msadists/ebola7_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/ebola8_MAFFT -d2 msadists/ebola8_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/ebola9_MAFFT -d2 msadists/ebola9_true -c spearman
	
	@echo "MAFFT Mantel (Pearson)"
	@./../helperScripts/mantel.py -d1 msadists/ebola0_MAFFT -d2 msadists/ebola0_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/ebola1_MAFFT -d2 msadists/ebola1_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/ebola2_MAFFT -d2 msadists/ebola2_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/ebola3_MAFFT -d2 msadists/ebola3_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/ebola4_MAFFT -d2 msadists/ebola4_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/ebola5_MAFFT -d2 msadists/ebola5_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/ebola6_MAFFT -d2 msadists/ebola6_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/ebola7_MAFFT -d2 msadists/ebola7_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/ebola8_MAFFT -d2 msadists/ebola8_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/ebola9_MAFFT -d2 msadists/ebola9_true -c pearson
	
	@rm -rf msadists

inference:
	@echo "FastTree URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola0/FastTree/fast.tre -t2 ../ebolaTrials/ebola0/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola1/FastTree/fast.tre -t2 ../ebolaTrials/ebola1/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola2/FastTree/fast.tre -t2 ../ebolaTrials/ebola2/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola3/FastTree/fast.tre -t2 ../ebolaTrials/ebola3/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola4/FastTree/fast.tre -t2 ../ebolaTrials/ebola4/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola5/FastTree/fast.tre -t2 ../ebolaTrials/ebola5/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola6/FastTree/fast.tre -t2 ../ebolaTrials/ebola6/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola7/FastTree/fast.tre -t2 ../ebolaTrials/ebola7/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola8/FastTree/fast.tre -t2 ../ebolaTrials/ebola8/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola9/FastTree/fast.tre -t2 ../ebolaTrials/ebola9/trueData/ebolaTrueTree.tre --metric URF --normalize 
	
	@echo "IQTree URF" 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola0/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola0/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola1/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola1/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola2/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola2/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola3/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola3/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola4/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola4/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola5/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola5/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola6/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola6/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola7/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola7/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola8/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola8/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola9/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola9/trueData/ebolaTrueTree.tre --metric URF --normalize 
	
	@echo "IQTreeMFP URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola0/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola0/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola1/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola1/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola2/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola2/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola3/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola3/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola4/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola4/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola5/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola5/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola6/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola6/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola7/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola7/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola8/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola8/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola9/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola9/trueData/ebolaTrueTree.tre --metric URF --normalize 
	
	@echo "RAxML URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola0/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola0/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola1/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola1/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola2/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola2/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola3/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola3/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola4/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola4/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola5/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola5/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola6/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola6/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola7/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola7/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola8/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola8/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola9/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola9/trueData/ebolaTrueTree.tre --metric URF --normalize 
	
	@echo "PhyML URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola0/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola0/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola1/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola1/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola2/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola2/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola3/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola3/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola4/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola4/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola5/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola5/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola6/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola6/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola7/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola7/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola8/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola8/trueData/ebolaTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola9/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola9/trueData/ebolaTrueTree.tre --metric URF --normalize 
	
	@echo "FastTree WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola0/FastTree/fast.tre -t2 ../ebolaTrials/ebola0/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola1/FastTree/fast.tre -t2 ../ebolaTrials/ebola1/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola2/FastTree/fast.tre -t2 ../ebolaTrials/ebola2/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola3/FastTree/fast.tre -t2 ../ebolaTrials/ebola3/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola4/FastTree/fast.tre -t2 ../ebolaTrials/ebola4/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola5/FastTree/fast.tre -t2 ../ebolaTrials/ebola5/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola6/FastTree/fast.tre -t2 ../ebolaTrials/ebola6/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola7/FastTree/fast.tre -t2 ../ebolaTrials/ebola7/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola8/FastTree/fast.tre -t2 ../ebolaTrials/ebola8/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola9/FastTree/fast.tre -t2 ../ebolaTrials/ebola9/trueData/ebolaTrueTree.tre --metric WRF 
	
	@echo "IQTree WRF"	
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola0/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola0/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola1/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola1/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola2/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola2/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola3/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola3/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola4/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola4/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola5/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola5/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola6/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola6/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola7/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola7/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola8/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola8/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola9/IQTree/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola9/trueData/ebolaTrueTree.tre --metric WRF 
	
	@echo "IQTreeMFP WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola0/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola0/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola1/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola1/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola2/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola2/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola3/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola3/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola4/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola4/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola5/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola5/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola6/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola6/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola7/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola7/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola8/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola8/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola9/IQTreeMFP/MAFFT.aln.treefile -t2 ../ebolaTrials/ebola9/trueData/ebolaTrueTree.tre --metric WRF 
	
	@echo "RAxML WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola0/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola0/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola1/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola1/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola2/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola2/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola3/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola3/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola4/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola4/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola5/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola5/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola6/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola6/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola7/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola7/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola8/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola8/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola9/RAxML/MAFFT.aln.raxml.bestTree -t2 ../ebolaTrials/ebola9/trueData/ebolaTrueTree.tre --metric WRF 
	
	@echo "PhyML WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola0/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola0/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola1/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola1/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola2/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola2/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola3/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola3/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola4/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola4/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola5/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola5/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola6/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola6/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola7/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola7/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola8/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola8/trueData/ebolaTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../ebolaTrials/ebola9/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../ebolaTrials/ebola9/trueData/ebolaTrueTree.tre --metric WRF 
	
	@mkdir patristic_distances
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola0/FastTree/fast.tre -o ebola0_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola0/IQTree/MAFFT.aln.treefile -o ebola0_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola0/IQTreeMFP/MAFFT.aln.treefile -o ebola0_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola0/RAxML/MAFFT.aln.raxml.bestTree -o ebola0_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola0/PhyML/MAFFT.phy_phyml_tree.txt -o ebola0_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola0/trueData/ebolaTrueTree.tre -o ebola0_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola1/FastTree/fast.tre -o ebola1_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola1/IQTree/MAFFT.aln.treefile -o ebola1_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola1/IQTreeMFP/MAFFT.aln.treefile -o ebola1_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola1/RAxML/MAFFT.aln.raxml.bestTree -o ebola1_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola1/PhyML/MAFFT.phy_phyml_tree.txt -o ebola1_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola1/trueData/ebolaTrueTree.tre -o ebola1_true
		
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola2/FastTree/fast.tre -o ebola2_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola2/IQTree/MAFFT.aln.treefile -o ebola2_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola2/IQTreeMFP/MAFFT.aln.treefile -o ebola2_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola2/RAxML/MAFFT.aln.raxml.bestTree -o ebola2_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola2/PhyML/MAFFT.phy_phyml_tree.txt -o ebola2_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola2/trueData/ebolaTrueTree.tre -o ebola2_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola3/FastTree/fast.tre -o ebola3_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola3/IQTree/MAFFT.aln.treefile -o ebola3_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola3/IQTreeMFP/MAFFT.aln.treefile -o ebola3_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola3/RAxML/MAFFT.aln.raxml.bestTree -o ebola3_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola3/PhyML/MAFFT.phy_phyml_tree.txt -o ebola3_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola3/trueData/ebolaTrueTree.tre -o ebola3_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola4/FastTree/fast.tre -o ebola4_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola4/IQTree/MAFFT.aln.treefile -o ebola4_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola4/IQTreeMFP/MAFFT.aln.treefile -o ebola4_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola4/RAxML/MAFFT.aln.raxml.bestTree -o ebola4_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola4/PhyML/MAFFT.phy_phyml_tree.txt -o ebola4_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola4/trueData/ebolaTrueTree.tre -o ebola4_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola5/FastTree/fast.tre -o ebola5_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola5/IQTree/MAFFT.aln.treefile -o ebola5_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola5/IQTreeMFP/MAFFT.aln.treefile -o ebola5_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola5/RAxML/MAFFT.aln.raxml.bestTree -o ebola5_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola5/PhyML/MAFFT.phy_phyml_tree.txt -o ebola5_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola5/trueData/ebolaTrueTree.tre -o ebola5_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola6/FastTree/fast.tre -o ebola6_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola6/IQTree/MAFFT.aln.treefile -o ebola6_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola6/IQTreeMFP/MAFFT.aln.treefile -o ebola6_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola6/RAxML/MAFFT.aln.raxml.bestTree -o ebola6_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola6/PhyML/MAFFT.phy_phyml_tree.txt -o ebola6_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola6/trueData/ebolaTrueTree.tre -o ebola6_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola7/FastTree/fast.tre -o ebola7_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola7/IQTree/MAFFT.aln.treefile -o ebola7_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola7/IQTreeMFP/MAFFT.aln.treefile -o ebola7_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola7/RAxML/MAFFT.aln.raxml.bestTree -o ebola7_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola7/PhyML/MAFFT.phy_phyml_tree.txt -o ebola7_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola7/trueData/ebolaTrueTree.tre -o ebola7_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola8/FastTree/fast.tre -o ebola8_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola8/IQTree/MAFFT.aln.treefile -o ebola8_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola8/IQTreeMFP/MAFFT.aln.treefile -o ebola8_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola8/RAxML/MAFFT.aln.raxml.bestTree -o ebola8_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola8/PhyML/MAFFT.phy_phyml_tree.txt -o ebola8_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola8/trueData/ebolaTrueTree.tre -o ebola8_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola9/FastTree/fast.tre -o ebola9_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola9/IQTree/MAFFT.aln.treefile -o ebola9_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola9/IQTreeMFP/MAFFT.aln.treefile -o ebola9_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola9/RAxML/MAFFT.aln.raxml.bestTree -o ebola9_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola9/PhyML/MAFFT.phy_phyml_tree.txt -o ebola9_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../ebola9/trueData/ebolaTrueTree.tre -o ebola9_true
	
	@echo "FastTree Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_FastTree --correlation spearman 
	
	@echo "IQTree Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_IQTree --correlation spearman 
	
	@echo "IQTreeMFP Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_IQTreeMFP --correlation spearman 
	
	@echo "PhyML Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_PhyML --correlation spearman 
	
	@echo "RAxML Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_RAxML --correlation spearman 
	
	@echo "FastTree Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_FastTree --correlation pearson 
	
	@echo "IQTree Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_IQTree --correlation pearson 
	
	@echo "IQTreeMFP Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_IQTreeMFP --correlation pearson 
	
	@echo "PhyML Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_PhyML --correlation pearson 
	
	@echo "RAxML Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_RAxML --correlation pearson 
	
	@echo "FastTree ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_FastTree 
	
	@echo "IQTREE ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_IQTree 
	
	@echo "IQTreeMFP ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_IQTreeMFP 
	
	@echo "RAxML ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_RAxML 
	
	@echo "PhyML ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola0_true -d2 patristic_distances/ebola0_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola1_true -d2 patristic_distances/ebola1_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola2_true -d2 patristic_distances/ebola2_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola3_true -d2 patristic_distances/ebola3_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola4_true -d2 patristic_distances/ebola4_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola5_true -d2 patristic_distances/ebola5_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola6_true -d2 patristic_distances/ebola6_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola7_true -d2 patristic_distances/ebola7_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola8_true -d2 patristic_distances/ebola8_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/ebola9_true -d2 patristic_distances/ebola9_PhyML 
	
	@rm -rf patristic_distances
		
rooting:
	@echo "FastTree MinVar"
	@./../helperScripts/delta_triplet_dist ebola0/trueData/ebolaTrueTree.tre ebola0/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola1/trueData/ebolaTrueTree.tre ebola1/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola2/trueData/ebolaTrueTree.tre ebola2/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola3/trueData/ebolaTrueTree.tre ebola3/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola4/trueData/ebolaTrueTree.tre ebola4/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola5/trueData/ebolaTrueTree.tre ebola5/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola6/trueData/ebolaTrueTree.tre ebola6/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola7/trueData/ebolaTrueTree.tre ebola7/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola8/trueData/ebolaTrueTree.tre ebola8/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola9/trueData/ebolaTrueTree.tre ebola9/FastTree/MinVarRooted.tre
	
	@echo "FastTree MidPoint"
	@./../helperScripts/delta_triplet_dist ebola0/trueData/ebolaTrueTree.tre ebola0/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola1/trueData/ebolaTrueTree.tre ebola1/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola2/trueData/ebolaTrueTree.tre ebola2/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola3/trueData/ebolaTrueTree.tre ebola3/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola4/trueData/ebolaTrueTree.tre ebola4/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola5/trueData/ebolaTrueTree.tre ebola5/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola6/trueData/ebolaTrueTree.tre ebola6/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola7/trueData/ebolaTrueTree.tre ebola7/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola8/trueData/ebolaTrueTree.tre ebola8/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola9/trueData/ebolaTrueTree.tre ebola9/FastTree/MidPointRooted.tre
	
	@echo "IQTree MinVar"
	@./../helperScripts/delta_triplet_dist ebola0/trueData/ebolaTrueTree.tre ebola0/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola1/trueData/ebolaTrueTree.tre ebola1/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola2/trueData/ebolaTrueTree.tre ebola2/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola3/trueData/ebolaTrueTree.tre ebola3/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola4/trueData/ebolaTrueTree.tre ebola4/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola5/trueData/ebolaTrueTree.tre ebola5/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola6/trueData/ebolaTrueTree.tre ebola6/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola7/trueData/ebolaTrueTree.tre ebola7/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola8/trueData/ebolaTrueTree.tre ebola8/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola9/trueData/ebolaTrueTree.tre ebola9/IQTree/MinVarRooted.tre
	
	@echo "IQTree MidPoint"
	@./../helperScripts/delta_triplet_dist ebola0/trueData/ebolaTrueTree.tre ebola0/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola1/trueData/ebolaTrueTree.tre ebola1/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola2/trueData/ebolaTrueTree.tre ebola2/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola3/trueData/ebolaTrueTree.tre ebola3/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola4/trueData/ebolaTrueTree.tre ebola4/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola5/trueData/ebolaTrueTree.tre ebola5/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola6/trueData/ebolaTrueTree.tre ebola6/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola7/trueData/ebolaTrueTree.tre ebola7/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola8/trueData/ebolaTrueTree.tre ebola8/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola9/trueData/ebolaTrueTree.tre ebola9/IQTree/MidPointRooted.tre
	
	@echo "IQTreeMFP MinVar"
	@./../helperScripts/delta_triplet_dist ebola0/trueData/ebolaTrueTree.tre ebola0/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola1/trueData/ebolaTrueTree.tre ebola1/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola2/trueData/ebolaTrueTree.tre ebola2/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola3/trueData/ebolaTrueTree.tre ebola3/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola4/trueData/ebolaTrueTree.tre ebola4/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola5/trueData/ebolaTrueTree.tre ebola5/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola6/trueData/ebolaTrueTree.tre ebola6/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola7/trueData/ebolaTrueTree.tre ebola7/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola8/trueData/ebolaTrueTree.tre ebola8/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola9/trueData/ebolaTrueTree.tre ebola9/IQTreeMFP/MinVarRooted.tre
	
	@echo "IQTreeMFP MidPoint"
	@./../helperScripts/delta_triplet_dist ebola0/trueData/ebolaTrueTree.tre ebola0/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola1/trueData/ebolaTrueTree.tre ebola1/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola2/trueData/ebolaTrueTree.tre ebola2/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola3/trueData/ebolaTrueTree.tre ebola3/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola4/trueData/ebolaTrueTree.tre ebola4/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola5/trueData/ebolaTrueTree.tre ebola5/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola6/trueData/ebolaTrueTree.tre ebola6/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola7/trueData/ebolaTrueTree.tre ebola7/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola8/trueData/ebolaTrueTree.tre ebola8/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola9/trueData/ebolaTrueTree.tre ebola9/IQTreeMFP/MidPointRooted.tre
	
	@echo "RAxML MinVar"
	@./../helperScripts/delta_triplet_dist ebola0/trueData/ebolaTrueTree.tre ebola0/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola1/trueData/ebolaTrueTree.tre ebola1/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola2/trueData/ebolaTrueTree.tre ebola2/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola3/trueData/ebolaTrueTree.tre ebola3/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola4/trueData/ebolaTrueTree.tre ebola4/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola5/trueData/ebolaTrueTree.tre ebola5/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola6/trueData/ebolaTrueTree.tre ebola6/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola7/trueData/ebolaTrueTree.tre ebola7/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola8/trueData/ebolaTrueTree.tre ebola8/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola9/trueData/ebolaTrueTree.tre ebola9/RAxML/MinVarRooted.tre
	
	@echo "RAxML MidPoint"
	@./../helperScripts/delta_triplet_dist ebola0/trueData/ebolaTrueTree.tre ebola0/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola1/trueData/ebolaTrueTree.tre ebola1/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola2/trueData/ebolaTrueTree.tre ebola2/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola3/trueData/ebolaTrueTree.tre ebola3/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola4/trueData/ebolaTrueTree.tre ebola4/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola5/trueData/ebolaTrueTree.tre ebola5/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola6/trueData/ebolaTrueTree.tre ebola6/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola7/trueData/ebolaTrueTree.tre ebola7/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola8/trueData/ebolaTrueTree.tre ebola8/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola9/trueData/ebolaTrueTree.tre ebola9/RAxML/MidPointRooted.tre
	
	@echo "PhyML MinVar"
	@./../helperScripts/delta_triplet_dist ebola0/trueData/ebolaTrueTree.tre ebola0/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola1/trueData/ebolaTrueTree.tre ebola1/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola2/trueData/ebolaTrueTree.tre ebola2/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola3/trueData/ebolaTrueTree.tre ebola3/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola4/trueData/ebolaTrueTree.tre ebola4/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola5/trueData/ebolaTrueTree.tre ebola5/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola6/trueData/ebolaTrueTree.tre ebola6/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola7/trueData/ebolaTrueTree.tre ebola7/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola8/trueData/ebolaTrueTree.tre ebola8/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist ebola9/trueData/ebolaTrueTree.tre ebola9/PhyML/MinVarRooted.tre
		
	@echo "PhyML MidPoint"
	@./../helperScripts/delta_triplet_dist ebola0/trueData/ebolaTrueTree.tre ebola0/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola1/trueData/ebolaTrueTree.tre ebola1/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola2/trueData/ebolaTrueTree.tre ebola2/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola3/trueData/ebolaTrueTree.tre ebola3/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola4/trueData/ebolaTrueTree.tre ebola4/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola5/trueData/ebolaTrueTree.tre ebola5/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola6/trueData/ebolaTrueTree.tre ebola6/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola7/trueData/ebolaTrueTree.tre ebola7/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola8/trueData/ebolaTrueTree.tre ebola8/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist ebola9/trueData/ebolaTrueTree.tre ebola9/PhyML/MidPointRooted.tre
