run: MAFFT FastTree IQTree IQTreeMFP RAxML PhyML FastRoot

MAFFT:
	cd hiv1/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv2/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv3/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv4/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv5/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv6/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv7/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv8/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv9/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln

FastTree:
	cd hiv1/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv2/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv3/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv4/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv5/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv6/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv7/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv8/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv9/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre

IQTree:
	cd hiv1/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv2/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv3/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv4/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv5/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv6/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv7/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv8/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv9/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO

IQTreeMFP:
	cd hiv1/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv2/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv3/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv4/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv5/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv6/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv7/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv8/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv9/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO

RAxML:
	cd hiv1/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv2/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv3/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv4/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv5/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv6/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv7/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv8/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv9/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G

PhyML:
	cd hiv1/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv2/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv3/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv4/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv5/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv6/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv7/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv8/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv9/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check

FastRoot:	
	cd hiv1/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hiv2/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hiv3/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hiv4/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hiv5/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hiv6/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hiv7/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hiv8/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	cd hiv9/FastTree && FastRoot.py -i fast.tre -m MV -o MinVarRooted.tre
	
	cd hiv1/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hiv2/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hiv3/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hiv4/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hiv5/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hiv6/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hiv7/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hiv8/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	cd hiv9/FastTree && FastRoot.py -i fast.tre -m MP -o MidPointRooted.tre
	
	cd hiv1/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv2/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv3/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv4/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv5/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv6/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv7/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv8/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv9/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	
	cd hiv1/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv2/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv3/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv4/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv5/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv6/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv7/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv8/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv9/IQTree && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	
	cd hiv1/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv2/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv3/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv4/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv5/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv6/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv7/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv8/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	cd hiv9/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MV -o MinVarRooted.tre
	
	cd hiv1/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv2/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv3/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv4/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv5/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv6/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv7/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv8/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	cd hiv9/IQTreeMFP && FastRoot.py -i MAFFT.aln.treefile -m MP -o MidPointRooted.tre
	
	cd hiv1/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hiv2/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hiv3/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hiv4/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hiv5/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hiv6/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hiv7/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hiv8/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	cd hiv9/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MV -o MinVarRooted.tre
	
	cd hiv1/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hiv2/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hiv3/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hiv4/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hiv5/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hiv6/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hiv7/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hiv8/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	cd hiv9/RAxML && FastRoot.py -i MAFFT.aln.raxml.bestTree -m MP -o MidPointRooted.tre
	
	cd hiv1/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hiv2/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hiv3/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hiv4/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hiv5/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hiv6/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hiv7/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hiv8/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	cd hiv9/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MV -o MinVarRooted.tre
	
	cd hiv1/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hiv2/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hiv3/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hiv4/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hiv5/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hiv6/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hiv7/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hiv8/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre
	cd hiv9/PhyML && FastRoot.py -i MAFFT.phy_phyml_tree.txt -m MP -o MidPointRooted.tre

