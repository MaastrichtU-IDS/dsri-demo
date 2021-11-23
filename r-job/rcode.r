x <- rnorm(100)
res <- mean(x)
print("Running the R job again!!")
save(res, file="/data/results.rdata") 