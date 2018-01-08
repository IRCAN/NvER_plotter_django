from __future__ import unicode_literals

from django.db import models

class Fasta(models.Model) :
	nvertx_id = models.CharField(max_length=20, primary_key=True)
	fasta_sequence = models.CharField(max_length=20000,null=True)
	def __str__(self) :
		return self.nvertx_id

class Regen_cpm(models.Model) :
	nvertx_id = models.CharField(max_length=20,primary_key=True)
	regen_anc_UC = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_0HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_2HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_4HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_8HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_12HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_16HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_20HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_24HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_36HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_48HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_60HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_72HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_96HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_120HPA = models.FloatField(max_length=17,null=True,blank=True)
	regen_anc_144HPA = models.FloatField(max_length=17,null=True,blank=True)
	def __str__(self) :
		return self.nvertx_id


class Embryo_cpm(models.Model) :
	nvertx_id = models.CharField(max_length=20,primary_key=True)
	warner_anc_24HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_anc_48HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_anc_72HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_anc_96HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_anc_120HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_anc_144HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_anc_168HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_anc_192HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_0HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_1HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_2HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_3HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_4HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_5HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_6HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_7HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_8HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_9HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_10HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_11HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_12HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_13HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_14HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_15HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_16HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_17HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_18HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_anc_19HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_anc_2HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_anc_7HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_anc_12HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_anc_24HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_anc_120HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_anc_240HPF = models.FloatField(max_length=10,null=True,blank=True)
	mean_2HPF = models.FloatField(max_length=10,null=True,blank=True)
	mean_7HPF = models.FloatField(max_length=10,null=True,blank=True)
	mean_12HPF = models.FloatField(max_length=10,null=True,blank=True)
	mean_24HPF = models.FloatField(max_length=10,null=True,blank=True)
	mean_120HPF = models.FloatField(max_length=10,null=True,blank=True)
	def __str__(self) :
		return self.nvertx_id
		
class Embryo_SE(models.Model) :
	nvertx_id = models.CharField(max_length=20,primary_key=True)
	warner_se_24HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_se_48HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_se_72HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_se_96HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_se_120HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_se_144HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_se_168HPF = models.FloatField(max_length=10,null=True,blank=True)
	warner_se_192HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_0HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_1HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_2HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_3HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_4HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_5HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_6HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_7HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_8HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_9HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_10HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_11HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_12HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_13HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_14HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_15HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_16HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_17HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_18HPF = models.FloatField(max_length=10,null=True,blank=True)
	fischer_se_19HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_se_2HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_se_7HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_se_12HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_se_24HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_se_120HPF = models.FloatField(max_length=10,null=True,blank=True)
	helm_se_240HPF = models.FloatField(max_length=10,null=True,blank=True)
	def __str__(self) :
		return self.nvertx_id

class Annotation(models.Model) :
	nvertx_id = models.CharField(max_length=17,primary_key=True)
	Nemve1_tophit = models.CharField(max_length=60,null=True,blank=True)
	Nemve1_e_val = models.FloatField(max_length=150,null=True,blank=True)
	Mfuzz_R_Clust = models.CharField(max_length=4,null=True,blank=True)
	Mfuzz_R_Score = models.FloatField(max_length=10,null=True,blank=True)
	Mfuzz_E_Clust = models.CharField(max_length=4,null=True,blank=True)
	Mfuzz_E_Score = models.FloatField(max_length=10,null=True,blank=True)
	Uniprot_ID = models.CharField(max_length=10,null=True,blank=True)
	Uniprot_Description = models.CharField(max_length=100,null=True,blank=True)
	Top_nr_hit_eval = models.CharField(max_length=1000,null=True,blank=True)
	Other_nr_hits = models.CharField(max_length=10000,null=True,blank=True)
	def __str__(self) :
		return self.nvertx_id		

class Regen_SE(models.Model) :
	nvertx_id = models.CharField(max_length=20,primary_key=True)
	regen_se_UC = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_0HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_2HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_4HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_8HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_12HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_16HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_20HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_24HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_36HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_48HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_60HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_72HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_96HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_120HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_se_144HPA = models.FloatField(max_length=10,null=True,blank=True)
	def __str__(self) :
		return self.nvertx_id
		
class Regen_log_SE(models.Model) :
	nvertx_id = models.CharField(max_length=20,primary_key=True)
	regen_log_se_UC = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_0HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_2HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_4HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_8HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_12HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_16HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_20HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_24HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_36HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_48HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_60HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_72HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_96HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_120HPA = models.FloatField(max_length=10,null=True,blank=True)
	regen_log_se_144HPA = models.FloatField(max_length=10,null=True,blank=True)
	def __str__(self) :
		return self.nvertx_id