msa:
	@./../helperScripts/fixFastaSpacing.py -i hiv1/MAFFT/MAFFT.aln
	@cat hiv1/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o MAFFTdists > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hiv1/trueData/hivTrueMSA.phy -o hiv1/trueData/hivTrueMSA.fasta
	@cat hiv1/trueData/hivTrueMSA.fasta | tn93 -t 1 -l 1 -q -o trueDists > /dev/null 2>&1
	@./../helperScripts/errorSq.py -d1 MAFFTdists -d2 trueDists 
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c spearman
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c pearson
	@rm trueDists MAFFTdists
	
	@./../helperScripts/fixFastaSpacing.py -i hiv2/MAFFT/MAFFT.aln
	@cat hiv2/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o MAFFTdists > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hiv2/trueData/hivTrueMSA.phy -o hiv2/trueData/hivTrueMSA.fasta
	@cat hiv2/trueData/hivTrueMSA.fasta | tn93 -t 1 -l 1 -q -o trueDists > /dev/null 2>&1
	@./../helperScripts/errorSq.py -d1 MAFFTdists -d2 trueDists 
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c spearman
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c pearson
	@rm trueDists MAFFTdists
	
	@./../helperScripts/fixFastaSpacing.py -i hiv3/MAFFT/MAFFT.aln
	@cat hiv3/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o MAFFTdists > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hiv3/trueData/hivTrueMSA.phy -o hiv3/trueData/hivTrueMSA.fasta
	@cat hiv3/trueData/hivTrueMSA.fasta | tn93 -t 1 -l 1 -q -o trueDists > /dev/null 2>&1
	@./../helperScripts/errorSq.py -d1 MAFFTdists -d2 trueDists 
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c spearman
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c pearson
	@rm trueDists MAFFTdists
	
	@./../helperScripts/fixFastaSpacing.py -i hiv4/MAFFT/MAFFT.aln
	@cat hiv4/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o MAFFTdists > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hiv4/trueData/hivTrueMSA.phy -o hiv4/trueData/hivTrueMSA.fasta
	@cat hiv4/trueData/hivTrueMSA.fasta | tn93 -t 1 -l 1 -q -o trueDists > /dev/null 2>&1
	@./../helperScripts/errorSq.py -d1 MAFFTdists -d2 trueDists 
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c spearman
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c pearson
	@rm trueDists MAFFTdists
	
	@./../helperScripts/fixFastaSpacing.py -i hiv5/MAFFT/MAFFT.aln
	@cat hiv5/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o MAFFTdists > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hiv5/trueData/hivTrueMSA.phy -o hiv5/trueData/hivTrueMSA.fasta
	@cat hiv5/trueData/hivTrueMSA.fasta | tn93 -t 1 -l 1 -q -o trueDists > /dev/null 2>&1
	@./../helperScripts/errorSq.py -d1 MAFFTdists -d2 trueDists 
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c spearman
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c pearson
	@rm trueDists MAFFTdists
	
	@./../helperScripts/fixFastaSpacing.py -i hiv6/MAFFT/MAFFT.aln
	@cat hiv6/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o MAFFTdists > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hiv6/trueData/hivTrueMSA.phy -o hiv6/trueData/hivTrueMSA.fasta
	@cat hiv6/trueData/hivTrueMSA.fasta | tn93 -t 1 -l 1 -q -o trueDists > /dev/null 2>&1
	@./../helperScripts/errorSq.py -d1 MAFFTdists -d2 trueDists 
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c spearman
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c pearson
	@rm trueDists MAFFTdists
	
	@./../helperScripts/fixFastaSpacing.py -i hiv7/MAFFT/MAFFT.aln
	@cat hiv7/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o MAFFTdists > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hiv7/trueData/hivTrueMSA.phy -o hiv7/trueData/hivTrueMSA.fasta
	@cat hiv7/trueData/hivTrueMSA.fasta | tn93 -t 1 -l 1 -q -o trueDists > /dev/null 2>&1
	@./../helperScripts/errorSq.py -d1 MAFFTdists -d2 trueDists 
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c spearman
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c pearson
	@rm trueDists MAFFTdists
	
	@./../helperScripts/fixFastaSpacing.py -i hiv8/MAFFT/MAFFT.aln
	@cat hiv8/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o MAFFTdists > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hiv8/trueData/hivTrueMSA.phy -o hiv8/trueData/hivTrueMSA.fasta
	@cat hiv8/trueData/hivTrueMSA.fasta | tn93 -t 1 -l 1 -q -o trueDists > /dev/null 2>&1
	@./../helperScripts/errorSq.py -d1 MAFFTdists -d2 trueDists 
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c spearman
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c pearson
	@rm trueDists MAFFTdists
	
	@./../helperScripts/fixFastaSpacing.py -i hiv9/MAFFT/MAFFT.aln
	@cat hiv9/MAFFT/MAFFT.aln | tn93 -t 1 -l 1 -q -o MAFFTdists > /dev/null 2>&1
	@../helperScripts/phy2fasta.py -i hiv9/trueData/hivTrueMSA.phy -o hiv9/trueData/hivTrueMSA.fasta
	@cat hiv9/trueData/hivTrueMSA.fasta | tn93 -t 1 -l 1 -q -o trueDists > /dev/null 2>&1
	@./../helperScripts/errorSq.py -d1 MAFFTdists -d2 trueDists 
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c spearman
	@./../helperScripts/mantel.py -d1 MAFFTdists -d2 trueDists -c pearson
	@rm trueDists MAFFTdists

