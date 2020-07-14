run: MAFFT FastTree IQTree IQTreeMFP RAxML PhyML FastRoot

MAFFT:
	cd hcv0/MAFFT && mafft --reorder --nomemsave --auto ../hcvSeqs.fas > MAFFT.aln
	cd hcv1/MAFFT && mafft --reorder --nomemsave --auto ../hcvSeqs.fas > MAFFT.aln
	cd hcv2/MAFFT && mafft --reorder --nomemsave --auto ../hcvSeqs.fas > MAFFT.aln
	cd hcv3/MAFFT && mafft --reorder --nomemsave --auto ../hcvSeqs.fas > MAFFT.aln
	cd hcv4/MAFFT && mafft --reorder --nomemsave --auto ../hcvSeqs.fas > MAFFT.aln
	cd hcv5/MAFFT && mafft --reorder --nomemsave --auto ../hcvSeqs.fas > MAFFT.aln
	cd hcv6/MAFFT && mafft --reorder --nomemsave --auto ../hcvSeqs.fas > MAFFT.aln
	cd hcv7/MAFFT && mafft --reorder --nomemsave --auto ../hcvSeqs.fas > MAFFT.aln
	cd hcv8/MAFFT && mafft --reorder --nomemsave --auto ../hcvSeqs.fas > MAFFT.aln
	cd hcv9/MAFFT && mafft --reorder --nomemsave --auto ../hcvSeqs.fas > MAFFT.aln

FastTree:
	cd hcv0/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hcv1/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hcv2/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hcv3/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hcv4/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hcv5/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hcv6/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hcv7/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hcv8/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hcv9/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre

IQTree:
	cd hcv0/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hcv1/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hcv2/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hcv3/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hcv4/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hcv5/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hcv6/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hcv7/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hcv8/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hcv9/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO

IQTreeMFP:
	cd hcv0/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hcv1/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hcv2/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hcv3/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hcv4/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hcv5/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hcv6/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hcv7/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hcv8/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hcv9/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO

RAxML:
	cd hcv0/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hcv1/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hcv2/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hcv3/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hcv4/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hcv5/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hcv6/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hcv7/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hcv8/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hcv9/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G

PhyML:
	cd hcv0/PhyML && ../../../helperScripts/fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hcv1/PhyML && ../../../helperScripts/fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hcv2/PhyML && ../../../helperScripts/fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hcv3/PhyML && ../../../helperScripts/fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hcv4/PhyML && ../../../helperScripts/fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hcv5/PhyML && ../../../helperScripts/fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hcv6/PhyML && ../../../helperScripts/fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hcv7/PhyML && ../../../helperScripts/fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hcv8/PhyML && ../../../helperScripts/fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hcv9/PhyML && ../../../helperScripts/fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check

FastRoot:	
	cd hcv0/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hcv1/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hcv2/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hcv3/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hcv4/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hcv5/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hcv6/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hcv7/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hcv8/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hcv9/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	
	cd hcv0/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hcv1/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hcv2/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hcv3/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hcv4/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hcv5/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hcv6/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hcv7/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hcv8/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hcv9/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	
	cd hcv0/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv1/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv2/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv3/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv4/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv5/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv6/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv7/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv8/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv9/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	
	cd hcv0/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv1/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv2/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv3/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv4/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv5/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv6/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv7/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv8/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv9/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	
	cd hcv0/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv1/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv2/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv3/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv4/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv5/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv6/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv7/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv8/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hcv9/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	
	cd hcv0/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv1/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv2/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv3/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv4/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv5/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv6/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv7/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv8/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hcv9/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	
	cd hcv0/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hcv1/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hcv2/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hcv3/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hcv4/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hcv5/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hcv6/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hcv7/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hcv8/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hcv9/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	
	cd hcv0/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hcv1/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hcv2/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hcv3/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hcv4/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hcv5/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hcv6/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hcv7/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hcv8/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hcv9/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	
	cd hcv0/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hcv1/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hcv2/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hcv3/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hcv4/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hcv5/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hcv6/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hcv7/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hcv8/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hcv9/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	
	cd hcv0/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hcv1/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hcv2/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hcv3/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hcv4/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hcv5/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hcv6/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hcv7/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hcv8/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hcv9/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre

metrics: msa inference rooting

msa:	
	@mkdir msadists
	@./../helperScripts/fixFastaSpacing.py -i hcv0/MAFFT/MAFFT.aln
	@cat hcv0/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/hcv0_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hcv0/trueData/hcvTrueMSA.phy -o hcv0/trueData/hcvTrueMSA.fasta
	@cat hcv0/trueData/hcvTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/hcv0_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i hcv1/MAFFT/MAFFT.aln
	@cat hcv1/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/hcv1_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hcv1/trueData/hcvTrueMSA.phy -o hcv1/trueData/hcvTrueMSA.fasta
	@cat hcv1/trueData/hcvTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/hcv1_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i hcv2/MAFFT/MAFFT.aln
	@cat hcv2/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/hcv2_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hcv2/trueData/hcvTrueMSA.phy -o hcv2/trueData/hcvTrueMSA.fasta
	@cat hcv2/trueData/hcvTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/hcv2_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i hcv3/MAFFT/MAFFT.aln
	@cat hcv3/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/hcv3_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hcv3/trueData/hcvTrueMSA.phy -o hcv3/trueData/hcvTrueMSA.fasta
	@cat hcv3/trueData/hcvTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/hcv3_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i hcv4/MAFFT/MAFFT.aln
	@cat hcv4/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/hcv4_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hcv4/trueData/hcvTrueMSA.phy -o hcv4/trueData/hcvTrueMSA.fasta
	@cat hcv4/trueData/hcvTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/hcv4_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i hcv5/MAFFT/MAFFT.aln
	@cat hcv5/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/hcv5_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hcv5/trueData/hcvTrueMSA.phy -o hcv5/trueData/hcvTrueMSA.fasta
	@cat hcv5/trueData/hcvTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/hcv5_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i hcv6/MAFFT/MAFFT.aln
	@cat hcv6/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/hcv6_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hcv6/trueData/hcvTrueMSA.phy -o hcv6/trueData/hcvTrueMSA.fasta
	@cat hcv6/trueData/hcvTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/hcv6_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i hcv7/MAFFT/MAFFT.aln
	@cat hcv7/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/hcv7_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hcv7/trueData/hcvTrueMSA.phy -o hcv7/trueData/hcvTrueMSA.fasta
	@cat hcv7/trueData/hcvTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/hcv7_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i hcv8/MAFFT/MAFFT.aln
	@cat hcv8/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/hcv8_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hcv8/trueData/hcvTrueMSA.phy -o hcv8/trueData/hcvTrueMSA.fasta
	@cat hcv8/trueData/hcvTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/hcv8_true > /dev/null 2>&1
	
	@./../helperScripts/fixFastaSpacing.py -i hcv9/MAFFT/MAFFT.aln
	@cat hcv9/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o msadists/hcv9_MAFFT > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hcv9/trueData/hcvTrueMSA.phy -o hcv9/trueData/hcvTrueMSA.fasta
	@cat hcv9/trueData/hcvTrueMSA.fasta | tn93 -t 1 -l 1 -q -o msadists/hcv9_true > /dev/null 2>&1
	
	@echo "MAFFT ErrorSq"
	@./../helperScripts/errorSq.py -d1 msadists/hcv0_MAFFT -d2 msadists/hcv0_true
	@./../helperScripts/errorSq.py -d1 msadists/hcv1_MAFFT -d2 msadists/hcv1_true
	@./../helperScripts/errorSq.py -d1 msadists/hcv2_MAFFT -d2 msadists/hcv2_true
	@./../helperScripts/errorSq.py -d1 msadists/hcv3_MAFFT -d2 msadists/hcv3_true
	@./../helperScripts/errorSq.py -d1 msadists/hcv4_MAFFT -d2 msadists/hcv4_true
	@./../helperScripts/errorSq.py -d1 msadists/hcv5_MAFFT -d2 msadists/hcv5_true
	@./../helperScripts/errorSq.py -d1 msadists/hcv6_MAFFT -d2 msadists/hcv6_true
	@./../helperScripts/errorSq.py -d1 msadists/hcv7_MAFFT -d2 msadists/hcv7_true
	@./../helperScripts/errorSq.py -d1 msadists/hcv8_MAFFT -d2 msadists/hcv8_true
	@./../helperScripts/errorSq.py -d1 msadists/hcv9_MAFFT -d2 msadists/hcv9_true
	
	@echo "MAFFT Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 msadists/hcv0_MAFFT -d2 msadists/hcv0_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/hcv1_MAFFT -d2 msadists/hcv1_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/hcv2_MAFFT -d2 msadists/hcv2_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/hcv3_MAFFT -d2 msadists/hcv3_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/hcv4_MAFFT -d2 msadists/hcv4_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/hcv5_MAFFT -d2 msadists/hcv5_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/hcv6_MAFFT -d2 msadists/hcv6_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/hcv7_MAFFT -d2 msadists/hcv7_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/hcv8_MAFFT -d2 msadists/hcv8_true -c spearman
	@./../helperScripts/mantel.py -d1 msadists/hcv9_MAFFT -d2 msadists/hcv9_true -c spearman
	
	@echo "MAFFT Mantel (Pearson)"
	@./../helperScripts/mantel.py -d1 msadists/hcv0_MAFFT -d2 msadists/hcv0_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/hcv1_MAFFT -d2 msadists/hcv1_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/hcv2_MAFFT -d2 msadists/hcv2_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/hcv3_MAFFT -d2 msadists/hcv3_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/hcv4_MAFFT -d2 msadists/hcv4_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/hcv5_MAFFT -d2 msadists/hcv5_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/hcv6_MAFFT -d2 msadists/hcv6_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/hcv7_MAFFT -d2 msadists/hcv7_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/hcv8_MAFFT -d2 msadists/hcv8_true -c pearson
	@./../helperScripts/mantel.py -d1 msadists/hcv9_MAFFT -d2 msadists/hcv9_true -c pearson
	
	@rm -rf msadists

