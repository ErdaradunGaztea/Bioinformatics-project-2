library(tidysq)
library(tidysqadv)

sequences <- read_fasta("data/all.fasta")
similarity <- computing_kernel(sequences$sq, max_kmer_length = 25)
rownames(similarity) <- sequences$name
colnames(similarity) <- sequences$name
write.csv(similarity, "input/similarity.csv")

distances <- -log(similarity)
write.csv(distances, "input/distances.csv", row.names = FALSE)