inference:
	@echo "FastTree URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv1/FastTree/fast.tre -t2 ../hivTrials/hiv1/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv2/FastTree/fast.tre -t2 ../hivTrials/hiv2/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv3/FastTree/fast.tre -t2 ../hivTrials/hiv3/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv4/FastTree/fast.tre -t2 ../hivTrials/hiv4/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv5/FastTree/fast.tre -t2 ../hivTrials/hiv5/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv6/FastTree/fast.tre -t2 ../hivTrials/hiv6/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv7/FastTree/fast.tre -t2 ../hivTrials/hiv7/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv8/FastTree/fast.tre -t2 ../hivTrials/hiv8/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv9/FastTree/fast.tre -t2 ../hivTrials/hiv9/trueData/hivTrueTree.tre --metric URF --normalize 
	
	@echo "IQTree URF" 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv1/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv1/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv2/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv2/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv3/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv3/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv4/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv4/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv5/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv5/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv6/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv6/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv7/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv7/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv8/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv8/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv9/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv9/trueData/hivTrueTree.tre --metric URF --normalize 
	
	@echo "IQTreeMFP URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv1/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv1/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv2/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv2/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv3/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv3/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv4/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv4/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv5/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv5/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv6/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv6/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv7/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv7/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv8/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv8/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv9/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv9/trueData/hivTrueTree.tre --metric URF --normalize 
	
	@echo "RAxML URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv1/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv1/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv2/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv2/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv3/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv3/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv4/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv4/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv5/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv5/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv6/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv6/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv7/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv7/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv8/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv8/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv9/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv9/trueData/hivTrueTree.tre --metric URF --normalize 
	
	@echo "PhyML URF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv1/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv1/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv2/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv2/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv3/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv3/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv4/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv4/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv5/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv5/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv6/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv6/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv7/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv7/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv8/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv8/trueData/hivTrueTree.tre --metric URF --normalize 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv9/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv9/trueData/hivTrueTree.tre --metric URF --normalize 
	
	@echo "FastTree WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv1/FastTree/fast.tre -t2 ../hivTrials/hiv1/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv2/FastTree/fast.tre -t2 ../hivTrials/hiv2/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv3/FastTree/fast.tre -t2 ../hivTrials/hiv3/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv4/FastTree/fast.tre -t2 ../hivTrials/hiv4/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv5/FastTree/fast.tre -t2 ../hivTrials/hiv5/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv6/FastTree/fast.tre -t2 ../hivTrials/hiv6/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv7/FastTree/fast.tre -t2 ../hivTrials/hiv7/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv8/FastTree/fast.tre -t2 ../hivTrials/hiv8/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv9/FastTree/fast.tre -t2 ../hivTrials/hiv9/trueData/hivTrueTree.tre --metric WRF 
	
	@echo "IQTree WRF"	
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv1/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv1/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv2/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv2/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv3/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv3/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv4/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv4/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv5/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv5/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv6/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv6/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv7/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv7/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv8/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv8/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv9/IQTree/MAFFT.aln.treefile -t2 ../hivTrials/hiv9/trueData/hivTrueTree.tre --metric WRF 
	
	@echo "IQTreeMFP WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv1/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv1/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv2/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv2/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv3/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv3/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv4/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv4/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv5/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv5/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv6/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv6/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv7/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv7/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv8/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv8/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv9/IQTreeMFP/MAFFT.aln.treefile -t2 ../hivTrials/hiv9/trueData/hivTrueTree.tre --metric WRF 
	
	@echo "RAxML WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv1/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv1/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv2/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv2/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv3/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv3/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv4/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv4/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv5/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv5/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv6/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv6/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv7/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv7/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv8/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv8/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv9/RAxML/MAFFT.aln.raxml.bestTree -t2 ../hivTrials/hiv9/trueData/hivTrueTree.tre --metric WRF 
	
	@echo "PhyML WRF"
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv1/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv1/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv2/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv2/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv3/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv3/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv4/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv4/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv5/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv5/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv6/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv6/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv7/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv7/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv8/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv8/trueData/hivTrueTree.tre --metric WRF 
	@cd ../helperScripts && python3 nw_error.py -t1 ../hivTrials/hiv9/PhyML/MAFFT.phy_phyml_tree.txt -t2 ../hivTrials/hiv9/trueData/hivTrueTree.tre --metric WRF 
	
	@mkdir patristic_distances
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv1/FastTree/fast.tre -o hiv1_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv1/IQTree/MAFFT.aln.treefile -o hiv1_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv1/IQTreeMFP/MAFFT.aln.treefile -o hiv1_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv1/RAxML/MAFFT.aln.raxml.bestTree -o hiv1_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv1/PhyML/MAFFT.phy_phyml_tree.txt -o hiv1_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv1/trueData/hivTrueTree.tre -o hiv1_true
		
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv2/FastTree/fast.tre -o hiv2_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv2/IQTree/MAFFT.aln.treefile -o hiv2_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv2/IQTreeMFP/MAFFT.aln.treefile -o hiv2_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv2/RAxML/MAFFT.aln.raxml.bestTree -o hiv2_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv2/PhyML/MAFFT.phy_phyml_tree.txt -o hiv2_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv2/trueData/hivTrueTree.tre -o hiv2_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv3/FastTree/fast.tre -o hiv3_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv3/IQTree/MAFFT.aln.treefile -o hiv3_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv3/IQTreeMFP/MAFFT.aln.treefile -o hiv3_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv3/RAxML/MAFFT.aln.raxml.bestTree -o hiv3_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv3/PhyML/MAFFT.phy_phyml_tree.txt -o hiv3_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv3/trueData/hivTrueTree.tre -o hiv3_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv4/FastTree/fast.tre -o hiv4_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv4/IQTree/MAFFT.aln.treefile -o hiv4_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv4/IQTreeMFP/MAFFT.aln.treefile -o hiv4_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv4/RAxML/MAFFT.aln.raxml.bestTree -o hiv4_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv4/PhyML/MAFFT.phy_phyml_tree.txt -o hiv4_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv4/trueData/hivTrueTree.tre -o hiv4_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv5/FastTree/fast.tre -o hiv5_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv5/IQTree/MAFFT.aln.treefile -o hiv5_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv5/IQTreeMFP/MAFFT.aln.treefile -o hiv5_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv5/RAxML/MAFFT.aln.raxml.bestTree -o hiv5_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv5/PhyML/MAFFT.phy_phyml_tree.txt -o hiv5_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv5/trueData/hivTrueTree.tre -o hiv5_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv6/FastTree/fast.tre -o hiv6_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv6/IQTree/MAFFT.aln.treefile -o hiv6_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv6/IQTreeMFP/MAFFT.aln.treefile -o hiv6_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv6/RAxML/MAFFT.aln.raxml.bestTree -o hiv6_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv6/PhyML/MAFFT.phy_phyml_tree.txt -o hiv6_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv6/trueData/hivTrueTree.tre -o hiv6_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv7/FastTree/fast.tre -o hiv7_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv7/IQTree/MAFFT.aln.treefile -o hiv7_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv7/IQTreeMFP/MAFFT.aln.treefile -o hiv7_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv7/RAxML/MAFFT.aln.raxml.bestTree -o hiv7_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv7/PhyML/MAFFT.phy_phyml_tree.txt -o hiv7_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv7/trueData/hivTrueTree.tre -o hiv7_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv8/FastTree/fast.tre -o hiv8_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv8/IQTree/MAFFT.aln.treefile -o hiv8_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv8/IQTreeMFP/MAFFT.aln.treefile -o hiv8_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv8/RAxML/MAFFT.aln.raxml.bestTree -o hiv8_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv8/PhyML/MAFFT.phy_phyml_tree.txt -o hiv8_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv8/trueData/hivTrueTree.tre -o hiv8_true
	
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv9/FastTree/fast.tre -o hiv9_FastTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv9/IQTree/MAFFT.aln.treefile -o hiv9_IQTree
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv9/IQTreeMFP/MAFFT.aln.treefile -o hiv9_IQTreeMFP
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv9/RAxML/MAFFT.aln.raxml.bestTree -o hiv9_RAxML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv9/PhyML/MAFFT.phy_phyml_tree.txt -o hiv9_PhyML
	@cd patristic_distances && ./../../helperScripts/patristic_distances.py -i ../hiv9/trueData/hivTrueTree.tre -o hiv9_true
	
	@echo "FastTree Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_FastTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_FastTree --correlation spearman 
	
	@echo "IQTree Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_IQTree --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_IQTree --correlation spearman 
	
	@echo "IQTreeMFP Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_IQTreeMFP --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_IQTreeMFP --correlation spearman 
	
	@echo "PhyML Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_PhyML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_PhyML --correlation spearman 
	
	@echo "RAxML Mantel (Spearman)"
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_RAxML --correlation spearman 
	@./../helperScripts/mantel.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_RAxML --correlation spearman 
	
	@echo "FastTree Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_FastTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_FastTree --correlation pearson 
	
	@echo "IQTree Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_IQTree --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_IQTree --correlation pearson 
	
	@echo "IQTreeMFP Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_IQTreeMFP --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_IQTreeMFP --correlation pearson 
	
	@echo "PhyML Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_PhyML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_PhyML --correlation pearson 
	
	@echo "RAxML Mantel (Pearson)"
	@../helperScripts/mantel.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_RAxML --correlation pearson 
	@../helperScripts/mantel.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_RAxML --correlation pearson 
	
	@echo "FastTree ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_FastTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_FastTree 
	
	@echo "IQTREE ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_IQTree 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_IQTree 
	
	@echo "IQTreeMFP ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_IQTreeMFP 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_IQTreeMFP 
	
	@echo "RAxML ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_RAxML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_RAxML 
	
	@echo "PhyML ErrorSq"
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv1_true -d2 patristic_distances/hiv1_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv2_true -d2 patristic_distances/hiv2_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv3_true -d2 patristic_distances/hiv3_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv4_true -d2 patristic_distances/hiv4_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv5_true -d2 patristic_distances/hiv5_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv6_true -d2 patristic_distances/hiv6_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv7_true -d2 patristic_distances/hiv7_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv8_true -d2 patristic_distances/hiv8_PhyML 
	@../helperScripts/errorSq.py -d1 patristic_distances/hiv9_true -d2 patristic_distances/hiv9_PhyML 
	
	@rm -rf patristic_distances
		
