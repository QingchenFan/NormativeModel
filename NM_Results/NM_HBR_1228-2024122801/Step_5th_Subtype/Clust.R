library('NbClust')
bDataScale <- read.table("/Users/qingchen/Desktop/GrayVol246_Z_AllMDD.csv",sep=",")
optimal_indexes <- NbClust(bDataScale, min.nc = 2, max.nc = 10, distance="euclidean",method = "kmeans")
kmeans_result <- kmeans(bDataScale, centers = 2, nstart = 10)
bDataScale$cluster <- kmeans_result$cluster
print(kmeans_result$size) 
write.csv(bDataScale,"/Users/qingchen/Desktop/GrayVol246_Z_AllMDD.csv",row.names=FALSE)
print(kmeans_result$cluster) 