inference:
	@echo "FastTree URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv0/FastTree/fast.tre -t2 ../hcvTrials/hcv0/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv1/FastTree/fast.tre -t2 ../hcvTrials/hcv1/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv2/FastTree/fast.tre -t2 ../hcvTrials/hcv2/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv3/FastTree/fast.tre -t2 ../hcvTrials/hcv3/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv4/FastTree/fast.tre -t2 ../hcvTrials/hcv4/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv5/FastTree/fast.tre -t2 ../hcvTrials/hcv5/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv6/FastTree/fast.tre -t2 ../hcvTrials/hcv6/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv7/FastTree/fast.tre -t2 ../hcvTrials/hcv7/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv8/FastTree/fast.tre -t2 ../hcvTrials/hcv8/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv9/FastTree/fast.tre -t2 ../hcvTrials/hcv9/trueData/hcvTrueTree.tre --metric URF --normalize 
	
	@echo "IQTree URF" 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv0/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv0/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv1/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv1/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv2/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv2/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv3/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv3/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv4/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv4/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv5/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv5/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv6/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv6/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv7/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv7/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv8/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv8/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv9/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv9/trueData/hcvTrueTree.tre --metric URF --normalize 
	
	@echo "IQTreeMFP URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv0/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv0/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv1/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv1/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv2/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv2/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv3/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv3/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv4/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv4/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv5/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv5/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv6/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv6/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv7/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv7/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv8/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv8/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv9/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv9/trueData/hcvTrueTree.tre --metric URF --normalize 
	
	@echo "RAxML URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv0/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv0/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv1/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv1/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv2/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv2/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv3/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv3/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv4/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv4/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv5/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv5/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv6/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv6/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv7/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv7/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv8/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv8/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv9/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv9/trueData/hcvTrueTree.tre --metric URF --normalize 
	
	@echo "PhyML URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv0/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv0/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv1/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv1/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv2/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv2/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv3/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv3/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv4/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv4/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv5/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv5/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv6/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv6/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv7/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv7/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv8/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv8/trueData/hcvTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv9/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv9/trueData/hcvTrueTree.tre --metric URF --normalize 
	
	@echo "FastTree WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv0/FastTree/fast.tre -t2 ../hcvTrials/hcv0/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv1/FastTree/fast.tre -t2 ../hcvTrials/hcv1/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv2/FastTree/fast.tre -t2 ../hcvTrials/hcv2/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv3/FastTree/fast.tre -t2 ../hcvTrials/hcv3/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv4/FastTree/fast.tre -t2 ../hcvTrials/hcv4/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv5/FastTree/fast.tre -t2 ../hcvTrials/hcv5/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv6/FastTree/fast.tre -t2 ../hcvTrials/hcv6/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv7/FastTree/fast.tre -t2 ../hcvTrials/hcv7/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv8/FastTree/fast.tre -t2 ../hcvTrials/hcv8/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv9/FastTree/fast.tre -t2 ../hcvTrials/hcv9/trueData/hcvTrueTree.tre --metric WRF 
	
	@echo "IQTree WRF"	
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv0/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv0/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv1/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv1/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv2/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv2/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv3/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv3/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv4/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv4/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv5/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv5/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv6/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv6/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv7/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv7/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv8/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv8/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv9/IQTree/MAFFT.aln.treefile -t2 ../hcvTrials/hcv9/trueData/hcvTrueTree.tre --metric WRF 
	
	@echo "IQTreeMFP WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv0/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv0/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv1/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv1/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv2/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv2/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv3/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv3/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv4/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv4/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv5/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv5/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv6/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv6/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv7/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv7/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv8/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv8/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv9/IQTreeMFP/MAFFT.aln.treefile -t2 ../hcvTrials/hcv9/trueData/hcvTrueTree.tre --metric WRF 
	
	@echo "RAxML WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv0/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv0/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv1/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv1/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv2/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv2/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv3/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv3/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv4/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv4/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv5/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv5/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv6/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv6/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv7/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv7/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv8/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv8/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv9/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hcvTrials/hcv9/trueData/hcvTrueTree.tre --metric WRF 
	
	@echo "PhyML WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv0/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv0/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv1/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv1/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv2/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv2/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv3/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv3/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv4/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv4/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv5/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv5/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv6/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv6/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv7/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv7/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv8/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv8/trueData/hcvTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hcvTrials/hcv9/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hcvTrials/hcv9/trueData/hcvTrueTree.tre --metric WRF 
	
	@mkdir patristic_distances
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv0/FastTree/fast.tre -o hcv0_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv0/IQTree/MAFFT.aln.treefile -o hcv0_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv0/IQTreeMFP/MAFFT.aln.treefile -o hcv0_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv0/RAxML/MAFFT.aln.raxml.bestTree -o hcv0_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv0/PhyML/MAFFT.phy_phyml_tree.txt -o hcv0_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv0/trueData/hcvTrueTree.tre -o hcv0_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv1/FastTree/fast.tre -o hcv1_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv1/IQTree/MAFFT.aln.treefile -o hcv1_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv1/IQTreeMFP/MAFFT.aln.treefile -o hcv1_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv1/RAxML/MAFFT.aln.raxml.bestTree -o hcv1_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv1/PhyML/MAFFT.phy_phyml_tree.txt -o hcv1_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv1/trueData/hcvTrueTree.tre -o hcv1_true
		
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv2/FastTree/fast.tre -o hcv2_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv2/IQTree/MAFFT.aln.treefile -o hcv2_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv2/IQTreeMFP/MAFFT.aln.treefile -o hcv2_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv2/RAxML/MAFFT.aln.raxml.bestTree -o hcv2_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv2/PhyML/MAFFT.phy_phyml_tree.txt -o hcv2_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv2/trueData/hcvTrueTree.tre -o hcv2_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv3/FastTree/fast.tre -o hcv3_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv3/IQTree/MAFFT.aln.treefile -o hcv3_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv3/IQTreeMFP/MAFFT.aln.treefile -o hcv3_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv3/RAxML/MAFFT.aln.raxml.bestTree -o hcv3_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv3/PhyML/MAFFT.phy_phyml_tree.txt -o hcv3_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv3/trueData/hcvTrueTree.tre -o hcv3_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv4/FastTree/fast.tre -o hcv4_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv4/IQTree/MAFFT.aln.treefile -o hcv4_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv4/IQTreeMFP/MAFFT.aln.treefile -o hcv4_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv4/RAxML/MAFFT.aln.raxml.bestTree -o hcv4_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv4/PhyML/MAFFT.phy_phyml_tree.txt -o hcv4_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv4/trueData/hcvTrueTree.tre -o hcv4_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv5/FastTree/fast.tre -o hcv5_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv5/IQTree/MAFFT.aln.treefile -o hcv5_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv5/IQTreeMFP/MAFFT.aln.treefile -o hcv5_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv5/RAxML/MAFFT.aln.raxml.bestTree -o hcv5_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv5/PhyML/MAFFT.phy_phyml_tree.txt -o hcv5_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv5/trueData/hcvTrueTree.tre -o hcv5_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv6/FastTree/fast.tre -o hcv6_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv6/IQTree/MAFFT.aln.treefile -o hcv6_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv6/IQTreeMFP/MAFFT.aln.treefile -o hcv6_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv6/RAxML/MAFFT.aln.raxml.bestTree -o hcv6_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv6/PhyML/MAFFT.phy_phyml_tree.txt -o hcv6_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv6/trueData/hcvTrueTree.tre -o hcv6_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv7/FastTree/fast.tre -o hcv7_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv7/IQTree/MAFFT.aln.treefile -o hcv7_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv7/IQTreeMFP/MAFFT.aln.treefile -o hcv7_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv7/RAxML/MAFFT.aln.raxml.bestTree -o hcv7_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv7/PhyML/MAFFT.phy_phyml_tree.txt -o hcv7_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv7/trueData/hcvTrueTree.tre -o hcv7_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv8/FastTree/fast.tre -o hcv8_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv8/IQTree/MAFFT.aln.treefile -o hcv8_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv8/IQTreeMFP/MAFFT.aln.treefile -o hcv8_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv8/RAxML/MAFFT.aln.raxml.bestTree -o hcv8_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv8/PhyML/MAFFT.phy_phyml_tree.txt -o hcv8_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv8/trueData/hcvTrueTree.tre -o hcv8_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv9/FastTree/fast.tre -o hcv9_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv9/IQTree/MAFFT.aln.treefile -o hcv9_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv9/IQTreeMFP/MAFFT.aln.treefile -o hcv9_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv9/RAxML/MAFFT.aln.raxml.bestTree -o hcv9_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv9/PhyML/MAFFT.phy_phyml_tree.txt -o hcv9_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hcv9/trueData/hcvTrueTree.tre -o hcv9_true
	
	@echo "FastTree Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_FastTree --correlation spearman 
	
	@echo "IQTree Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_IQTree --correlation spearman 
	
	@echo "IQTreeMFP Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_IQTreeMFP --correlation spearman 
	
	@echo "PhyML Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_PhyML --correlation spearman 
	
	@echo "RAxML Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_RAxML --correlation spearman 
	
	@echo "FastTree Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_FastTree --correlation pearson 
	
	@echo "IQTree Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_IQTree --correlation pearson 
	
	@echo "IQTreeMFP Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_IQTreeMFP --correlation pearson 
	
	@echo "PhyML Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_PhyML --correlation pearson 
	
	@echo "RAxML Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_RAxML --correlation pearson 
	
	@echo "FastTree ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_FastTree 
	
	@echo "IQTREE ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_IQTree 
	
	@echo "IQTreeMFP ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_IQTreeMFP 
	
	@echo "RAxML ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_RAxML 
	
	@echo "PhyML ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv0_true -d2 patristic_distances/hcv0_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv1_true -d2 patristic_distances/hcv1_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv2_true -d2 patristic_distances/hcv2_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv3_true -d2 patristic_distances/hcv3_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv4_true -d2 patristic_distances/hcv4_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv5_true -d2 patristic_distances/hcv5_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv6_true -d2 patristic_distances/hcv6_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv7_true -d2 patristic_distances/hcv7_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv8_true -d2 patristic_distances/hcv8_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hcv9_true -d2 patristic_distances/hcv9_PhyML 
	
	@rm -rf patristic_distances
		
