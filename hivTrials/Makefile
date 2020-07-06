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