rooting:
	@echo "FastTree MinVar"
	@./../helperScripts/delta_triplet_dist hiv1/trueData/hivTrueTree.tre hiv1/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv2/trueData/hivTrueTree.tre hiv2/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv3/trueData/hivTrueTree.tre hiv3/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv4/trueData/hivTrueTree.tre hiv4/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv5/trueData/hivTrueTree.tre hiv5/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv6/trueData/hivTrueTree.tre hiv6/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv7/trueData/hivTrueTree.tre hiv7/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv8/trueData/hivTrueTree.tre hiv8/FastTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv9/trueData/hivTrueTree.tre hiv9/FastTree/MinVarRooted.tre
	
	@echo "FastTree MidPoint"
	@./../helperScripts/delta_triplet_dist hiv1/trueData/hivTrueTree.tre hiv1/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv2/trueData/hivTrueTree.tre hiv2/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv3/trueData/hivTrueTree.tre hiv3/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv4/trueData/hivTrueTree.tre hiv4/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv5/trueData/hivTrueTree.tre hiv5/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv6/trueData/hivTrueTree.tre hiv6/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv7/trueData/hivTrueTree.tre hiv7/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv8/trueData/hivTrueTree.tre hiv8/FastTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv9/trueData/hivTrueTree.tre hiv9/FastTree/MidPointRooted.tre
	
	@echo "IQTree MinVar"
	@./../helperScripts/delta_triplet_dist hiv1/trueData/hivTrueTree.tre hiv1/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv2/trueData/hivTrueTree.tre hiv2/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv3/trueData/hivTrueTree.tre hiv3/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv4/trueData/hivTrueTree.tre hiv4/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv5/trueData/hivTrueTree.tre hiv5/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv6/trueData/hivTrueTree.tre hiv6/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv7/trueData/hivTrueTree.tre hiv7/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv8/trueData/hivTrueTree.tre hiv8/IQTree/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv9/trueData/hivTrueTree.tre hiv9/IQTree/MinVarRooted.tre
	
	@echo "IQTree MidPoint"
	@./../helperScripts/delta_triplet_dist hiv1/trueData/hivTrueTree.tre hiv1/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv2/trueData/hivTrueTree.tre hiv2/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv3/trueData/hivTrueTree.tre hiv3/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv4/trueData/hivTrueTree.tre hiv4/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv5/trueData/hivTrueTree.tre hiv5/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv6/trueData/hivTrueTree.tre hiv6/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv7/trueData/hivTrueTree.tre hiv7/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv8/trueData/hivTrueTree.tre hiv8/IQTree/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv9/trueData/hivTrueTree.tre hiv9/IQTree/MidPointRooted.tre
	
	@echo "IQTreeMFP MinVar"
	@./../helperScripts/delta_triplet_dist hiv1/trueData/hivTrueTree.tre hiv1/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv2/trueData/hivTrueTree.tre hiv2/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv3/trueData/hivTrueTree.tre hiv3/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv4/trueData/hivTrueTree.tre hiv4/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv5/trueData/hivTrueTree.tre hiv5/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv6/trueData/hivTrueTree.tre hiv6/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv7/trueData/hivTrueTree.tre hiv7/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv8/trueData/hivTrueTree.tre hiv8/IQTreeMFP/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv9/trueData/hivTrueTree.tre hiv9/IQTreeMFP/MinVarRooted.tre
	
	@echo "IQTreeMFP MidPoint"
	@./../helperScripts/delta_triplet_dist hiv1/trueData/hivTrueTree.tre hiv1/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv2/trueData/hivTrueTree.tre hiv2/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv3/trueData/hivTrueTree.tre hiv3/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv4/trueData/hivTrueTree.tre hiv4/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv5/trueData/hivTrueTree.tre hiv5/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv6/trueData/hivTrueTree.tre hiv6/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv7/trueData/hivTrueTree.tre hiv7/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv8/trueData/hivTrueTree.tre hiv8/IQTreeMFP/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv9/trueData/hivTrueTree.tre hiv9/IQTreeMFP/MidPointRooted.tre
	
	@echo "RAxML MinVar"
	@./../helperScripts/delta_triplet_dist hiv1/trueData/hivTrueTree.tre hiv1/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv2/trueData/hivTrueTree.tre hiv2/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv3/trueData/hivTrueTree.tre hiv3/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv4/trueData/hivTrueTree.tre hiv4/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv5/trueData/hivTrueTree.tre hiv5/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv6/trueData/hivTrueTree.tre hiv6/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv7/trueData/hivTrueTree.tre hiv7/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv8/trueData/hivTrueTree.tre hiv8/RAxML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv9/trueData/hivTrueTree.tre hiv9/RAxML/MinVarRooted.tre
	
	@echo "RAxML MidPoint"
	@./../helperScripts/delta_triplet_dist hiv1/trueData/hivTrueTree.tre hiv1/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv2/trueData/hivTrueTree.tre hiv2/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv3/trueData/hivTrueTree.tre hiv3/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv4/trueData/hivTrueTree.tre hiv4/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv5/trueData/hivTrueTree.tre hiv5/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv6/trueData/hivTrueTree.tre hiv6/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv7/trueData/hivTrueTree.tre hiv7/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv8/trueData/hivTrueTree.tre hiv8/RAxML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv9/trueData/hivTrueTree.tre hiv9/RAxML/MidPointRooted.tre
	
	@echo "PhyML MinVar"
	@./../helperScripts/delta_triplet_dist hiv1/trueData/hivTrueTree.tre hiv1/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv2/trueData/hivTrueTree.tre hiv2/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv3/trueData/hivTrueTree.tre hiv3/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv4/trueData/hivTrueTree.tre hiv4/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv5/trueData/hivTrueTree.tre hiv5/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv6/trueData/hivTrueTree.tre hiv6/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv7/trueData/hivTrueTree.tre hiv7/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv8/trueData/hivTrueTree.tre hiv8/PhyML/MinVarRooted.tre
	@./../helperScripts/delta_triplet_dist hiv9/trueData/hivTrueTree.tre hiv9/PhyML/MinVarRooted.tre
		
	@echo "PhyML MidPoint"
	@./../helperScripts/delta_triplet_dist hiv1/trueData/hivTrueTree.tre hiv1/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv2/trueData/hivTrueTree.tre hiv2/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv3/trueData/hivTrueTree.tre hiv3/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv4/trueData/hivTrueTree.tre hiv4/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv5/trueData/hivTrueTree.tre hiv5/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv6/trueData/hivTrueTree.tre hiv6/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv7/trueData/hivTrueTree.tre hiv7/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv8/trueData/hivTrueTree.tre hiv8/PhyML/MidPointRooted.tre
	@./../helperScripts/delta_triplet_dist hiv9/trueData/hivTrueTree.tre hiv9/PhyML/MidPointRooted.tre
