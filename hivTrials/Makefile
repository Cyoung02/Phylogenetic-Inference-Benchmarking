MFFT:
	cd hiv1/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv2/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv3/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv4/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv5/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv6/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv7/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv8/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	cd hiv9/MAFFT && mafft --reorder --nomemsave --auto ../hivSeqs.fas > MAFFT.aln
	
	cd hiv1/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv2/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv3/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv4/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv5/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv6/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv7/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv8/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	cd hiv9/FastTree && cat ../MAFFT/MAFFT.aln | FastTree -gamma -nt -gtr -out fast.tre
	
	cd hiv1/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv2/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv3/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv4/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv5/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv6/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv7/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv8/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	cd hiv9/IQTree && cp ../MAFFT/MAFFT.aln . && iqtree -m GTR+I+R -s MAFFT.aln -nt AUTO
	
	cd hiv1/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv2/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv3/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv4/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv5/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv6/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv7/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv8/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	cd hiv9/IQTreeMFP && cp ../MAFFT/MAFFT.aln . && iqtree -m MFP -s MAFFT.aln -nt AUTO
	
	cd hiv1/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv2/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv3/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv4/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv5/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv6/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv7/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv8/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	cd hiv9/RAxML && cp ../MAFFT/MAFFT.aln . && raxml-ng --msa MAFFT.aln --model GTR+I+G
	
	cd hiv1/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv2/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv3/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv4/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv5/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv6/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv7/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv8/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	cd hiv9/PhyML && fasta2phylip.py -i ../MAFFT/MAFFT.aln -o MAFFT.phy && phyml -i MAFFT.phy -a e -d nt -m GTR --no_memory_check
	
continue:
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