rooting:
	@echo "FastTree MinVar"
	@./../helperScripts/delta_triplet_dist hcv0/trueData/hcvTrueTree.tre hcv0/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv1/trueData/hcvTrueTree.tre hcv1/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv2/trueData/hcvTrueTree.tre hcv2/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv3/trueData/hcvTrueTree.tre hcv3/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv4/trueData/hcvTrueTree.tre hcv4/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv5/trueData/hcvTrueTree.tre hcv5/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv6/trueData/hcvTrueTree.tre hcv6/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv7/trueData/hcvTrueTree.tre hcv7/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv8/trueData/hcvTrueTree.tre hcv8/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv9/trueData/hcvTrueTree.tre hcv9/FastTree/MinVarRooted.tre
	
	@echo "FastTree MidPoint"
	@./../helperScripts/delta_triplet_dist hcv0/trueData/hcvTrueTree.tre hcv0/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv1/trueData/hcvTrueTree.tre hcv1/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv2/trueData/hcvTrueTree.tre hcv2/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv3/trueData/hcvTrueTree.tre hcv3/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv4/trueData/hcvTrueTree.tre hcv4/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv5/trueData/hcvTrueTree.tre hcv5/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv6/trueData/hcvTrueTree.tre hcv6/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv7/trueData/hcvTrueTree.tre hcv7/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv8/trueData/hcvTrueTree.tre hcv8/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv9/trueData/hcvTrueTree.tre hcv9/FastTree/MidPointRooted.tre
	
	@echo "IQTree MinVar"
	@./../helperScripts/delta_triplet_dist hcv0/trueData/hcvTrueTree.tre hcv0/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv1/trueData/hcvTrueTree.tre hcv1/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv2/trueData/hcvTrueTree.tre hcv2/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv3/trueData/hcvTrueTree.tre hcv3/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv4/trueData/hcvTrueTree.tre hcv4/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv5/trueData/hcvTrueTree.tre hcv5/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv6/trueData/hcvTrueTree.tre hcv6/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv7/trueData/hcvTrueTree.tre hcv7/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv8/trueData/hcvTrueTree.tre hcv8/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv9/trueData/hcvTrueTree.tre hcv9/IQTree/MinVarRooted.tre
	
	@echo "IQTree MidPoint"
	@./../helperScripts/delta_triplet_dist hcv0/trueData/hcvTrueTree.tre hcv0/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv1/trueData/hcvTrueTree.tre hcv1/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv2/trueData/hcvTrueTree.tre hcv2/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv3/trueData/hcvTrueTree.tre hcv3/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv4/trueData/hcvTrueTree.tre hcv4/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv5/trueData/hcvTrueTree.tre hcv5/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv6/trueData/hcvTrueTree.tre hcv6/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv7/trueData/hcvTrueTree.tre hcv7/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv8/trueData/hcvTrueTree.tre hcv8/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv9/trueData/hcvTrueTree.tre hcv9/IQTree/MidPointRooted.tre
	
	@echo "IQTreeMFP MinVar"
	@./../helperScripts/delta_triplet_dist hcv0/trueData/hcvTrueTree.tre hcv0/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv1/trueData/hcvTrueTree.tre hcv1/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv2/trueData/hcvTrueTree.tre hcv2/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv3/trueData/hcvTrueTree.tre hcv3/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv4/trueData/hcvTrueTree.tre hcv4/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv5/trueData/hcvTrueTree.tre hcv5/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv6/trueData/hcvTrueTree.tre hcv6/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv7/trueData/hcvTrueTree.tre hcv7/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv8/trueData/hcvTrueTree.tre hcv8/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv9/trueData/hcvTrueTree.tre hcv9/IQTreeMFP/MinVarRooted.tre
	
	@echo "IQTreeMFP MidPoint"
	@./../helperScripts/delta_triplet_dist hcv0/trueData/hcvTrueTree.tre hcv0/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv1/trueData/hcvTrueTree.tre hcv1/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv2/trueData/hcvTrueTree.tre hcv2/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv3/trueData/hcvTrueTree.tre hcv3/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv4/trueData/hcvTrueTree.tre hcv4/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv5/trueData/hcvTrueTree.tre hcv5/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv6/trueData/hcvTrueTree.tre hcv6/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv7/trueData/hcvTrueTree.tre hcv7/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv8/trueData/hcvTrueTree.tre hcv8/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv9/trueData/hcvTrueTree.tre hcv9/IQTreeMFP/MidPointRooted.tre
	
	@echo "RAxML MinVar"
	@./../helperScripts/delta_triplet_dist hcv0/trueData/hcvTrueTree.tre hcv0/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv1/trueData/hcvTrueTree.tre hcv1/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv2/trueData/hcvTrueTree.tre hcv2/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv3/trueData/hcvTrueTree.tre hcv3/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv4/trueData/hcvTrueTree.tre hcv4/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv5/trueData/hcvTrueTree.tre hcv5/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv6/trueData/hcvTrueTree.tre hcv6/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv7/trueData/hcvTrueTree.tre hcv7/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv8/trueData/hcvTrueTree.tre hcv8/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv9/trueData/hcvTrueTree.tre hcv9/RAxML/MinVarRooted.tre
	
	@echo "RAxML MidPoint"
	@./../helperScripts/delta_triplet_dist hcv0/trueData/hcvTrueTree.tre hcv0/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv1/trueData/hcvTrueTree.tre hcv1/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv2/trueData/hcvTrueTree.tre hcv2/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv3/trueData/hcvTrueTree.tre hcv3/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv4/trueData/hcvTrueTree.tre hcv4/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv5/trueData/hcvTrueTree.tre hcv5/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv6/trueData/hcvTrueTree.tre hcv6/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv7/trueData/hcvTrueTree.tre hcv7/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv8/trueData/hcvTrueTree.tre hcv8/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv9/trueData/hcvTrueTree.tre hcv9/RAxML/MidPointRooted.tre
	
	@echo "PhyML MinVar"
	@./../helperScripts/delta_triplet_dist hcv0/trueData/hcvTrueTree.tre hcv0/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv1/trueData/hcvTrueTree.tre hcv1/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv2/trueData/hcvTrueTree.tre hcv2/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv3/trueData/hcvTrueTree.tre hcv3/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv4/trueData/hcvTrueTree.tre hcv4/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv5/trueData/hcvTrueTree.tre hcv5/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv6/trueData/hcvTrueTree.tre hcv6/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv7/trueData/hcvTrueTree.tre hcv7/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv8/trueData/hcvTrueTree.tre hcv8/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hcv9/trueData/hcvTrueTree.tre hcv9/PhyML/MinVarRooted.tre
		
	@echo "PhyML MidPoint"
	@./../helperScripts/delta_triplet_dist hcv0/trueData/hcvTrueTree.tre hcv0/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv1/trueData/hcvTrueTree.tre hcv1/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv2/trueData/hcvTrueTree.tre hcv2/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv3/trueData/hcvTrueTree.tre hcv3/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv4/trueData/hcvTrueTree.tre hcv4/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv5/trueData/hcvTrueTree.tre hcv5/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv6/trueData/hcvTrueTree.tre hcv6/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv7/trueData/hcvTrueTree.tre hcv7/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv8/trueData/hcvTrueTree.tre hcv8/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hcv9/trueData/hcvTrueTree.tre hcv9/PhyML/MidPointRooted.tre