class Mfuzz(models.Model) :
	#name = models.CharField(max_length=20,primary_key=True)
	mfuzz_cluster_nb = models.CharField(max_length=4,primary_key=True)
	cluster_image = models.CharField(max_length=50)
	bp_plot_image = models.CharField(max_length=50)
	#def __str__(self) :
	#	return self.name

class de_table(models.Model) :
	nvertx_id = models.CharField(max_length=20,primary_key=True)
	Nemve1_tophit = models.CharField(max_length=60,null=True,blank=True)
	Uniprot_Description = models.CharField(max_length=100,null=True,blank=True)
	Top_nr_hit_eval = models.CharField(max_length=1000,null=True,blank=True)
	regen_0_2_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_2_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_2_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_2_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_2_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_4_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_4_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_4_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_4_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_4_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_8_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_8_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_8_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_8_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	regen_0_8_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_12_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_12_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_12_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_12_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	regen_0_12_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_16_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_16_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_16_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_16_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	regen_0_16_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_20_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_20_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_20_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_20_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_20_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_24_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_24_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_24_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_24_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	regen_0_24_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_36_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_36_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_36_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_36_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	regen_0_36_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_48_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_48_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_48_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_48_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	regen_0_48_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_60_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_60_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_60_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_60_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_60_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_72_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_72_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_72_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_72_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	regen_0_72_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_96_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_96_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_96_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_96_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	regen_0_96_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_120_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_120_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_120_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_120_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	regen_0_120_sig = models.CharField(max_length=10,null=True,blank=True)
	regen_0_144_logfc = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_144_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_144_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	regen_0_144_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	regen_0_144_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_8_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_8_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_8_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_8_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_8_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_9_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_9_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_9_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_9_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_9_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_10_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_10_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_10_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_10_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_10_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_11_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_11_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_11_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_11_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_11_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_12_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_12_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_12_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_12_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_12_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_13_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_13_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_13_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_13_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_13_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_14_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_14_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_14_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_14_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_14_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_15_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_15_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_15_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_15_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_15_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_16_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_16_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_16_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_16_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_16_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_17_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_17_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_17_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_17_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_17_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_18_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_18_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_18_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_18_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_18_sig = models.CharField(max_length=10,null=True,blank=True)
	fischer_7_19_logfc = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_19_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_19_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	fischer_7_19_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	fischer_7_19_sig = models.CharField(max_length=10,null=True,blank=True)
	helm_7_12_logfc = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_12_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_12_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_12_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	helm_7_12_sig = models.CharField(max_length=10,null=True,blank=True)
	helm_7_24_logfc = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_24_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_24_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_24_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	helm_7_24_sig = models.CharField(max_length=10,null=True,blank=True)
	helm_7_120_logfc = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_120_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_120_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_120_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	helm_7_120_sig = models.CharField(max_length=10,null=True,blank=True)
	helm_7_240_logfc = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_240_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_240_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	helm_7_240_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	helm_7_240_sig = models.CharField(max_length=10,null=True,blank=True)
	warner_24_48_logfc = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_48_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_48_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_48_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	warner_24_48_sig = models.CharField(max_length=10,null=True,blank=True)
	warner_24_72_logfc = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_72_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_72_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_72_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	warner_24_72_sig = models.CharField(max_length=10,null=True,blank=True)
	warner_24_96_logfc = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_96_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_96_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_96_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	warner_24_96_sig = models.CharField(max_length=10,null=True,blank=True)
	warner_24_120_logfc = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_120_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_120_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_120_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	warner_24_120_sig = models.CharField(max_length=10,null=True,blank=True)
	warner_24_144_logfc = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_144_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_144_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_144_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	warner_24_144_sig = models.CharField(max_length=10,null=True,blank=True)
	warner_24_168_logfc = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_168_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_168_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_168_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	warner_24_168_sig = models.CharField(max_length=10,null=True,blank=True)
	warner_24_192_logfc = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_192_logcpm = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_192_pvalue = models.FloatField(max_length=10,null=True,blank=True)
	warner_24_192_neglogfdr = models.FloatField(max_length=10,null=True,blank=True)	
	warner_24_192_sig = models.CharField(max_length=10,null=True,blank=True)
	def __str__(self) :
		return self.nvertx_id
